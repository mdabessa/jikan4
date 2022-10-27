from jikan4.utils.cache import LRUCache


def test_cache_init():
    cache = LRUCache()
    assert cache.maxsize == 128, "Default maxsize should be 128"
    assert len(cache) == 0, "Cache should be empty"

def test_cache_decorator():
    cache = LRUCache(maxsize=2)

    @cache
    def add(a, b):
        return a + b

    assert add(1, 2) == 3, "Should return 3"
    assert add(1, 5) == 6, "Should return 6"
    assert add(1, 3) == 4, "Should return 4"
    assert add(1, 2) == 3, "Should return 3"
    assert add(4, 3) == 7, "Should return 7"

    assert len(cache) == 2, "Cache should have 2 items"
    assert ((1, 2) , frozenset({})) in cache, "Cache should have (1, 2) key"
    assert ((4, 3) , frozenset({})) in cache, "Cache should have (4, 3) key"
    assert ((1, 3) , frozenset({})) not in cache, "Cache should not have (1, 3) key"
    assert ((1, 5) , frozenset({})) not in cache, "Cache should not have (1, 5) key"

    assert add('a', b='b') == 'ab', "Should return 'ab'"
    assert (('a',), frozenset({('b', 'b')})) in cache, "Cache should have ('a', b='b') key"
