# jikan4
 A Python wrapper for the [Jikan API V4](https://docs.api.jikan.moe)


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

search = jikan.search_anime("anime", "naruto")
```

### Async Usage
```python
import asyncio
from jikan4.aiojikan import AioJikan


async def main():
    jikan = AioJikan()

    resp = await jikan.get_anime(1)

    search = await jikan.search_anime('anime', 'naruto')
    jikan.close()


if __name__ == '__main__':
    asyncio.run(main())
```
