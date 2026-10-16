# jikan4

A synchronous and asynchronous Python wrapper for the Tenrai v1 API. Tenrai
follows the Jikan v4 response schema, so the same client covers anime, manga,
catalog resources, discovery, articles, news, and stacks.


## Tenrai Endpoint Support

The client currently uses these Tenrai v1 endpoints:

| Client method | Endpoint | Status |
| --- | --- | --- |
| `get_anime` | `GET /anime/{id}` | Supported |
| `get_anime_full` | `GET /anime/{id}/full` | Supported |
| `get_anime_characters` | `GET /anime/{id}/characters` | Supported |
| `get_anime_staff` | `GET /anime/{id}/staff` | Supported |
| `get_anime_episodes` | `GET /anime/{id}/episodes` | Supported |
| `get_anime_episode` | `GET /anime/{id}/episodes/{episode}` | Supported |
| `get_anime_news` | `GET /anime/{id}/news` | Supported |
| `search_anime` | `GET /anime` | Supported |
| `get_anime_forum` | `GET /anime/{id}/forum` | Supported |
| `get_anime_recommendations` | `GET /anime/{id}/recommendations` | Supported |
| `get_anime_articles` | `GET /anime/{id}/articles` | Supported |
| `get_anime_videos` | `GET /anime/{id}/videos` | Supported |
| `get_anime_episode_videos` | `GET /anime/{id}/videos/episodes` | Supported |
| `get_anime_pictures` | `GET /anime/{id}/pictures` | Supported |
| `get_anime_statistics` | `GET /anime/{id}/statistics` | Supported |
| `get_anime_moreinfo` | `GET /anime/{id}/moreinfo` | Supported |
| `get_anime_relations` | `GET /anime/{id}/relations` | Supported |
| `get_anime_themes` | `GET /anime/{id}/themes` | Supported |
| `get_anime_external` | `GET /anime/{id}/external` | Supported |
| `get_anime_streaming` | `GET /anime/{id}/streaming` | Supported |
| `get_anime_reviews` | `GET /anime/{id}/reviews` | Supported |
| `get_anime_stacks` | `GET /anime/{id}/stacks` | Supported |
| `get_anime_deleted` | `GET /anime/deleted` | Supported |
| `get_anime_unapproved` | `GET /anime/unapproved` | Supported |
| `get_anime_denied` | `GET /anime/denied` | Supported |
| `get_anime_ids` | `GET /anime/ids` | Supported |
| `search_manga` | `GET /manga` | Supported |
| `get_manga` | `GET /manga/{id}` | Supported |
| `get_manga_full` | `GET /manga/{id}/full` | Supported |
| `get_manga_recommendations` | `GET /manga/{id}/recommendations` | Supported |
| `get_manga_characters` | `GET /manga/{id}/characters` | Supported |
| `get_manga_news` | `GET /manga/{id}/news` | Supported |
| `get_manga_articles` | `GET /manga/{id}/articles` | Supported |
| `get_manga_pictures` | `GET /manga/{id}/pictures` | Supported |
| `get_manga_statistics` | `GET /manga/{id}/statistics` | Supported |
| `get_manga_moreinfo` | `GET /manga/{id}/moreinfo` | Supported |
| `get_manga_relations` | `GET /manga/{id}/relations` | Supported |
| `get_manga_external` | `GET /manga/{id}/external` | Supported |
| `get_manga_reviews` | `GET /manga/{id}/reviews` | Supported |
| `get_manga_stacks` | `GET /manga/{id}/stacks` | Supported |
| `get_manga_deleted` | `GET /manga/deleted` | Supported |
| `get_manga_unapproved` | `GET /manga/unapproved` | Supported |
| `get_manga_denied` | `GET /manga/denied` | Supported |
| `get_manga_ids` | `GET /manga/ids` | Supported |
| `get_characters` | `GET /characters` | Supported |
| `get_character` | `GET /characters/{id}` | Supported |
| `get_character_full` | `GET /characters/{id}/full` | Supported |
| `get_character_anime` | `GET /characters/{id}/anime` | Supported |
| `get_character_manga` | `GET /characters/{id}/manga` | Supported |
| `get_character_articles` | `GET /characters/{id}/articles` | Supported |
| `get_character_pictures` | `GET /characters/{id}/pictures` | Supported |
| `get_character_voices` | `GET /characters/{id}/voices` | Supported |
| `get_character_ids` | `GET /characters/ids` | Supported |
| `get_people` | `GET /people` | Supported |
| `get_person` | `GET /people/{id}` | Supported |
| `get_person_full` | `GET /people/{id}/full` | Supported |
| `get_person_anime` | `GET /people/{id}/anime` | Supported |
| `get_person_manga` | `GET /people/{id}/manga` | Supported |
| `get_person_articles` | `GET /people/{id}/articles` | Supported |
| `get_person_pictures` | `GET /people/{id}/pictures` | Supported |
| `get_person_voices` | `GET /people/{id}/voices` | Supported |
| `get_person_ids` | `GET /people/ids` | Supported |
| `get_producers` | `GET /producers` | Supported |
| `get_producer` | `GET /producers/{id}` | Supported |
| `get_producer_full` | `GET /producers/{id}/full` | Supported |
| `get_producer_external` | `GET /producers/{id}/external` | Supported |
| `get_producer_ids` | `GET /producers/ids` | Supported |
| `get_genres_anime` | `GET /genres/anime` | Supported |
| `get_genres_manga` | `GET /genres/manga` | Supported |
| `get_magazines` | `GET /magazines` | Supported |
| `get_random_anime` | `GET /random/anime` | Supported |
| `get_random_manga` | `GET /random/manga` | Supported |
| `get_random_character` | `GET /random/characters` | Supported |
| `get_random_person` | `GET /random/people` | Supported |
| `get_recommendations_anime` | `GET /recommendations/anime` | Supported |
| `get_recommendations_manga` | `GET /recommendations/manga` | Supported |
| `get_top_anime` | `GET /top/anime` | Supported |
| `get_top_manga` | `GET /top/manga` | Supported |
| `get_top_characters` | `GET /top/characters` | Supported |
| `get_top_people` | `GET /top/people` | Supported |
| `get_top_reviews` | `GET /top/reviews` | Supported |
| `get_seasons` | `GET /seasons` | Supported |
| `get_season` | `GET /seasons/{year}/{season}` | Supported |
| `get_seasons_now` | `GET /seasons/now` | Supported |
| `get_seasons_previous` | `GET /seasons/previous` | Supported |
| `get_seasons_upcoming` | `GET /seasons/upcoming` | Supported |
| `get_schedules` | `GET /schedules` | Supported |
| `get_reviews_anime` | `GET /reviews/anime` | Supported |
| `get_reviews_manga` | `GET /reviews/manga` | Supported |
| `get_stacks` | `GET /stacks` | Supported |
| `get_stack` | `GET /stacks/{id}` | Supported |
| `get_articles` | `GET /articles` | Supported |
| `get_article_tags` | `GET /articles/tags` | Supported |
| `get_article` | `GET /articles/{id}` | Supported |
| `get_news` | `GET /news` | Supported |
| `get_news_tags` | `GET /news/tags` | Supported |
| `get_news_detail` | `GET /news/{id}` | Supported |


## Installation
```bash
pip install jikan4
```

## Client Configuration

Both clients accept a `base_url` and a per-minute `rate_limit`. The default
backend is `https://api.tenrai.org/v1`.

```python
from jikan4 import Jikan

jikan = Jikan(rate_limit=60)
custom = Jikan("https://api.example.test/v1", rate_limit=30)
```

Every optional endpoint argument is omitted when it is `None`; valid falsy
values such as `False` and `0` are still sent. The Python argument
`sfw_strict` is translated to the API parameter `sfw-strict`.

## Usage

### Basic Usage
```python
from jikan4.jikan import Jikan

jikan = Jikan()

anime = jikan.get_anime(1)
search = jikan.search_anime("tv", "naruto")
```

### Async Usage
```python
import asyncio
from jikan4.aiojikan import AioJikan


async def main():
    async with AioJikan() as jikan:
        anime = await jikan.get_anime(1)
        search = await jikan.search_anime("tv", "naruto")


if __name__ == '__main__':
    asyncio.run(main())
```
