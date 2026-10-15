import pytest

from jikan4 import routes
from jikan4.aiojikan import AioJikan
from jikan4.jikan import Jikan
from jikan4.models import Manga


@pytest.mark.parametrize(
    ("builder", "args", "expected"),
    [
        (routes.search_manga, (), ("manga", {"page": 1})),
        (routes.get_manga, (1,), ("manga/1", {})),
        (routes.get_manga_full, (1,), ("manga/1/full", {})),
        (routes.get_manga_recommendations, (1,), ("manga/1/recommendations", {})),
        (routes.get_manga_characters, (1,), ("manga/1/characters", {})),
        (routes.get_manga_news, (1,), ("manga/1/news", {})),
        (routes.get_manga_articles, (1,), ("manga/1/articles", {})),
        (routes.get_manga_pictures, (1,), ("manga/1/pictures", {})),
        (routes.get_manga_statistics, (1,), ("manga/1/statistics", {})),
        (routes.get_manga_moreinfo, (1,), ("manga/1/moreinfo", {})),
        (routes.get_manga_relations, (1,), ("manga/1/relations", {})),
        (routes.get_manga_external, (1,), ("manga/1/external", {})),
        (routes.get_manga_reviews, (1,), ("manga/1/reviews", {})),
        (routes.get_manga_stacks, (1,), ("manga/1/stacks", {})),
    ],
)
def test_manga_route_builders(builder, args, expected):
    assert builder(*args) == expected


@pytest.mark.parametrize("resource", ["deleted", "unapproved", "denied"])
def test_manga_catalog_routes(resource):
    builder = getattr(routes, f"get_manga_{resource}")
    assert builder(page=0, sort="desc") == (
        f"manga/{resource}",
        {"page": 0, "sort": "desc"},
    )


def test_manga_search_parameters_preserve_falsy_values():
    endpoint, params = routes.search_manga(
        query="berserk",
        page=0,
        sfw=False,
        sfw_strict=True,
        unapproved=False,
        genres_exclude="9",
    )

    assert endpoint == "manga"
    assert params == {
        "q": "berserk",
        "page": 0,
        "sfw": False,
        "sfw-strict": True,
        "unapproved": False,
        "genres_exclude": "9",
    }


def test_manga_ids_route():
    assert routes.get_manga_ids(sfw=False, sfw_strict=True) == (
        "manga/ids",
        {"sfw": False, "sfw-strict": True},
    )


def test_manga_model():
    manga = Manga(mal_id=1, url="https://myanimelist.net/manga/1")
    assert manga.mal_id == 1


def test_sync_manga_methods_use_routes(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = []

    def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint in {"manga/1", "manga/1/full"}:
            return {"data": {"mal_id": 1, "url": "https://example.test/manga/1"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert client.get_manga(1).mal_id == 1
    assert client.get_manga_full(1, sfw=False).mal_id == 1
    client.search_manga("berserk", page=0)
    client.get_manga_reviews(1, page=0, spoilers=False)
    client.get_manga_ids(sfw=False)

    assert captured == [
        ("manga/1", {}),
        ("manga/1/full", {"sfw": False}),
        ("manga", {"q": "berserk", "page": 0}),
        ("manga/1/reviews", {"page": 0, "spoilers": False}),
        ("manga/ids", {"sfw": False}),
    ]


@pytest.mark.asyncio
async def test_async_manga_methods_use_routes(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = []

    async def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint in {"manga/1", "manga/1/full"}:
            return {"data": {"mal_id": 1, "url": "https://example.test/manga/1"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert (await client.get_manga(1)).mal_id == 1
    assert (await client.get_manga_full(1, sfw=False)).mal_id == 1
    await client.search_manga("berserk", page=0)
    await client.get_manga_reviews(1, page=0, spoilers=False)
    await client.get_manga_ids(sfw=False)

    assert captured == [
        ("manga/1", {}),
        ("manga/1/full", {"sfw": False}),
        ("manga", {"q": "berserk", "page": 0}),
        ("manga/1/reviews", {"page": 0, "spoilers": False}),
        ("manga/ids", {"sfw": False}),
    ]
