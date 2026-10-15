# jikan4
 A Python wrapper for an anime API, with Tenrai as the default backend.


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


## Installation
```bash
pip install jikan4
```

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
    jikan = AioJikan()

    anime = await jikan.get_anime(1)
    search = await jikan.search_anime('tv', 'naruto')

    jikan.close()


if __name__ == '__main__':
    asyncio.run(main())
```
