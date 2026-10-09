import pytest
import pytest_asyncio
import time

from jikan4.aiojikan import AioJikan


@pytest_asyncio.fixture
async def aiojikan():
    time.sleep(
        1
    )  # This is needed to prevent 429 Too Many Requests when resetting the rate limit

    client = AioJikan()
    yield client
    await client.close()


@pytest.mark.asyncio
async def test_default_base_url():
    assert AioJikan(rate_limit=0).base_url == "https://api.tenrai.org/v1"


@pytest.mark.asyncio
async def test_session_lifecycle():
    client = AioJikan(rate_limit=0)

    assert client.session is None
    await client.close()

    await client.get_anime(1)
    session = client.session

    assert session is not None
    assert not session.closed

    await client.close()

    assert session.closed


@pytest.mark.asyncio
async def test_get_anime(aiojikan: AioJikan):
    resp = await aiojikan.get_anime(1)

    assert resp.title == "Cowboy Bebop", "Response does not match expected response"


@pytest.mark.asyncio
async def test_get_anime_full(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_full(1)

    assert resp.title == "Cowboy Bebop", "Response does not match expected response"
    assert len(resp.streaming) > 0, "Response streaming list is empty"


@pytest.mark.asyncio
async def test_get_anime_full_filters(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = {}

    async def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {"data": {}}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.aiojikan.Anime", lambda **data: data)

    await client.get_anime_full(1, sfw=False, sfw_strict=True)

    assert captured == {
        "endpoint": "anime/1/full",
        "params": {"sfw": False, "sfw-strict": True},
    }


@pytest.mark.asyncio
async def test_get_anime_characters(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_characters(1)

    assert len(resp.data) > 0, "Response characters is empty"
    assert len(resp.data[0].voice_actors) > 0, "Response voice actors is empty"


@pytest.mark.asyncio
async def test_get_anime_staff(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_staff(1)

    assert len(resp.data) > 0, "Response staff is empty"
    assert len(resp.data[0].positions) > 0, "Response positions is empty"


@pytest.mark.asyncio
async def test_get_anime_episodes(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_episodes(1)

    assert len(resp.data) > 0, "Response episodes is empty"


@pytest.mark.asyncio
async def test_get_anime_episodes_page(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = {}

    async def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.aiojikan.AnimeEpisodes", lambda **data: data)

    await client.get_anime_episodes(1, page=0)

    assert captured == {
        "endpoint": "anime/1/episodes",
        "params": {"page": 0},
    }


@pytest.mark.asyncio
async def test_get_anime_episode(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_episode(1, 1)

    assert resp.synopsis is not None, "Response synopsis is empty"


@pytest.mark.asyncio
async def test_get_anime_news(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_news(1)

    assert {"pagination", "data"}.issubset(
        resp.__dict__
    ), "Response does not match expected response"


@pytest.mark.asyncio
async def test_get_anime_news_filters(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = {}

    async def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.aiojikan.AnimeNews", lambda **data: data)

    await client.get_anime_news(1, page=0, sfw=False, sfw_strict=True)

    assert captured == {
        "endpoint": "anime/1/news",
        "params": {"page": 0, "sfw": False, "sfw-strict": True},
    }


@pytest.mark.asyncio
async def test_search_anime(aiojikan: AioJikan):
    resp = await aiojikan.search_anime("tv", "naruto")

    assert {"pagination", "data"}.issubset(
        resp.__dict__
    ), "Response does not match expected response"
    assert len(resp.data) > 0, "Response data is empty"


@pytest.mark.asyncio
async def test_search_anime_filters(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = {}

    async def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)

    await client.search_anime(
        "tv",
        "naruto",
        page=2,
        limit=10,
        status="airing",
        score=8.5,
        min_score=7,
        max_score=9,
        rating="pg13",
        genres="1,2",
        genres_exclude="9",
        order_by="score",
        sort="desc",
        letter="N",
        producers="1",
        start_date="2020-01-01",
        end_date="2020-12-31",
        sfw=False,
        sfw_strict=True,
    )

    assert captured == {
        "endpoint": "anime",
        "params": {
            "q": "naruto",
            "page": 2,
            "type": "tv",
            "limit": 10,
            "status": "airing",
            "score": 8.5,
            "min_score": 7,
            "max_score": 9,
            "rating": "pg13",
            "genres": "1,2",
            "genres_exclude": "9",
            "order_by": "score",
            "sort": "desc",
            "letter": "N",
            "producers": "1",
            "start_date": "2020-01-01",
            "end_date": "2020-12-31",
            "sfw": False,
            "sfw-strict": True,
        },
    }


@pytest.mark.asyncio
async def test_ratelimit(aiojikan: AioJikan):
    start = time.time()
    for _ in range(10):
        await aiojikan.get_anime(1)
    end = time.time()

    max_per_minute = aiojikan.rate_limiter.calls_limit / aiojikan.rate_limiter.period

    assert end - start > 10 / (60 / max_per_minute), "Rate limit not working"


@pytest.mark.asyncio
async def test_get_anime_forum(aiojikan: AioJikan):
    resp = await aiojikan.get_anime_forum(1)

    assert len(resp.data) > 0, "Response data is empty"
    assert resp.data[0].url is not None, "Response url is empty"
    assert resp.data[0].last_comment.url is not None, "Response last_comment url is empty"


@pytest.mark.asyncio
async def test_get_anime_forum_filters(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = {}

    async def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.aiojikan.AnimeForum", lambda **data: data)

    await client.get_anime_forum(
        1,
        filter="episode",
        page=0,
        order_by="date",
        sort="desc",
    )

    assert captured == {
        "endpoint": "anime/1/forum",
        "params": {
            "filter": "episode",
            "page": 0,
            "order_by": "date",
            "sort": "desc",
        },
    }
