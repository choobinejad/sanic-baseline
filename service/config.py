

class Config(object):
    """
    A global configuration object that creates an environmental context for sanic-baseline modules to run in.

    """

    SERVER_CERT_PATH = './test/ssl/certs/server.crt'
    SERVER_KEY_PATH = './test/ssl/certs/server.key'
    TRUSTED_CA = './test/ssl/certs/ca.crt'

    def __init__(self):
        pass

    def setup(self,
              server_cert=None,
              server_key=None,
              trusted_ca=None):
        """
        Setup the app's configuration.

        :param server_cert: The signed server certificate.
        :param server_key: The server's private key.
        :param trusted_ca: The CA file which your server trusts.
        """

        if server_cert:
            self.SERVER_KEY_PATH = server_cert
        if server_key:
            self.SERVER_KEY_PATH = server_key
        if trusted_ca:
            self.TRUSTED_CA = trusted_ca
