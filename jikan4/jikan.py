import requests

from .models import (
    Anime,
    AnimeSearch,
    AnimeCharacters,
    AnimeStaff,
    AnimeEpisodes,
    Episode,
    AnimeNews,
    AnimeForum,
)
from .base import BaseClient
from .utils.limiter import Limiter
from .utils.params import exclude_none


class Jikan(BaseClient):
    """Anime API wrapper with Tenrai as the default backend."""

    def __init__(
        self, base_url: str = "https://api.tenrai.org/v1", rate_limit: int = 60
    ):
        """Construct a Jikan object

        Args:
            base_url (str, optional): Base URL for the anime API. Defaults to "https://api.tenrai.org/v1".
            rate_limit (int, optional): Rate limit in requests per minute. Defaults to 60.

        Returns:
            Jikan: Jikan object

        Examples:
            >>> jikan = Jikan()
            >>> jikan = Jikan("https://api.tenrai.org/v1")
        """

        self.session = requests.Session()
        super().__init__(base_url, rate_limit)

    def _setup_limiter(self, rate_limit: int) -> None:
        self.rate_limiter = Limiter(calls_limit=rate_limit, period=60, spread=True)
        self._get = self.rate_limiter.__call__(self._get)

    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        """Make a GET request to the configured anime API

        Args:
            endpoint (str): Endpoint to request
            params (dict, optional): Parameters to send with request. Defaults to None.

        Returns:
            dict: JSON response from the configured anime API
        """

        url = f"{self.base_url}/{endpoint}"

        response = self.session.get(url, params=params)

        response.raise_for_status()
        return response.json()

    def get_anime(self, anime_id: int) -> Anime:
        """Get anime information

        Args:
            anime_id (int): Anime ID

        Returns:
            Anime: Anime object

        Examples:
            >>> jikan = Jikan()
            >>> anime = jikan.get_anime(1)
        """

        endpoint = f"anime/{anime_id}"
        response = self._get(endpoint)
        return Anime(**response["data"])

    def get_anime_full(
        self,
        anime_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> Anime:
        """Get anime information with full details

        Args:
            anime_id (int): Anime ID
            sfw (bool, optional): Restrict the response to safe-for-work content.
            sfw_strict (bool, optional): Apply strict safe-for-work filtering.

        Returns:
            Anime: Anime object

        Examples:
            >>> jikan = Jikan()
            >>> anime = jikan.get_anime_full(1)
        """

        endpoint = f"anime/{anime_id}/full"
        params = {
            "sfw": sfw,
            "sfw-strict": sfw_strict,
        }
        params = exclude_none(params)
        response = self._get(endpoint, params)
        return Anime(**response["data"])

    def get_anime_characters(self, anime_id: int) -> AnimeCharacters:
        """Get anime characters

        Args:
            anime_id (int): Anime ID

        Returns:
            AnimeCharacters: AnimeCharacters object

        Examples:
            >>> jikan = Jikan()
            >>> characters = jikan.get_anime_characters(1)
        """

        endpoint = f"anime/{anime_id}/characters"
        response = self._get(endpoint)
        return AnimeCharacters(**response)

    def get_anime_staff(self, anime_id: int) -> AnimeStaff:
        """Get anime staff

        Args:
            anime_id (int): Anime ID

        Returns:
            AnimeStaff: AnimeStaff object

        Examples:
            >>> jikan = Jikan()
            >>> staff = jikan.get_anime_staff(1)
        """

        endpoint = f"anime/{anime_id}/staff"
        response = self._get(endpoint)
        return AnimeStaff(**response)

    def get_anime_episodes(
        self, anime_id: int, page: int | None = None
    ) -> AnimeEpisodes:
        """Get anime episodes

        Args:
            anime_id (int): Anime ID
            page (int, optional): Page number.

        Returns:
            AnimeEpisodes: AnimeEpisodes object

        Examples:
            >>> jikan = Jikan()
            >>> episodes = jikan.get_anime_episodes(1)
        """

        endpoint = f"anime/{anime_id}/episodes"
        params = {"page": page}
        params = exclude_none(params)
        response = self._get(endpoint, params)
        return AnimeEpisodes(**response)

    def get_anime_episode(self, anime_id: int, episode: int) -> Episode:
        """Get anime episode

        Args:
            anime_id (int): Anime ID
            episode (int): Episode number

        Returns:
            Episode: Episode object

        Examples:
            >>> jikan = Jikan()
            >>> episode = jikan.get_anime_episode(1, 1)
        """

        endpoint = f"anime/{anime_id}/episodes/{episode}"
        response = self._get(endpoint)
        return Episode(**response["data"])

    def get_anime_news(
        self,
        anime_id: int,
        page: int | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> AnimeNews:
        """Get anime news

        Args:
            anime_id (int): Anime ID
            page (int, optional): Page number. Defaults to None.
            sfw (bool, optional): Restrict the response to safe-for-work content.
            sfw_strict (bool, optional): Apply strict safe-for-work filtering.

        Returns:
            AnimeNews: AnimeNews object

        Examples:
            >>> jikan = Jikan()
            >>> news = jikan.get_anime_news(1)
        """

        params = {
            "page": page,
            "sfw": sfw,
            "sfw-strict": sfw_strict,
        }
        params = exclude_none(params)

        endpoint = f"anime/{anime_id}/news"
        response = self._get(endpoint, params=params)

        return AnimeNews(**response)

    def search_anime(
        self,
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
    ) -> AnimeSearch:
        """Search for anime

        Args:
            search_type (str): Type of search to perform (tv, movie, ova, special, ona, music)
            query (str): Query to search for
            page (int, optional): Page number. Defaults to 1.
            limit (int, optional): Maximum number of results.
            status (str, optional): Airing status to filter by.
            score (float, optional): Exact score to filter by.
            min_score (float, optional): Minimum score to filter by.
            max_score (float, optional): Maximum score to filter by.
            rating (str, optional): Age rating to filter by.
            genres (str, optional): Genre IDs to include.
            genres_exclude (str, optional): Genre IDs to exclude.
            order_by (str, optional): Field to order results by.
            sort (str, optional): Sort direction.
            letter (str, optional): First letter of the title.
            producers (str, optional): Producer IDs to filter by.
            start_date (str, optional): Earliest release date.
            end_date (str, optional): Latest release date.
            sfw (bool, optional): Restrict results to safe-for-work titles.
            sfw_strict (bool, optional): Apply strict safe-for-work filtering.

        Returns:
            AnimeSearch: AnimeSearch object

        Examples:
            >>> jikan = Jikan()
            >>> result = jikan.search_anime("tv", "naruto")
        """

        endpoint = f"anime"
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
        params = exclude_none(params)
        response = self._get(endpoint, params)

        return AnimeSearch(**response)

    def get_anime_forum(
        self,
        anime_id: int,
        filter: str | None = None,
        page: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeForum:
        """Get anime forum

        Args:
            anime_id (int): Anime ID
            filter (str, optional): Filter to apply. Tenrai currently supports only "episode". Defaults to None.
            page (int, optional): Page number.
            order_by (str, optional): Field to order results by.
            sort (str, optional): Sort direction.

        Returns:
            AnimeForum: AnimeForum object

        Examples:
            >>> jikan = Jikan()
            >>> forum = jikan.get_anime_forum(1)
        """

        params = {
            "filter": filter,
            "page": page,
            "order_by": order_by,
            "sort": sort,
        }
        params = exclude_none(params)

        endpoint = f"anime/{anime_id}/forum"
        response = self._get(endpoint, params=params)

        return AnimeForum(**response)
