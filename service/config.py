

class Config(object):

    SERVER_CERT_PATH = './test/ssl/certs/server.crt'
    SERVER_KEY_PATH = './test/ssl/certs/server.key'

    def __init__(self,
                 server_cert=None,
                 server_key=None):

        if server_cert is not None:
            self.SERVER_KEY_PATH = server_cert
        if server_key is not None:
            self.SERVER_KEY_PATH = server_key
