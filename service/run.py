from service import config
from service.app import app, context
from service.root import *


if __name__ == "__main__":
    app.run(host="sanic-baseline-server", port=8000, ssl=context)