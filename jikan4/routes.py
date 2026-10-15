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


def get_anime_recommendations(
    anime_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/recommendations", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_anime_articles(
    anime_id: int,
    page: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/articles", exclude_none(
        {"page": page, "order_by": order_by, "sort": sort}
    )


def get_anime_videos(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/videos", {}


def get_anime_episode_videos(
    anime_id: int, page: int | None = None
) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/videos/episodes", exclude_none({"page": page})


def get_anime_pictures(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/pictures", {}


def get_anime_statistics(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/statistics", {}


def get_anime_moreinfo(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/moreinfo", {}


def get_anime_relations(
    anime_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/relations", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_anime_themes(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/themes", {}


def get_anime_external(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/external", {}


def get_anime_streaming(anime_id: int) -> tuple[str, dict[str, Any]]:
    return f"anime/{anime_id}/streaming", {}


def get_anime_reviews(
    anime_id: int,
    page: int | None = None,
    sort: str | None = None,
    preliminary: bool | None = None,
    spoilers: bool | None = None,
    sentiment: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "page": page,
        "sort": sort,
        "preliminary": preliminary,
        "spoilers": spoilers,
        "sentiment": sentiment,
    }
    return f"anime/{anime_id}/reviews", exclude_none(params)


def get_anime_stacks(
    anime_id: int,
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    spoilers: bool | None = None,
    challenges: bool | None = None,
    official: bool | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "q": q,
        "page": page,
        "limit": limit,
        "order_by": order_by,
        "sort": sort,
        "spoilers": spoilers,
        "challenges": challenges,
        "official": official,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return f"anime/{anime_id}/stacks", exclude_none(params)


def _get_anime_catalog(
    resource: str,
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "q": q,
        "page": page,
        "limit": limit,
        "order_by": order_by,
        "sort": sort,
    }
    return f"anime/{resource}", exclude_none(params)


def get_anime_deleted(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_anime_catalog("deleted", **kwargs)


def get_anime_unapproved(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_anime_catalog("unapproved", **kwargs)


def get_anime_denied(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_anime_catalog("denied", **kwargs)


def get_anime_ids(
    type: str | None = None,
    status: str | None = None,
    rating: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
    include: str | None = None,
    updated_at: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "type": type,
        "status": status,
        "rating": rating,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
        "include": include,
        "updated_at": updated_at,
    }
    return "anime/ids", exclude_none(params)