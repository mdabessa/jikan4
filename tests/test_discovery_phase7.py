import pytest

from jikan4 import routes
from jikan4.aiojikan import AioJikan
from jikan4.jikan import Jikan
from jikan4.models import Anime, Character, Manga, Person


@pytest.mark.parametrize(
    ("builder", "args", "expected"),
    [
        (routes.get_random_anime, (), ("random/anime", {})),
        (routes.get_random_manga, (), ("random/manga", {})),
        (routes.get_random_character, (), ("random/characters", {})),
        (routes.get_random_person, (), ("random/people", {})),
        (routes.get_recommendations_anime, (), ("recommendations/anime", {})),
        (routes.get_recommendations_manga, (), ("recommendations/manga", {})),
        (routes.get_top_anime, (), ("top/anime", {})),
        (routes.get_top_manga, (), ("top/manga", {})),
        (routes.get_top_characters, (), ("top/characters", {})),
        (routes.get_top_people, (), ("top/people", {})),
        (routes.get_top_reviews, (), ("top/reviews", {})),
        (routes.get_seasons, (), ("seasons", {})),
        (routes.get_season, (2026, "winter"), ("seasons/2026/winter", {})),
        (routes.get_seasons_now, (), ("seasons/now", {})),
        (routes.get_seasons_previous, (), ("seasons/previous", {})),
        (routes.get_seasons_upcoming, (), ("seasons/upcoming", {})),
        (routes.get_schedules, (), ("schedules", {})),
        (routes.get_reviews_anime, (), ("reviews/anime", {})),
        (routes.get_reviews_manga, (), ("reviews/manga", {})),
    ],
)
def test_discovery_route_builders(builder, args, expected):
    assert builder(*args) == expected


def test_discovery_parameters_preserve_falsy_values():
    assert routes.get_random_anime(sfw=False, sfw_strict=True) == (
        "random/anime",
        {"sfw": False, "sfw-strict": True},
    )
    assert routes.get_top_anime(page=0, limit=0, sfw=False) == (
        "top/anime",
        {"page": 0, "limit": 0, "sfw": False},
    )
    assert routes.get_seasons_now(continuing=False, page=0) == (
        "seasons/now",
        {"continuing": False, "page": 0},
    )
    assert routes.get_reviews_manga(spoilers=False, sfw_strict=True) == (
        "reviews/manga",
        {"spoilers": False, "sfw-strict": True},
    )


def test_seasons_index_model_shape():
    client = Jikan(rate_limit=0)
    client._get = lambda endpoint, params: {
        "data": [{"year": 2026, "seasons": ["winter", "spring"]}]
    }
    seasons = client.get_seasons()
    assert seasons.data[0].year == 2026
    assert seasons.data[0].seasons == ["winter", "spring"]


def test_sync_discovery_methods_use_routes(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = []

    def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint == "random/anime":
            return {"data": {"mal_id": 1, "url": "https://example.test/anime/1"}}
        if endpoint == "random/manga":
            return {"data": {"mal_id": 1, "url": "https://example.test/manga/1"}}
        if endpoint == "random/characters":
            return {"data": {"mal_id": 1, "name": "sample"}}
        if endpoint == "random/people":
            return {"data": {"mal_id": 1, "name": "sample"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert isinstance(client.get_random_anime(), Anime)
    assert isinstance(client.get_random_manga(), Manga)
    assert isinstance(client.get_random_character(), Character)
    assert isinstance(client.get_random_person(), Person)
    client.get_top_anime(page=0, sfw=False)
    client.get_seasons_now(continuing=False, page=0)
    client.get_schedules(page=0)
    client.get_reviews_anime(spoilers=False)

    assert captured == [
        ("random/anime", {}),
        ("random/manga", {}),
        ("random/characters", {}),
        ("random/people", {}),
        ("top/anime", {"page": 0, "sfw": False}),
        ("seasons/now", {"continuing": False, "page": 0}),
        ("schedules", {"page": 0}),
        ("reviews/anime", {"spoilers": False}),
    ]


@pytest.mark.asyncio
async def test_async_discovery_methods_use_routes(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = []

    async def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint == "random/anime":
            return {"data": {"mal_id": 1, "url": "https://example.test/anime/1"}}
        if endpoint == "random/manga":
            return {"data": {"mal_id": 1, "url": "https://example.test/manga/1"}}
        if endpoint == "random/characters":
            return {"data": {"mal_id": 1, "name": "sample"}}
        if endpoint == "random/people":
            return {"data": {"mal_id": 1, "name": "sample"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert isinstance(await client.get_random_anime(), Anime)
    assert isinstance(await client.get_random_manga(), Manga)
    assert isinstance(await client.get_random_character(), Character)
    assert isinstance(await client.get_random_person(), Person)
    await client.get_top_anime(page=0, sfw=False)
    await client.get_seasons_now(continuing=False, page=0)
    await client.get_schedules(page=0)
    await client.get_reviews_anime(spoilers=False)

    assert captured == [
        ("random/anime", {}),
        ("random/manga", {}),
        ("random/characters", {}),
        ("random/people", {}),
        ("top/anime", {"page": 0, "sfw": False}),
        ("seasons/now", {"continuing": False, "page": 0}),
        ("schedules", {"page": 0}),
        ("reviews/anime", {"spoilers": False}),
    ]
