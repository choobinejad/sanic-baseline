"""
The single entrypoint for starting the sanic-baseline service's web server.
"""

from service.app import app, context


if __name__ == "__main__":
    app.run(host="sanic-baseline-server", port=8000, ssl=context)
