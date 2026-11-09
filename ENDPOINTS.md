# Endpoint reference

Every Tenrai v1 endpoint exposed by `jikan4`. Each row maps a client method to
the HTTP request it sends and the [Pydantic model](jikan4/models.py) it returns.

The same 97 methods exist on both clients, so this list applies to `Jikan` and
`AioJikan` alike:

| Client | Import | Call style |
| --- | --- | --- |
| `Jikan` | `from jikan4 import Jikan` | `jikan.get_anime(1)` |
| `AioJikan` | `from jikan4 import AioJikan` | `await jikan.get_anime(1)` |

## Conventions

- **Method** — arguments in parentheses are positional and required.
- **Endpoint** — `{id}` is the resource identifier (anime, manga, character,
  person, producer, stack, article or news ID); any other braces are named path
  parameters.
- **Parameters** — keyword arguments. All are optional, are sent as query
  parameters, and are omitted from the request when left as `None`.
- **Returns** — the model parsed from the response.

> **Server key required:** the `…/ids` endpoints need a Tenrai server key that
> the client does not send, so `get_anime_ids`, `get_manga_ids`,
> `get_character_ids`, `get_person_ids` and `get_producer_ids` return an HTTP
> `401` error against the default backend.

## Index

- [Anime](#anime) — 26 methods
- [Manga](#manga) — 18 methods
- [Characters](#characters) — 9 methods
- [People](#people) — 9 methods
- [Producers](#producers) — 5 methods
- [Genres & magazines](#genres--magazines) — 3 methods
- [Seasons & schedules](#seasons--schedules) — 6 methods
- [Top lists](#top-lists) — 5 methods
- [Recommendations](#recommendations) — 2 methods
- [Random](#random) — 4 methods
- [Reviews](#reviews) — 2 methods
- [Stacks](#stacks) — 2 methods
- [Articles](#articles) — 3 methods
- [News](#news) — 3 methods

## Anime

Anime lookup, sub-resources, search and the catalog listings.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_anime(anime_id)` | `GET /anime/{id}` | — | `Anime` |
| `get_anime_full(anime_id)` | `GET /anime/{id}/full` | `sfw`, `sfw_strict` | `Anime` |
| `get_anime_characters(anime_id)` | `GET /anime/{id}/characters` | — | `AnimeCharacters` |
| `get_anime_staff(anime_id)` | `GET /anime/{id}/staff` | — | `AnimeStaff` |
| `get_anime_episodes(anime_id)` | `GET /anime/{id}/episodes` | `page` | `AnimeEpisodes` |
| `get_anime_episode(anime_id, episode)` | `GET /anime/{id}/episodes/{episode}` | — | `Episode` |
| `get_anime_news(anime_id)` | `GET /anime/{id}/news` | `page`, `sfw`, `sfw_strict` | `AnimeNews` |
| `get_anime_forum(anime_id)` | `GET /anime/{id}/forum` | `filter`, `page`, `order_by`, `sort` | `AnimeForum` |
| `get_anime_recommendations(anime_id)` | `GET /anime/{id}/recommendations` | `sfw`, `sfw_strict` | `AnimeRecommendations` |
| `get_anime_articles(anime_id)` | `GET /anime/{id}/articles` | `page`, `order_by`, `sort` | `AnimeArticles` |
| `get_anime_videos(anime_id)` | `GET /anime/{id}/videos` | — | `AnimeVideos` |
| `get_anime_episode_videos(anime_id)` | `GET /anime/{id}/videos/episodes` | `page` | `AnimeEpisodeVideos` |
| `get_anime_pictures(anime_id)` | `GET /anime/{id}/pictures` | — | `AnimePictures` |
| `get_anime_statistics(anime_id)` | `GET /anime/{id}/statistics` | — | `AnimeStatistics` |
| `get_anime_moreinfo(anime_id)` | `GET /anime/{id}/moreinfo` | — | `AnimeMoreInfo` |
| `get_anime_relations(anime_id)` | `GET /anime/{id}/relations` | `sfw`, `sfw_strict` | `AnimeRelations` |
| `get_anime_themes(anime_id)` | `GET /anime/{id}/themes` | — | `AnimeThemes` |
| `get_anime_external(anime_id)` | `GET /anime/{id}/external` | — | `AnimeExternal` |
| `get_anime_streaming(anime_id)` | `GET /anime/{id}/streaming` | — | `AnimeStreaming` |
| `get_anime_reviews(anime_id)` | `GET /anime/{id}/reviews` | `page`, `sort`, `preliminary`, `spoilers`, `sentiment` | `AnimeReviews` |
| `get_anime_stacks(anime_id)` | `GET /anime/{id}/stacks` | `q`, `page`, `limit`, `order_by`, `sort`, `spoilers`, `challenges`, `official`, `sfw`, `sfw_strict` | `AnimeStacks` |
| `search_anime(search_type, query)` | `GET /anime` | `page`, `limit`, `status`, `score`, `min_score`, `max_score`, `rating`, `genres`, `genres_exclude`, `order_by`, `sort`, `letter`, `producers`, `start_date`, `end_date`, `sfw`, `sfw_strict` | `AnimeSearch` |
| `get_anime_deleted()` | `GET /anime/deleted` | `q`, `page`, `limit`, `order_by`, `sort` | `AnimeCatalog` |
| `get_anime_unapproved()` | `GET /anime/unapproved` | `q`, `page`, `limit`, `order_by`, `sort` | `AnimeCatalog` |
| `get_anime_denied()` | `GET /anime/denied` | `q`, `page`, `limit`, `order_by`, `sort` | `AnimeCatalog` |
| `get_anime_ids()` | `GET /anime/ids` | `type`, `status`, `rating`, `sfw`, `sfw_strict`, `include`, `updated_at` | `AnimeIds` |

## Manga

Manga lookup, sub-resources, search and the catalog listings.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_manga(manga_id)` | `GET /manga/{id}` | — | `Manga` |
| `get_manga_full(manga_id)` | `GET /manga/{id}/full` | `sfw`, `sfw_strict` | `Manga` |
| `get_manga_characters(manga_id)` | `GET /manga/{id}/characters` | — | `MangaCharacters` |
| `get_manga_news(manga_id)` | `GET /manga/{id}/news` | `page`, `sfw`, `sfw_strict` | `MangaNews` |
| `get_manga_articles(manga_id)` | `GET /manga/{id}/articles` | `page`, `order_by`, `sort` | `MangaArticles` |
| `get_manga_pictures(manga_id)` | `GET /manga/{id}/pictures` | — | `MangaPictures` |
| `get_manga_statistics(manga_id)` | `GET /manga/{id}/statistics` | — | `MangaStatistics` |
| `get_manga_moreinfo(manga_id)` | `GET /manga/{id}/moreinfo` | — | `MangaMoreInfo` |
| `get_manga_relations(manga_id)` | `GET /manga/{id}/relations` | `sfw`, `sfw_strict` | `MangaRelations` |
| `get_manga_recommendations(manga_id)` | `GET /manga/{id}/recommendations` | `sfw`, `sfw_strict` | `MangaRecommendations` |
| `get_manga_external(manga_id)` | `GET /manga/{id}/external` | — | `MangaExternal` |
| `get_manga_reviews(manga_id)` | `GET /manga/{id}/reviews` | `page`, `sort`, `preliminary`, `spoilers`, `sentiment` | `MangaReviews` |
| `get_manga_stacks(manga_id)` | `GET /manga/{id}/stacks` | `q`, `page`, `limit`, `order_by`, `sort`, `spoilers`, `challenges`, `official`, `sfw`, `sfw_strict` | `MangaStacks` |
| `search_manga()` | `GET /manga` | `query`, `page`, `limit`, `manga_type`, `status`, `sfw`, `sfw_strict`, `score`, `min_score`, `max_score`, `unapproved`, `genres`, `genres_exclude`, `order_by`, `sort`, `letter`, `magazines`, `start_date`, `end_date` | `MangaSearch` |
| `get_manga_deleted()` | `GET /manga/deleted` | `q`, `page`, `limit`, `order_by`, `sort` | `MangaCatalog` |
| `get_manga_unapproved()` | `GET /manga/unapproved` | `q`, `page`, `limit`, `order_by`, `sort` | `MangaCatalog` |
| `get_manga_denied()` | `GET /manga/denied` | `q`, `page`, `limit`, `order_by`, `sort` | `MangaCatalog` |
| `get_manga_ids()` | `GET /manga/ids` | `type`, `status`, `sfw`, `sfw_strict`, `include`, `updated_at` | `MangaIds` |

## Characters

Character search, details, appearances and voice actors.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_characters()` | `GET /characters` | `q`, `page`, `limit`, `order_by`, `sort`, `letter` | `CharacterList` |
| `get_character(character_id)` | `GET /characters/{id}` | — | `Character` |
| `get_character_full(character_id)` | `GET /characters/{id}/full` | — | `Character` |
| `get_character_anime(character_id)` | `GET /characters/{id}/anime` | `sfw`, `sfw_strict` | `CharacterAnimeList` |
| `get_character_manga(character_id)` | `GET /characters/{id}/manga` | `sfw`, `sfw_strict` | `CharacterMangaList` |
| `get_character_voices(character_id)` | `GET /characters/{id}/voices` | — | `VoiceActorList` |
| `get_character_pictures(character_id)` | `GET /characters/{id}/pictures` | — | `AnimePictures` |
| `get_character_articles(character_id)` | `GET /characters/{id}/articles` | `page`, `order_by`, `sort` | `AnimeArticles` |
| `get_character_ids()` | `GET /characters/ids` | — | `CharacterIds` |

## People

Voice actors and staff.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_people()` | `GET /people` | `q`, `page`, `limit`, `order_by`, `sort`, `letter` | `PersonList` |
| `get_person(person_id)` | `GET /people/{id}` | — | `Person` |
| `get_person_full(person_id)` | `GET /people/{id}/full` | — | `Person` |
| `get_person_anime(person_id)` | `GET /people/{id}/anime` | `sfw`, `sfw_strict` | `PersonAnimeList` |
| `get_person_manga(person_id)` | `GET /people/{id}/manga` | `sfw`, `sfw_strict` | `PersonMangaList` |
| `get_person_voices(person_id)` | `GET /people/{id}/voices` | `sfw`, `sfw_strict` | `VoiceActorList` |
| `get_person_pictures(person_id)` | `GET /people/{id}/pictures` | — | `AnimePictures` |
| `get_person_articles(person_id)` | `GET /people/{id}/articles` | `page`, `order_by`, `sort` | `AnimeArticles` |
| `get_person_ids()` | `GET /people/ids` | — | `PersonIds` |

## Producers

Studios and licensing companies.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_producers()` | `GET /producers` | `q`, `page`, `limit`, `order_by`, `sort`, `letter` | `ProducerList` |
| `get_producer(producer_id)` | `GET /producers/{id}` | — | `Producer` |
| `get_producer_full(producer_id)` | `GET /producers/{id}/full` | — | `Producer` |
| `get_producer_external(producer_id)` | `GET /producers/{id}/external` | — | `AnimeExternal` |
| `get_producer_ids()` | `GET /producers/ids` | — | `ProducerIds` |

## Genres & magazines

Static catalogs used to filter searches.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_genres_anime()` | `GET /genres/anime` | `filter` | `GenreList` |
| `get_genres_manga()` | `GET /genres/manga` | `filter` | `GenreList` |
| `get_magazines()` | `GET /magazines` | `q`, `page`, `limit`, `order_by`, `sort`, `letter` | `MagazineList` |

## Seasons & schedules

Seasonal line-ups and weekly broadcast schedules.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_seasons()` | `GET /seasons` | — | `SeasonCalendar` |
| `get_season(year, season)` | `GET /seasons/{year}/{season}` | `filter`, `rating`, `sfw`, `sfw_strict`, `unapproved`, `continuing`, `kids`, `order_by`, `sort`, `page`, `limit` | `SeasonList` |
| `get_seasons_now()` | `GET /seasons/now` | `filter`, `rating`, `sfw`, `sfw_strict`, `unapproved`, `continuing`, `kids`, `order_by`, `sort`, `page`, `limit` | `SeasonList` |
| `get_seasons_previous()` | `GET /seasons/previous` | `filter`, `rating`, `sfw`, `sfw_strict`, `unapproved`, `continuing`, `kids`, `order_by`, `sort`, `page`, `limit` | `SeasonList` |
| `get_seasons_upcoming()` | `GET /seasons/upcoming` | `filter`, `rating`, `sfw`, `sfw_strict`, `unapproved`, `continuing`, `kids`, `order_by`, `sort`, `page`, `limit` | `SeasonList` |
| `get_schedules()` | `GET /schedules` | `filter`, `kids`, `sfw`, `sfw_strict`, `unapproved`, `page`, `limit` | `ScheduleList` |

## Top lists

Editorial and community rankings.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_top_anime()` | `GET /top/anime` | `page`, `limit`, `type`, `filter`, `rating`, `sfw`, `sfw_strict` | `AnimeSearch` |
| `get_top_manga()` | `GET /top/manga` | `page`, `limit`, `type`, `filter`, `sfw`, `sfw_strict` | `MangaSearch` |
| `get_top_characters()` | `GET /top/characters` | `page`, `limit` | `CharacterList` |
| `get_top_people()` | `GET /top/people` | `page`, `limit` | `PersonList` |
| `get_top_reviews()` | `GET /top/reviews` | `page`, `limit`, `type`, `preliminary`, `spoilers`, `sfw`, `sfw_strict` | `AnimeReviews` |

## Recommendations

Site-wide recommendation feeds.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_recommendations_anime()` | `GET /recommendations/anime` | `page`, `limit`, `sfw`, `sfw_strict` | `AnimeRecommendations` |
| `get_recommendations_manga()` | `GET /recommendations/manga` | `page`, `limit`, `sfw`, `sfw_strict` | `MangaRecommendations` |

## Random

Random entries, useful for discovery features.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_random_anime()` | `GET /random/anime` | `sfw`, `sfw_strict` | `Anime` |
| `get_random_manga()` | `GET /random/manga` | `sfw`, `sfw_strict` | `Manga` |
| `get_random_character()` | `GET /random/characters` | — | `Character` |
| `get_random_person()` | `GET /random/people` | — | `Person` |

## Reviews

Site-wide review feeds.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_reviews_anime()` | `GET /reviews/anime` | `page`, `limit`, `sort`, `preliminary`, `spoilers`, `sentiment`, `sfw`, `sfw_strict` | `AnimeReviews` |
| `get_reviews_manga()` | `GET /reviews/manga` | `page`, `limit`, `sort`, `preliminary`, `spoilers`, `sentiment`, `sfw`, `sfw_strict` | `MangaReviews` |

## Stacks

User-curated stacks.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_stacks()` | `GET /stacks` | `q`, `page`, `limit`, `order_by`, `sort`, `spoilers`, `challenges`, `official`, `stack_type`, `sfw`, `sfw_strict` | `StackList` |
| `get_stack(stack_id)` | `GET /stacks/{id}` | `sfw`, `sfw_strict` | `StackDetail` |

## Articles

Editorial articles.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_articles()` | `GET /articles` | `q`, `tag`, `page`, `limit`, `order_by`, `sort` | `ArticleList` |
| `get_article(article_id)` | `GET /articles/{id}` | — | `Article` |
| `get_article_tags()` | `GET /articles/tags` | — | `ArticleTags` |

## News

News posts.

| Method | Endpoint | Parameters | Returns |
| --- | --- | --- | --- |
| `get_news()` | `GET /news` | `q`, `tag`, `page`, `limit` | `NewsList` |
| `get_news_detail(news_id)` | `GET /news/{id}` | — | `News` |
| `get_news_tags()` | `GET /news/tags` | — | `NewsTags` |

