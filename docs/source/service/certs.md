# Certificates

### Usage

To make sure that your clients are truly _your_ clients, you'll want to authenticate them.  

The sanic-baseline project:
1. Enforces client certificate authentication
2. Requires TLSv1.2
3. Uses only its own self-generated certificate authority.
4. Presents its own certificate for client to verify the service.

```python
# service/app.py
import ssl
from service import config
  
context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(config.TRUSTED_CA)
context.load_cert_chain(certfile=config.SERVER_CERT_PATH, keyfile=config.SERVER_KEY_PATH)
```
### Generate Certs

Generator.sh uses the configuration files in this directory to create your
certificate authority, as well as keys and signed certificates for both
the test server and the test client.

### Override the defaults

Override these self-signed certificates by updating `SERVER_CERT_PATH`, `SERVER_KEY_PATH`,
 and `TRUSTED_CA` in `service.config`.

