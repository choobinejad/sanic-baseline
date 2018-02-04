"""
Provide an LRU cache that works as a decorator. Review https://en.wikipedia.org/wiki/Cache_replacement_policies for
information about an `LRU` cache, and other cache implementations.
"""

import functools
from collections import OrderedDict


def async_lru(size=128):
    """
    Since functools.lru_cache can't decorate an async coroutine, this decorator
    uses a collections.OrderedDict to get the job done in an async world.

    :param size: The maximum size of the LRU cache.
    :return: decorator
    """
    cache = OrderedDict()

    def decorator(fn):
        @functools.wraps(fn)
        async def memoizer(*args, **kwargs):
            key = str((args, kwargs))
            try:
                cache[key] = cache.pop(key)
            except KeyError:
                if len(cache) >= size:
                    cache.popitem(last=False)
                cache[key] = await fn(*args, **kwargs)
            return cache[key]
        return memoizer
    return decorator