import pytest
import time

from jikan4.jikan import Jikan
from jikan4.utils.params import exclude_none


@pytest.fixture
def jikan():
    time.sleep(
        1
    )  # This is needed to prevent 429 Too Many Requests when resetting the rate limit

    return Jikan()


def test_default_base_url():
    assert Jikan(rate_limit=0).base_url == "https://api.tenrai.org/v1"


def test_exclude_none_preserves_falsy_values():
    assert exclude_none({"none": None, "false": False, "zero": 0}) == {
        "false": False,
        "zero": 0,
    }


def test_get_anime(jikan: Jikan):
    resp = jikan.get_anime(1)

    assert resp.title == "Cowboy Bebop", "Response does not match expected response"


def test_get_anime_full(jikan: Jikan):
    resp = jikan.get_anime_full(1)

    assert resp.title == "Cowboy Bebop", "Response does not match expected response"
    assert len(resp.streaming) > 0, "Response streaming list is empty"


def test_get_anime_full_filters(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = {}

    def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {"data": {}}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.jikan.Anime", lambda **data: data)

    client.get_anime_full(1, sfw=False, sfw_strict=True)

    assert captured == {
        "endpoint": "anime/1/full",
        "params": {"sfw": False, "sfw-strict": True},
    }


def test_get_anime_characters(jikan: Jikan):
    resp = jikan.get_anime_characters(1)

    assert len(resp.data) > 0, "Response characters is empty"
    assert len(resp.data[0].voice_actors) > 0, "Response voice actors is empty"


def test_get_anime_staff(jikan: Jikan):
    resp = jikan.get_anime_staff(1)

    assert len(resp.data) > 0, "Response staff is empty"
    assert len(resp.data[0].positions) > 0, "Response positions is empty"


def test_get_anime_episodes(jikan: Jikan):
    resp = jikan.get_anime_episodes(1)

    assert len(resp.data) > 0, "Response episodes is empty"


def test_get_anime_episodes_page(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = {}

    def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.jikan.AnimeEpisodes", lambda **data: data)

    client.get_anime_episodes(1, page=0)

    assert captured == {
        "endpoint": "anime/1/episodes",
        "params": {"page": 0},
    }


def test_get_anime_episode(jikan: Jikan):
    resp = jikan.get_anime_episode(1, 1)

    assert resp.synopsis is not None, "Response synopsis is empty"


def test_get_anime_news(jikan: Jikan):
    resp = jikan.get_anime_news(1)

    assert {"pagination", "data"}.issubset(
        resp.__dict__
    ), "Response does not match expected response"
    assert len(resp.data) > 0, "Response data is empty"


def test_get_anime_news_filters(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = {}

    def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.jikan.AnimeNews", lambda **data: data)

    client.get_anime_news(1, page=0, sfw=False, sfw_strict=True)

    assert captured == {
        "endpoint": "anime/1/news",
        "params": {"page": 0, "sfw": False, "sfw-strict": True},
    }


def test_search_anime(jikan: Jikan):
    resp = jikan.search_anime("tv", "naruto")

    assert {"pagination", "data"}.issubset(
        resp.__dict__
    ), "Response does not match expected response"
    assert len(resp.data) > 0, "Response data is empty"


def test_search_anime_filters(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = {}

    def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)

    client.search_anime(
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


def test_ratelimit(jikan: Jikan):
    start = time.time()
    for _ in range(10):
        jikan.get_anime(1)
    end = time.time()

    max_per_minute = jikan.rate_limiter.calls_limit / jikan.rate_limiter.period

    assert end - start > 10 / (60 / max_per_minute), "Rate limit not working"


def test_get_anime_forum(jikan: Jikan):
    resp = jikan.get_anime_forum(1)

    assert len(resp.data) > 0, "Response data is empty"
    assert resp.data[0].url is not None, "Response url is empty"
    assert resp.data[0].last_comment.url is not None, "Response last_comment url is empty"


def test_get_anime_forum_filters(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = {}

    def fake_get(endpoint, params):
        captured["endpoint"] = endpoint
        captured["params"] = params
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    monkeypatch.setattr("jikan4.jikan.AnimeForum", lambda **data: data)

    client.get_anime_forum(
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
