from collections import OrderedDict
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
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in self.cache:
                return self.cache[key]
            else:
                value = func(*args, **kwargs)
                self[key] = value
                return value

        return wrapper

    def clear(self) -> None:
        self.cache.clear()