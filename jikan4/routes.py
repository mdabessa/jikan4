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


def search_manga(
    query: str | None = None,
    page: int = 1,
    limit: int | None = None,
    manga_type: str | None = None,
    status: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
    score: float | None = None,
    min_score: float | None = None,
    max_score: float | None = None,
    unapproved: bool | None = None,
    genres: str | None = None,
    genres_exclude: str | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
    magazines: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "q": query,
        "page": page,
        "limit": limit,
        "type": manga_type,
        "status": status,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
        "score": score,
        "min_score": min_score,
        "max_score": max_score,
        "unapproved": unapproved,
        "genres": genres,
        "genres_exclude": genres_exclude,
        "order_by": order_by,
        "sort": sort,
        "letter": letter,
        "magazines": magazines,
        "start_date": start_date,
        "end_date": end_date,
    }
    return "manga", exclude_none(params)


def get_manga(manga_id: int) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}", {}


def get_manga_full(
    manga_id: int,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/full", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_manga_recommendations(
    manga_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/recommendations", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_manga_characters(manga_id: int) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/characters", {}


def get_manga_news(
    manga_id: int,
    page: int | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/news", exclude_none(
        {"page": page, "sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_manga_articles(
    manga_id: int,
    page: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/articles", exclude_none(
        {"page": page, "order_by": order_by, "sort": sort}
    )


def get_manga_pictures(manga_id: int) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/pictures", {}


def get_manga_statistics(manga_id: int) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/statistics", {}


def get_manga_moreinfo(manga_id: int) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/moreinfo", {}


def get_manga_relations(
    manga_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/relations", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_manga_external(manga_id: int) -> tuple[str, dict[str, Any]]:
    return f"manga/{manga_id}/external", {}


def get_manga_reviews(
    manga_id: int,
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
    return f"manga/{manga_id}/reviews", exclude_none(params)


def get_manga_stacks(
    manga_id: int,
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
    return f"manga/{manga_id}/stacks", exclude_none(params)


def _get_manga_catalog(
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
    return f"manga/{resource}", exclude_none(params)


def get_manga_deleted(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_manga_catalog("deleted", **kwargs)


def get_manga_unapproved(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_manga_catalog("unapproved", **kwargs)


def get_manga_denied(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_manga_catalog("denied", **kwargs)


def get_manga_ids(
    type: str | None = None,
    status: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
    include: str | None = None,
    updated_at: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "type": type,
        "status": status,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
        "include": include,
        "updated_at": updated_at,
    }
    return "manga/ids", exclude_none(params)


def _get_catalog(
    resource: str,
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "q": q,
        "page": page,
        "limit": limit,
        "order_by": order_by,
        "sort": sort,
        "letter": letter,
    }
    return resource, exclude_none(params)


def get_characters(
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_catalog("characters", q, page, limit, order_by, sort, letter)


def get_character(character_id: int) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}", {}


def get_character_full(character_id: int) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}/full", {}


def get_character_anime(
    character_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}/anime", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_character_manga(
    character_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}/manga", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_character_articles(
    character_id: int,
    page: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}/articles", exclude_none(
        {"page": page, "order_by": order_by, "sort": sort}
    )


def get_character_pictures(character_id: int) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}/pictures", {}


def get_character_voices(character_id: int) -> tuple[str, dict[str, Any]]:
    return f"characters/{character_id}/voices", {}


def get_character_ids() -> tuple[str, dict[str, Any]]:
    return "characters/ids", {}


def get_people(
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_catalog("people", q, page, limit, order_by, sort, letter)


def get_person(person_id: int) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}", {}


def get_person_full(person_id: int) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}/full", {}


def get_person_anime(
    person_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}/anime", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_person_manga(
    person_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}/manga", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_person_articles(
    person_id: int,
    page: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}/articles", exclude_none(
        {"page": page, "order_by": order_by, "sort": sort}
    )


def get_person_pictures(person_id: int) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}/pictures", {}


def get_person_voices(
    person_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return f"people/{person_id}/voices", exclude_none(
        {"sfw": sfw, "sfw-strict": sfw_strict}
    )


def get_person_ids() -> tuple[str, dict[str, Any]]:
    return "people/ids", {}


def get_producers(
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_catalog("producers", q, page, limit, order_by, sort, letter)


def get_producer(producer_id: int) -> tuple[str, dict[str, Any]]:
    return f"producers/{producer_id}", {}


def get_producer_full(producer_id: int) -> tuple[str, dict[str, Any]]:
    return f"producers/{producer_id}/full", {}


def get_producer_external(producer_id: int) -> tuple[str, dict[str, Any]]:
    return f"producers/{producer_id}/external", {}


def get_producer_ids() -> tuple[str, dict[str, Any]]:
    return "producers/ids", {}


def get_genres_anime(filter: str | None = None) -> tuple[str, dict[str, Any]]:
    return "genres/anime", exclude_none({"filter": filter})


def get_genres_manga(filter: str | None = None) -> tuple[str, dict[str, Any]]:
    return "genres/manga", exclude_none({"filter": filter})


def get_magazines(
    q: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    letter: str | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_catalog("magazines", q, page, limit, order_by, sort, letter)


def get_random_anime(
    sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return "random/anime", exclude_none({"sfw": sfw, "sfw-strict": sfw_strict})


def get_random_manga(
    sfw: bool | None = None, sfw_strict: bool | None = None
) -> tuple[str, dict[str, Any]]:
    return "random/manga", exclude_none({"sfw": sfw, "sfw-strict": sfw_strict})


def get_random_character() -> tuple[str, dict[str, Any]]:
    return "random/characters", {}


def get_random_person() -> tuple[str, dict[str, Any]]:
    return "random/people", {}


def get_recommendations_anime(
    page: int | None = None,
    limit: int | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {"page": page, "limit": limit, "sfw": sfw, "sfw-strict": sfw_strict}
    return "recommendations/anime", exclude_none(params)


def get_recommendations_manga(
    page: int | None = None,
    limit: int | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {"page": page, "limit": limit, "sfw": sfw, "sfw-strict": sfw_strict}
    return "recommendations/manga", exclude_none(params)


def get_top_anime(
    page: int | None = None,
    limit: int | None = None,
    type: str | None = None,
    filter: str | None = None,
    rating: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "page": page,
        "limit": limit,
        "type": type,
        "filter": filter,
        "rating": rating,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return "top/anime", exclude_none(params)


def get_top_manga(
    page: int | None = None,
    limit: int | None = None,
    type: str | None = None,
    filter: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "page": page,
        "limit": limit,
        "type": type,
        "filter": filter,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return "top/manga", exclude_none(params)


def get_top_characters(
    page: int | None = None, limit: int | None = None
) -> tuple[str, dict[str, Any]]:
    return "top/characters", exclude_none({"page": page, "limit": limit})


def get_top_people(
    page: int | None = None, limit: int | None = None
) -> tuple[str, dict[str, Any]]:
    return "top/people", exclude_none({"page": page, "limit": limit})


def get_top_reviews(
    page: int | None = None,
    limit: int | None = None,
    type: str | None = None,
    preliminary: bool | None = None,
    spoilers: bool | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "page": page,
        "limit": limit,
        "type": type,
        "preliminary": preliminary,
        "spoilers": spoilers,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return "top/reviews", exclude_none(params)


def get_seasons() -> tuple[str, dict[str, Any]]:
    return "seasons", {}


def _get_season(
    endpoint: str,
    filter: str | None = None,
    rating: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
    unapproved: bool | None = None,
    continuing: bool | None = None,
    kids: bool | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    page: int | None = None,
    limit: int | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "filter": filter,
        "rating": rating,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
        "unapproved": unapproved,
        "continuing": continuing,
        "kids": kids,
        "order_by": order_by,
        "sort": sort,
        "page": page,
        "limit": limit,
    }
    return endpoint, exclude_none(params)


def get_season(
    year: int,
    season: str,
    filter: str | None = None,
    rating: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
    unapproved: bool | None = None,
    continuing: bool | None = None,
    kids: bool | None = None,
    order_by: str | None = None,
    sort: str | None = None,
    page: int | None = None,
    limit: int | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_season(
        f"seasons/{year}/{season}",
        filter,
        rating,
        sfw,
        sfw_strict,
        unapproved,
        continuing,
        kids,
        order_by,
        sort,
        page,
        limit,
    )


def get_seasons_now(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_season("seasons/now", **kwargs)


def get_seasons_previous(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_season("seasons/previous", **kwargs)


def get_seasons_upcoming(**kwargs: Any) -> tuple[str, dict[str, Any]]:
    return _get_season("seasons/upcoming", **kwargs)


def get_schedules(
    filter: str | None = None,
    kids: bool | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
    unapproved: bool | None = None,
    page: int | None = None,
    limit: int | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "filter": filter,
        "kids": kids,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
        "unapproved": unapproved,
        "page": page,
        "limit": limit,
    }
    return "schedules", exclude_none(params)


def _get_discovery_reviews(
    resource: str,
    page: int | None = None,
    limit: int | None = None,
    sort: str | None = None,
    preliminary: bool | None = None,
    spoilers: bool | None = None,
    sentiment: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    params = {
        "page": page,
        "limit": limit,
        "sort": sort,
        "preliminary": preliminary,
        "spoilers": spoilers,
        "sentiment": sentiment,
        "sfw": sfw,
        "sfw-strict": sfw_strict,
    }
    return resource, exclude_none(params)


def get_reviews_anime(
    page: int | None = None,
    limit: int | None = None,
    sort: str | None = None,
    preliminary: bool | None = None,
    spoilers: bool | None = None,
    sentiment: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_discovery_reviews(
        "reviews/anime", page, limit, sort, preliminary, spoilers, sentiment, sfw, sfw_strict
    )


def get_reviews_manga(
    page: int | None = None,
    limit: int | None = None,
    sort: str | None = None,
    preliminary: bool | None = None,
    spoilers: bool | None = None,
    sentiment: str | None = None,
    sfw: bool | None = None,
    sfw_strict: bool | None = None,
) -> tuple[str, dict[str, Any]]:
    return _get_discovery_reviews(
        "reviews/manga", page, limit, sort, preliminary, spoilers, sentiment, sfw, sfw_strict
    )