from jikan4.routes import (
    get_anime,
    get_anime_characters,
    get_anime_episode,
    get_anime_episodes,
    get_anime_forum,
    get_anime_full,
    get_anime_news,
    get_anime_staff,
    search_anime,
)


def test_parameterless_route_builders():
    assert get_anime(1) == ("anime/1", {})
    assert get_anime_characters(1) == ("anime/1/characters", {})
    assert get_anime_staff(1) == ("anime/1/staff", {})
    assert get_anime_episode(1, 2) == ("anime/1/episodes/2", {})


def test_anime_full_builder_normalizes_parameters():
    assert get_anime_full(1, sfw=False, sfw_strict=True) == (
        "anime/1/full",
        {"sfw": False, "sfw-strict": True},
    )


def test_paginated_builders_preserve_zero_and_omit_none():
    assert get_anime_episodes(1, page=0) == ("anime/1/episodes", {"page": 0})
    assert get_anime_news(1, page=None, sfw=False) == (
        "anime/1/news",
        {"sfw": False},
    )
    assert get_anime_forum(1, page=0, sort=None) == (
        "anime/1/forum",
        {"page": 0},
    )


def test_search_builder_uses_tenrai_parameter_names():
    endpoint, params = search_anime(
        "tv",
        "naruto",
        page=0,
        genres_exclude="9",
        sfw=False,
        sfw_strict=True,
    )

    assert endpoint == "anime"
    assert params == {
        "q": "naruto",
        "page": 0,
        "type": "tv",
        "genres_exclude": "9",
        "sfw": False,
        "sfw-strict": True,
    }