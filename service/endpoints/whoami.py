from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc


whoami_blueprint = Blueprint('whoami', url_prefix='/whoami', strict_slashes=True)


@whoami_blueprint.route('/', methods=['GET', 'OPTIONS'])
@doc.summary("See who you are.")
@doc.produces(json)
async def whoami(request):
    """
    See who you are!

    :return: sanic.response.json
    """

    r = dict(
        value='Hello, {}'.format(str(request.get('peer_dn').get('commonName'))),
        authorizations=request.get('authorizations')
    )

    return json(r)