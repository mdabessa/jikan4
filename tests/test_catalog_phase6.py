import pytest

from jikan4 import routes
from jikan4.aiojikan import AioJikan
from jikan4.jikan import Jikan
from jikan4.models import Character, Person, Producer


@pytest.mark.parametrize(
    ("builder", "args", "expected"),
    [
        (routes.get_characters, (), ("characters", {})),
        (routes.get_character, (1,), ("characters/1", {})),
        (routes.get_character_full, (1,), ("characters/1/full", {})),
        (routes.get_character_anime, (1,), ("characters/1/anime", {})),
        (routes.get_character_manga, (1,), ("characters/1/manga", {})),
        (routes.get_character_articles, (1,), ("characters/1/articles", {})),
        (routes.get_character_pictures, (1,), ("characters/1/pictures", {})),
        (routes.get_character_voices, (1,), ("characters/1/voices", {})),
        (routes.get_character_ids, (), ("characters/ids", {})),
        (routes.get_people, (), ("people", {})),
        (routes.get_person, (1,), ("people/1", {})),
        (routes.get_person_full, (1,), ("people/1/full", {})),
        (routes.get_person_anime, (1,), ("people/1/anime", {})),
        (routes.get_person_manga, (1,), ("people/1/manga", {})),
        (routes.get_person_articles, (1,), ("people/1/articles", {})),
        (routes.get_person_pictures, (1,), ("people/1/pictures", {})),
        (routes.get_person_voices, (1,), ("people/1/voices", {})),
        (routes.get_person_ids, (), ("people/ids", {})),
        (routes.get_producers, (), ("producers", {})),
        (routes.get_producer, (1,), ("producers/1", {})),
        (routes.get_producer_full, (1,), ("producers/1/full", {})),
        (routes.get_producer_external, (1,), ("producers/1/external", {})),
        (routes.get_producer_ids, (), ("producers/ids", {})),
        (routes.get_genres_anime, (), ("genres/anime", {})),
        (routes.get_genres_manga, (), ("genres/manga", {})),
        (routes.get_magazines, (), ("magazines", {})),
    ],
)
def test_catalog_route_builders(builder, args, expected):
    assert builder(*args) == expected


def test_catalog_parameters_preserve_falsy_values():
    assert routes.get_characters(page=0, limit=0, order_by="mal_id", sort="desc") == (
        "characters",
        {"page": 0, "limit": 0, "order_by": "mal_id", "sort": "desc"},
    )
    assert routes.get_character_anime(1, sfw=False, sfw_strict=True) == (
        "characters/1/anime",
        {"sfw": False, "sfw-strict": True},
    )
    assert routes.get_genres_anime(filter="genres") == (
        "genres/anime",
        {"filter": "genres"},
    )


def test_catalog_models():
    assert Character(mal_id=1, name="Spike").name == "Spike"
    assert Person(mal_id=1, name="Mamoru Miyano").name == "Mamoru Miyano"
    assert Producer(mal_id=1, name="Sunrise").name == "Sunrise"


def test_sync_catalog_methods_use_routes(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = []

    def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint in {"characters/1", "people/1", "producers/1"}:
            return {"data": {"mal_id": 1, "name": "sample"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert client.get_character(1).name == "sample"
    assert client.get_person(1).name == "sample"
    assert client.get_producer(1).name == "sample"
    client.get_characters(page=0)
    client.get_people(page=0)
    client.get_genres_anime(filter="genres")
    client.get_magazines(page=0)

    assert captured == [
        ("characters/1", {}),
        ("people/1", {}),
        ("producers/1", {}),
        ("characters", {"page": 0}),
        ("people", {"page": 0}),
        ("genres/anime", {"filter": "genres"}),
        ("magazines", {"page": 0}),
    ]


@pytest.mark.asyncio
async def test_async_catalog_methods_use_routes(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = []

    async def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint in {"characters/1", "people/1", "producers/1"}:
            return {"data": {"mal_id": 1, "name": "sample"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert (await client.get_character(1)).name == "sample"
    assert (await client.get_person(1)).name == "sample"
    assert (await client.get_producer(1)).name == "sample"
    await client.get_characters(page=0)
    await client.get_people(page=0)
    await client.get_genres_anime(filter="genres")
    await client.get_magazines(page=0)

    assert captured == [
        ("characters/1", {}),
        ("people/1", {}),
        ("producers/1", {}),
        ("characters", {"page": 0}),
        ("people", {"page": 0}),
        ("genres/anime", {"filter": "genres"}),
        ("magazines", {"page": 0}),
    ]
