import pytest

from jikan4.aiojikan import AioJikan
from jikan4.jikan import Jikan
from jikan4 import routes


@pytest.mark.parametrize(
    ("builder", "expected"),
    [
        (routes.get_anime_recommendations, ("anime/1/recommendations", {"sfw": False})),
        (routes.get_anime_articles, ("anime/1/articles", {"page": 0})),
        (routes.get_anime_videos, ("anime/1/videos", {})),
        (routes.get_anime_episode_videos, ("anime/1/videos/episodes", {"page": 0})),
        (routes.get_anime_pictures, ("anime/1/pictures", {})),
        (routes.get_anime_statistics, ("anime/1/statistics", {})),
        (routes.get_anime_moreinfo, ("anime/1/moreinfo", {})),
        (routes.get_anime_relations, ("anime/1/relations", {"sfw-strict": True})),
        (routes.get_anime_themes, ("anime/1/themes", {})),
        (routes.get_anime_external, ("anime/1/external", {})),
        (routes.get_anime_streaming, ("anime/1/streaming", {})),
        (routes.get_anime_reviews, ("anime/1/reviews", {"page": 0, "spoilers": False})),
        (routes.get_anime_stacks, ("anime/1/stacks", {"page": 0, "official": False})),
    ],
)
def test_phase4_anime_routes(builder, expected):
    if builder is routes.get_anime_recommendations:
        result = builder(1, sfw=False)
    elif builder is routes.get_anime_relations:
        result = builder(1, sfw_strict=True)
    elif builder is routes.get_anime_articles:
        result = builder(1, page=0)
    elif builder is routes.get_anime_episode_videos:
        result = builder(1, page=0)
    elif builder is routes.get_anime_reviews:
        result = builder(1, page=0, spoilers=False)
    elif builder is routes.get_anime_stacks:
        result = builder(1, page=0, official=False)
    else:
        result = builder(1)
    assert result == expected


@pytest.mark.parametrize("resource", ["deleted", "unapproved", "denied"])
def test_anime_catalog_routes(resource):
    builder = getattr(routes, f"get_anime_{resource}")
    assert builder(page=0, sort="desc") == (
        f"anime/{resource}",
        {"page": 0, "sort": "desc"},
    )


def test_anime_ids_route_preserves_false():
    assert routes.get_anime_ids(sfw=False, sfw_strict=True) == (
        "anime/ids",
        {"sfw": False, "sfw-strict": True},
    )


def test_sync_phase4_methods_use_routes(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = []

    def fake_get(endpoint, params):
        captured.append((endpoint, params))
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    client.get_anime_recommendations(1, sfw=False)
    client.get_anime_episode_videos(1, page=0)
    client.get_anime_ids(sfw=False)

    assert captured == [
        ("anime/1/recommendations", {"sfw": False}),
        ("anime/1/videos/episodes", {"page": 0}),
        ("anime/ids", {"sfw": False}),
    ]


@pytest.mark.asyncio
async def test_async_phase4_methods_use_routes(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = []

    async def fake_get(endpoint, params):
        captured.append((endpoint, params))
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    await client.get_anime_recommendations(1, sfw=False)
    await client.get_anime_episode_videos(1, page=0)
    await client.get_anime_ids(sfw=False)

    assert captured == [
        ("anime/1/recommendations", {"sfw": False}),
        ("anime/1/videos/episodes", {"page": 0}),
        ("anime/ids", {"sfw": False}),
    ]
