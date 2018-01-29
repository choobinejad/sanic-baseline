from sanic import Sanic
import ssl
from service import config
from sanic_cors import CORS
from sanic_openapi import swagger_blueprint, openapi_blueprint


from .root import root_blueprint


app = Sanic()
CORS(app)


context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=config.SERVER_CERT_PATH, keyfile=config.SERVER_KEY_PATH)
context.set_ciphers('TLSv1.2')


app.blueprint(root_blueprint)
app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)


app.config.API_VERSION = '0.1'
app.config.API_TITLE = 'sanic-baseline'
app.config.API_DESCRIPTION = 'A baseline project for Sanic with security features.'
app.config.API_TERMS_OF_SERVICE = 'Use with caution!'
app.config.API_PRODUCES_CONTENT_TYPES = ['application/json']
app.config.API_CONTACT_EMAIL = 'nope@nope.com'