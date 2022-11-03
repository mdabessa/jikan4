import pytest
import time

from jikan4.aiojikan import AioJikan


@pytest.fixture
def aiojikan():
    time.sleep(
        1
    )  # This is needed to prevent 429 Too Many Requests when resetting the rate limit

    return AioJikan(max_cache=100)


@pytest.mark.asyncio
async def test_get_anime_with_cache(aiojikan: AioJikan):
    aiojikan.cache.clear()

    resp = await aiojikan.get_anime(1)
    assert resp.title == "Cowboy Bebop", "Response does not match expected response"

    start = time.time()
    resp = await aiojikan.get_anime(1)
    assert resp.title == "Cowboy Bebop", "Response does not match expected response"
    end = time.time()

    elapsed = end - start

    assert len(aiojikan.cache) == 1, "Cache length is not correct"
    assert elapsed < 1, "Cache is not working"

@pytest.mark.asyncio
async def test_search_anime_with_cache(aiojikan: AioJikan):
    aiojikan.cache.clear()
    searchs = ["Cowboy Bebop", "Naruto", "Bleach", "One Piece", "Dragon Ball"]

    # Search with empty cache
    for search in searchs:
        resp = await aiojikan.search_anime('tv', search)
        assert len(resp.data) > 0, "Response does not match expected response"

    # Search when already cached (should be faster)
    start = time.time()
    for search in searchs:
        resp = await aiojikan.search_anime('tv', search)
        assert len(resp.data) > 0, "Response does not match expected response"

    end = time.time()

    elapsed = end - start


    assert len(aiojikan.cache) == len(searchs), "Cache length is not correct"
    assert elapsed < 1, "Cache is not working"
