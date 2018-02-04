"""
Provide a pluggable cache that can be wrapped around nearly anything in the service.
"""

from redis import StrictRedis
from expiringdict import ExpiringDict


redis = StrictRedis(host='localhost', port=32768, db=0)

auth_cache = ExpiringDict(max_len=5000, max_age_seconds=3600)

# TODO wrap the local and redis cache in a logical way
# TODO make sure to use the local and redis caches in the right order


def check_cache(namespace, key):
    name_key = f'{namespace}_{key}'

    # Short circuit
    if namespace == 'auth' and auth_cache.get(name_key) is not None:
        return auth_cache.get(name_key)

    # Check the cache backend
    v = redis.get(name_key)
    v = v.decode() if v is not None else None
    return v


def put_cache(namespace, key, value):
    name_key = f'{namespace}_{key}'
    if type(value) is list:
        value = ','.join(value)
    r = redis.set(name_key, value)
    return r
