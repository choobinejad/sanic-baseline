from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc


health_blueprint = Blueprint('health', url_prefix='/health', strict_slashes=True)


@health_blueprint.route('/', methods=['GET', 'OPTIONS'])
@doc.summary("Get health and stats about the service.")
@doc.produces(json)
async def health(request):
    """
    Get health and stats about the service.

    :return: sanic.response.json
    """

    r = dict(
        health='green'
    )

    return json(r)
