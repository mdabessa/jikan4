import pytest

from jikan4 import aiojikan as async_client_module
from jikan4 import jikan as sync_client_module
from jikan4.aiojikan import AioJikan
from jikan4.jikan import Jikan
from jikan4 import routes


REQUEST_CASES = [
    pytest.param(
        "get_anime",
        (1,),
        {},
        routes.get_anime,
        {"data": {}},
        id="anime",
    ),
    pytest.param(
        "get_anime_full",
        (1, False, True),
        {},
        routes.get_anime_full,
        {"data": {}},
        id="anime-full-falsy-and-strict",
    ),
    pytest.param(
        "get_anime_characters",
        (1,),
        {},
        routes.get_anime_characters,
        {},
        id="anime-characters",
    ),
    pytest.param(
        "get_anime_staff",
        (1,),
        {},
        routes.get_anime_staff,
        {},
        id="anime-staff",
    ),
    pytest.param(
        "get_anime_episodes",
        (1, 0),
        {},
        routes.get_anime_episodes,
        {},
        id="anime-episodes-zero-page",
    ),
    pytest.param(
        "get_anime_episode",
        (1, 2),
        {},
        routes.get_anime_episode,
        {"data": {}},
        id="anime-episode",
    ),
    pytest.param(
        "get_anime_news",
        (1,),
        {"page": 0, "sfw": False, "sfw_strict": True},
        routes.get_anime_news,
        {},
        id="anime-news-falsy-and-strict",
    ),
    pytest.param(
        "search_anime",
        ("tv", "naruto", 0),
        {
            "limit": 0,
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
            "sfw_strict": True,
        },
        routes.search_anime,
        {},
        id="search-all-parameters",
    ),
    pytest.param(
        "search_anime",
        ("tv", "naruto"),
        {},
        routes.search_anime,
        {},
        id="search-defaults-and-none-omission",
    ),
    pytest.param(
        "get_anime_forum",
        (1,),
        {"filter": "episode", "page": 0, "order_by": "date", "sort": "desc"},
        routes.get_anime_forum,
        {},
        id="anime-forum-all-parameters",
    ),
]

MODEL_NAMES = (
    "Anime",
    "AnimeSearch",
    "AnimeCharacters",
    "AnimeStaff",
    "AnimeEpisodes",
    "Episode",
    "AnimeNews",
    "AnimeForum",
)


@pytest.mark.asyncio
@pytest.mark.parametrize("client_kind", ("sync", "async"))
@pytest.mark.parametrize(
    "method_name,args,kwargs,builder,response",
    REQUEST_CASES,
)
async def test_request_specs_are_identical_for_sync_and_async_clients(
    monkeypatch,
    client_kind,
    method_name,
    args,
    kwargs,
    builder,
    response,
):
    if client_kind == "async":
        client_module = async_client_module
        client = AioJikan(rate_limit=0)
    else:
        client_module = sync_client_module
        client = Jikan(rate_limit=0)

    for model_name in MODEL_NAMES:
        monkeypatch.setattr(client_module, model_name, lambda **data: data)

    captured = {}

    if client_kind == "async":

        async def fake_get(endpoint, params):
            captured["endpoint"] = endpoint
            captured["params"] = params
            return response

    else:

        def fake_get(endpoint, params):
            captured["endpoint"] = endpoint
            captured["params"] = params
            return response

    monkeypatch.setattr(client, "_get", fake_get)

    result = getattr(client, method_name)(*args, **kwargs)
    if client_kind == "async":
        result = await result

    endpoint, params = builder(*args, **kwargs)
    assert captured == {"endpoint": endpoint, "params": params}
    assert result == response.get("data", response)