# jikan4

A synchronous and asynchronous Python client for the **Tenrai v1** anime API.
Tenrai serves the Jikan v4 response schema, so one client covers anime, manga,
characters, people, producers, seasons, schedules, top lists, reviews, stacks,
articles and news.

- **Two clients, one API** — `Jikan` (blocking, on top of `requests`) and
  `AioJikan` (async, on top of `aiohttp`), with identical method signatures.
- **Typed responses** — every method returns a Pydantic model rather than a raw
  `dict`.
- **Rate limiting built in** — requests are spaced out to stay inside a
  configurable calls-per-minute budget.
- **Pluggable backend** — point `base_url` at any Jikan-v4-compatible host.

## Requirements

Python 3.10 or newer. `requests`, `aiohttp` and `pydantic` are installed
automatically with the package.

## Installation

```bash
pip install jikan4
```

## Quick start

Synchronous:

```python
from jikan4 import Jikan

jikan = Jikan()

anime = jikan.get_anime(1)
print(anime.title)     # Cowboy Bebop
print(anime.episodes)  # 26

results = jikan.search_anime("tv", "naruto", limit=3, order_by="score", sort="desc")
for entry in results.data:
    print(entry.title, entry.score)

print(results.pagination.has_next_page)
```

Asynchronous:

```python
import asyncio

from jikan4 import AioJikan


async def main() -> None:
    async with AioJikan() as jikan:
        anime = await jikan.get_anime(1)
        print(anime.title)

        results = await jikan.search_anime("tv", "naruto", limit=3)
        for entry in results.data:
            print(entry.title, entry.score)


if __name__ == "__main__":
    asyncio.run(main())
```

`AioJikan` opens its `aiohttp` session on the first request. Use it as a
context manager, or call `await jikan.close()`, to release the connection pool.

## Configuration

Both clients accept the same two arguments:

```python
from jikan4 import Jikan

Jikan()                             # https://api.tenrai.org/v1, 60 rpm
Jikan(rate_limit=30)                # default backend, 30 rpm
Jikan(rate_limit=0)                 # default backend, no throttling
Jikan("https://example.test/v1")    # another backend, 60 rpm
```

| Argument     | Default                     | Description                                  |
| ------------ | --------------------------- | -------------------------------------------- |
| `base_url`   | `https://api.tenrai.org/v1` | API root; a trailing slash is stripped       |
| `rate_limit` | `60`                        | Requests allowed per minute; `0` disables it |

The limiter spreads calls across the minute instead of firing a burst, so the
default of `60` works out to roughly one request per second. The budget belongs
to the client instance, so create one client and reuse it instead of one per
call.

## Passing parameters

Arguments in parentheses are required and positional; everything else is an
optional keyword argument:

- `None` values are dropped, so unused filters never reach the API.
- Falsy values are still sent, which matters for flags such as `sfw=False` and
  for paging such as `page=0`.
- `sfw_strict` is sent as `sfw-strict`, because Python identifiers cannot
  contain a hyphen.

```python
from jikan4 import Jikan

jikan = Jikan()

jikan.get_anime_full(1, sfw=True, sfw_strict=True)

jikan.search_anime(
    "tv",
    "naruto",
    status="finished",
    min_score=8,
    genres="1,2",
    order_by="score",
    sort="desc",
)
```

## Response models

Responses are parsed into the Pydantic models in
[jikan4/models.py][models]:

- Single-resource methods (`get_anime`, `get_character`, `get_stack`, …) return
  the resource model directly, such as `Anime` or `Character`.
- Search and listing methods return a model with `data` and `pagination`, such
  as `AnimeSearch`, `CharacterList` or `NewsList`.

```python
from jikan4 import Jikan
from jikan4.models import Anime, AnimeSearch

jikan = Jikan()

anime: Anime = jikan.get_anime(1)
print(anime.title, anime.score, anime.genres[0].name)
print(anime.model_dump())  # plain dict, ready to serialise

search: AnimeSearch = jikan.search_anime("tv", "naruto")
print(search.pagination.last_visible_page)
```

Fields the API omits are `None`, and list fields default to an empty list, so
check for `None` before using optional values.

## Error handling

Non-2xx responses raise the exception of the underlying HTTP library:

| Client     | Raises                          |
| ---------- | ------------------------------- |
| `Jikan`    | `requests.exceptions.HTTPError` |
| `AioJikan` | `aiohttp.ClientResponseError`   |

```python
import requests

from jikan4 import Jikan

jikan = Jikan()

try:
    jikan.get_anime(999_999_999)
except requests.HTTPError as error:
    print(error.response.status_code)  # 404
```

## Endpoints

The client wraps 97 Tenrai v1 endpoints, and each one is available on both
clients. [ENDPOINTS.md][endpoints] is the full reference: one row per method
with its HTTP endpoint, query parameters and return model.

| Area                                  | Methods | Highlights                                                                |
| ------------------------------------- | ------- | ------------------------------------------------------------------------- |
| [Anime][ep-anime]                     | 26      | `get_anime`, `get_anime_full`, `search_anime`, episodes, staff, streaming |
| [Manga][ep-manga]                     | 18      | `get_manga`, `get_manga_full`, `search_manga`, characters, statistics     |
| [Characters][ep-characters]           | 9       | `get_character`, `get_characters`, appearances, voice actors              |
| [People][ep-people]                   | 9       | `get_person`, `get_people`, credits, voice roles                          |
| [Producers][ep-producers]             | 5       | `get_producer`, `get_producers`, external links                           |
| [Genres & magazines][ep-genres]       | 3       | `get_genres_anime`, `get_genres_manga`, `get_magazines`                   |
| [Seasons & schedules][ep-seasons]     | 6       | `get_season`, `get_seasons_now`, `get_schedules`                          |
| [Top lists][ep-top]                   | 5       | `get_top_anime`, `get_top_manga`, `get_top_characters`                    |
| [Recommendations][ep-recommendations] | 2       | `get_recommendations_anime`, `get_recommendations_manga`                  |
| [Random][ep-random]                   | 4       | `get_random_anime`, `get_random_character`                                |
| [Reviews][ep-reviews]                 | 2       | `get_reviews_anime`, `get_reviews_manga`                                  |
| [Stacks][ep-stacks]                   | 2       | `get_stacks`, `get_stack`                                                 |
| [Articles][ep-articles]               | 3       | `get_articles`, `get_article`, `get_article_tags`                         |
| [News][ep-news]                       | 3       | `get_news`, `get_news_detail`, `get_news_tags`                            |

### Endpoints that need a server key

Tenrai protects the `…/ids` endpoint family with a server key that the client
does not send, so these five methods return `401 Unauthorized` against the
default backend: `get_anime_ids`, `get_manga_ids`, `get_character_ids`,
`get_person_ids` and `get_producer_ids`.

## Development

```bash
git clone https://github.com/mdabessa/jikan4.git
cd jikan4
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
pip install pytest pytest-asyncio
pytest tests
```

Or run the suite through the Hatch environment defined in
[pyproject.toml][pyproject]:

```bash
hatch run test
```

The tests hit the live Tenrai API, so they need network access and take about a
second per request because of the default rate limit.

## License

Released under the [MIT License][license]. This is an unofficial wrapper and is
not affiliated with MyAnimeList or Tenrai.

[models]: https://github.com/mdabessa/jikan4/blob/main/jikan4/models.py
[endpoints]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md
[pyproject]: https://github.com/mdabessa/jikan4/blob/main/pyproject.toml
[license]: https://github.com/mdabessa/jikan4/blob/main/LICENSE
[ep-anime]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#anime
[ep-manga]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#manga
[ep-characters]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#characters
[ep-people]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#people
[ep-producers]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#producers
[ep-genres]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#genres--magazines
[ep-seasons]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#seasons--schedules
[ep-top]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#top-lists
[ep-recommendations]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#recommendations
[ep-random]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#random
[ep-reviews]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#reviews
[ep-stacks]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#stacks
[ep-articles]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#articles
[ep-news]: https://github.com/mdabessa/jikan4/blob/main/ENDPOINTS.md#news
