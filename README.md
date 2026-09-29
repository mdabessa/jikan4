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
