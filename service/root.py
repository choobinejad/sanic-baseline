from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc


root_blueprint = Blueprint('root', url_prefix='/', strict_slashes=True)
root_blueprint.static('favicon.ico', './static/favicon.ico')


class GenericResponse:
    hello = doc.String('It just says \'world.\'')
    query_params = doc.Dictionary('Your query string parameters.')
    integer_arg = doc.Integer('Your integer argument.')


@root_blueprint.route('/<integer_arg:int>', methods=['GET', 'OPTIONS'])
@doc.summary("Says Hello to the root path.")
@doc.produces(GenericResponse)
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
