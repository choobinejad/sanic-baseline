import requests


s = requests.Session()
s.cert = ('service/test/ssl/certs/client.crt', 'service/test/ssl/certs/client.key')
s.verify = 'service/test/ssl/certs/ca.crt'

r = s.get('https://sanic-baseline-server:8000/whoami/')
print(r.content)

