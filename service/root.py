from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc


root_blueprint = Blueprint('root', url_prefix='/', strict_slashes=True)
root_blueprint.static('favicon.ico', './static/favicon.ico')


@root_blueprint.route('/', methods=['GET', 'OPTIONS'])
@doc.summary("Hello, root path.")
@doc.produces(json)
async def root(request):
    """
    The API root function.
    :param request: sanic.request object
    :return: sanic.response.json
    """
    r = dict(
        hello='world'
    )
    return json(r)


@root_blueprint.route('/<integer_arg:int>', methods=['GET', 'OPTIONS'])
@doc.summary("Echo the args.")
@doc.produces(json)
async def root(request, integer_arg: int):
    """
    The API root function.
    :param request: sanic.request object
    :param integer_arg: a required integer argument
    :return: sanic.response.json
    """
    r = dict(
        hello='world',
        query_params=request.args,
        integer_arg=integer_arg
    )
    return json(r)
