import asyncio
from collections import OrderedDict, namedtuple
from typing import Any, Callable


class LRUCache:
    def __init__(self, maxsize=128) -> None:
        self.maxsize = maxsize
        self.cache = OrderedDict()

    def __getitem__(self, key) -> Any:
        return self.cache[key] # does not update order

    def __setitem__(self, key, value) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.maxsize:
            self.cache.popitem(last=False)

    def __contains__(self, key) -> bool:
        return key in self.cache

    def __len__(self) -> int:
        return len(self.cache)
    
    def __repr__(self) -> str:
        return repr(self.cache)

    def __call__(self, func) -> Callable:

        if not asyncio.iscoroutinefunction(func):
            def wrapper(*args, **kwargs):
                key = self.to_key(*args, **kwargs)
                if key in self.cache:
                    return self.cache[key]
                else:
                    value = func(*args, **kwargs)
                    self[key] = value
                    return value
        else:
            async def wrapper(*args, **kwargs):
                key = self.to_key(*args, **kwargs)
                if key in self.cache:
                    return self.cache[key]
                else:
                    value = await func(*args, **kwargs)
                    self[key] = value
                    return value


        return wrapper

    def clear(self) -> None:
        self.cache.clear()

    def dict_to_namedtuple(self, d: dict) -> namedtuple:
        if not d:
            return None

        keys, values = zip(*d.items())
        values = [self.dict_to_namedtuple(v) if isinstance(v, dict) else v for v in values]

        return namedtuple("CacheEntry", keys)(*values)

    def to_key(self, *args, **kwargs) -> Any:
        return self.dict_to_namedtuple({"args": args, "kwargs": kwargs})
