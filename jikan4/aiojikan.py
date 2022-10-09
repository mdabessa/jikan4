from __future__ import annotations

import aiohttp
from ratelimiter import RateLimiter
from .models import Anime, AnimeSearch


class AioJikan:
    """Async Jikan API Wrapper"""

    def __init__(
        self, base_url: str = "https://api.jikan.moe/v4", rate_limit: int = 60
    ) -> None:
        """Construct a AioJikan object

        Args:
            base_url (str, optional): Base URL for Jikan API. Defaults to "https://api.jikan.moe/v4".
            rate_limit (int, optional): Rate limit in requests per minute. Defaults to 60.

        Returns:
            AioJikan: AioJikan object

        Examples:
            >>> aiojikan = AioJikan()
            >>> aiojikan = AioJikan("https://api.jikan.moe/v4")
        """

        base_url = base_url.rstrip("/")
        self.base_url = base_url
        self.session = aiohttp.ClientSession()
        self.rate_limiter = RateLimiter(
            max_calls=rate_limit / 60, period=1
        )  # Spread out requests over 60 seconds

    async def close(self) -> None:
        """Close the aiohttp session"""

        await self.session.close()

    async def __aenter__(self) -> AioJikan:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    async def _get(self, endpoint: str, params: dict = None) -> dict:
        """Make a GET request to the Jikan API

        Args:
            endpoint (str): Endpoint to request
            params (dict, optional): Parameters to send with request. Defaults to None.

        Returns:
            dict: JSON response from Jikan API
        """

        url = f"{self.base_url}/{endpoint}"

        async with self.rate_limiter:
            async with self.session.get(url, params=params) as r:
                r.raise_for_status()
                response = await r.json()

        return response

    async def get_anime(self, anime_id: int) -> Anime:
        """Get anime information

        Args:
            anime_id (int): Anime ID

        Returns:
            Anime: Anime object

        Examples:
            >>> aiojikan = AioJikan()
            >>> anime = aiojikan.get_anime(1)
        """

        endpoint = f"anime/{anime_id}"
        response = await self._get(endpoint)

        return Anime(**response["data"])

    async def search_anime(
        self, search_type: str, query: str, page: int = 1
    ) -> AnimeSearch:
        """Search for anime

        Args:
            search_type (str): Type of search to perform (tv, movie, ova, special, ona, music)
            query (str): Query to search for
            page (int, optional): Page number. Defaults to 1.

        Returns:
            AnimeSearch: AnimeSearch object

        Examples:
            >>> aiojikan = AioJikan()
            >>> result = aiojikan.search_anime("tv", "naruto")
        """

        endpoint = f"anime"
        params = {"q": query, "page": page, "type": search_type}
        response = await self._get(endpoint, params)

        return AnimeSearch(**response)
