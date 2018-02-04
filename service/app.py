"""
Create, configure, and define routing for a Sanic application. Implement middleware for authorization and XSS
protection.
"""

import ssl
from hashlib import sha256
from collections import OrderedDict

from sanic import Sanic
from sanic.exceptions import Forbidden

from sanic_cors import CORS
from sanic_openapi import swagger_blueprint, openapi_blueprint

from service import app_conf

from service.resources.cache import check_cache, put_cache
from service.resources.auth_backend import users
from service.resources.aio_lru_cache import async_lru
from service.endpoints.root import root_blueprint
from service.endpoints.whoami import whoami_blueprint
from service.endpoints.health import health_blueprint


app = Sanic()
CORS(app)


# Require client certificate authentication and TLSv1.2
context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(app_conf.TRUSTED_CA)
context.load_cert_chain(certfile=app_conf.SERVER_CERT_PATH, keyfile=app_conf.SERVER_KEY_PATH)


# Add all the blueprints. openapi and swagger are built in by sanic_openapi
app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)
app.blueprint(root_blueprint)
app.blueprint(whoami_blueprint)
app.blueprint(health_blueprint)


app.config.API_VERSION = '0.1'
app.config.API_TITLE = 'sanic-baseline'
app.config.API_DESCRIPTION = 'A baseline project for Sanic with security features.'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
app.config.API_CONTACT_EMAIL = 'nope@nope.com'


@async_lru(size=1024)
async def authorize(user_id):
    """

    :param user_id: The SHA256 user_id created by `get_client_identity`
    :return: user authorizations
    """
    auth = users.get(user_id, [])
    return auth


@app.middleware('request')
async def get_client_identity(request):
    """
    Intercept all requests to parse the peer's DN and create a user_id. Look up the peer's authorizations.

    Reject requests with `403 Forbidden` if the user has no authorizations

    :param request: sanic.request
    :return: sanix.request
    """

    # For each request, parse the peer's DN and form a user ID.
    peer_cert = request.transport._ssl_protocol._extra['peercert']
    subject = OrderedDict([x[0] for x in peer_cert.get('subject')])
    request['peer_dn'] = subject
    request['user_id'] = sha256(str(subject).encode()).hexdigest()

    # Check the peer's authorizations.
    auths = await authorize(request['user_id'])

    # If no authorizations, raise 403 Forbidden
    if len(auths) == 0:
        raise Forbidden('Forbidden')
    # Otherwise include peer's authorizations.
    request['authorizations'] = auths


# @app.middleware('response')
# async def halt_response(request, response):
#     # Use middleware of this form to implement a security filter on outgoing data.
#     return text('Stopped response for security reasons.')


@app.middleware('response')
async def prevent_xss(request, response):
    """
    Add the `x-xss-protection` header to all responses.

    :param request: sanic.request
    :param response: sanic.response
    :return: sanic.response
    """
    response.headers["x-xss-protection"] = "1; mode=block"


# Listener works in these modes: before_server_start, after_server_start, before_server_stop, after_server_stop
# @app.listener('before_server_start')
# async def setup_db(app, loop):
#     # Do some kind of setup or teardown.
#     pass
