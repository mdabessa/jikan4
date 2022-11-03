import pytest
import time

from jikan4.jikan import Jikan


@pytest.fixture
def jikan():
    time.sleep(
        1
    )  # This is needed to prevent 429 Too Many Requests when resetting the rate limit

    return Jikan(max_cache=100)


def test_get_anime_with_cache(jikan: Jikan):
    jikan.cache.clear()

    resp = jikan.get_anime(1)
    assert resp.title == "Cowboy Bebop", "Response does not match expected response"

    start = time.time()
    resp = jikan.get_anime(1)
    assert resp.title == "Cowboy Bebop", "Response does not match expected response"
    end = time.time()

    elapsed = end - start

    assert len(jikan.cache) == 1, "Cache length is not correct"
    assert elapsed < 1, "Cache is not working"


def test_search_anime_with_cache(jikan: Jikan):
    jikan.cache.clear()
    searchs = ["Cowboy Bebop", "Naruto", "Bleach", "One Piece", "Dragon Ball"]

    # Search with empty cache
    for search in searchs:
        resp = jikan.search_anime("tv", search)
        assert len(resp.data) > 0, "Response does not match expected response"

    # Search when already cached (should be faster)
    start = time.time()
    for search in searchs:
        resp = jikan.search_anime("tv", search)
        assert len(resp.data) > 0, "Response does not match expected response"

    end = time.time()

    elapsed = end - start

    assert len(jikan.cache) == len(searchs), "Cache length is not correct"
    assert elapsed < 1, "Cache is not working"
