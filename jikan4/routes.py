from typing import Any

from .utils.params import exclude_none


def get_anime(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}", {}


def get_anime_full(
    anime_id: int,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return f"anime/{anime_id}/full", exclude_none(params)


def get_anime_characters(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/characters", {}


def get_anime_staff(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/staff", {}


def get_anime_episodes(
    anime_id: int, page: int | None = None
) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/episodes", exclude_none({"page": page})


def get_anime_episode(anime_id: int, episode: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/episodes/{episode}", {}


def get_anime_news(
    anime_id: int,
    page: int | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "page": page,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return f"anime/{anime_id}/news", exclude_none(params)


def search_anime(
    search_type: str,
    query: str,
    page: int = 1,
    limit: int | None = None,
    status: str | None = None,
    score: float | None = None,
    min_score: float | None = None,
    max_score: float | None = None,
    rating: str | None = None,
    genres: str | None = None,
    genres_exclude: str | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
    producers: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "q": query,
        "page": page,
        "type": search_type,
        "limit": limit,
        "status": status,
        "score": score,
        "min_score": min_score,
        "max_score": max_score,
        "rating": rating,
        "genres": genres,
        "genres_exclude": genres_exclude,
        "order_by": order_by,
        "sort": sort,
        "letter": letter,
        "producers": producers,
        "start_date": start_date,
        "end_date": end_date,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return "anime", exclude_none(params)


def get_anime_forum(
    anime_id: int,
    filter: str | None = None,
    page: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "filter": filter,
        "page": page,
        "order_by": order_by,
        "sort": sort,
    }
    return f"anime/{anime_id}/forum", exclude_none(params)