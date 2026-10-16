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
    AnimeRecommendations,
    AnimeArticles,
    AnimeVideos,
    AnimeEpisodeVideos,
    AnimePictures,
    AnimeStatistics,
    AnimeMoreInfo,
    AnimeRelations,
    AnimeThemes,
    AnimeExternal,
    AnimeStreaming,
    AnimeReviews,
    AnimeStacks,
    AnimeCatalog,
    AnimeIds,
    Manga,
    MangaSearch,
    MangaCharacters,
    MangaNews,
    MangaArticles,
    MangaPictures,
    MangaStatistics,
    MangaMoreInfo,
    MangaRelations,
    MangaExternal,
    MangaReviews,
    MangaStacks,
    MangaRecommendations,
    MangaCatalog,
    MangaIds,
    Character,
    CharacterList,
    CharacterAnimeList,
    CharacterMangaList,
    Person,
    PersonList,
    PersonAnimeList,
    PersonMangaList,
    Producer,
    ProducerList,
    GenreList,
    MagazineList,
    CharacterIds,
    PersonIds,
    ProducerIds,
    VoiceActorList,
    SeasonCalendar,
    SeasonList,
    ScheduleList,
    ArticleList,
    ArticleTags,
    NewsList,
    NewsTags,
    StackList,
    StackDetail,
    Article,
    News,
)
from .base import BaseClient
from . import routes
from .utils.limiter import Limiter


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

        endpoint, params = routes.get_anime(anime_id)
        response = self._get(endpoint, params)
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

        endpoint, params = routes.get_anime_full(anime_id, sfw, sfw_strict)
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

        endpoint, params = routes.get_anime_characters(anime_id)
        response = self._get(endpoint, params)
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

        endpoint, params = routes.get_anime_staff(anime_id)
        response = self._get(endpoint, params)
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

        endpoint, params = routes.get_anime_episodes(anime_id, page)
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

        endpoint, params = routes.get_anime_episode(anime_id, episode)
        response = self._get(endpoint, params)
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

        endpoint, params = routes.get_anime_news(anime_id, page, sfw, sfw_strict)
        response = self._get(endpoint, params)

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

        endpoint, params = routes.search_anime(
            search_type,
            query,
            page,
            limit,
            status,
            score,
            min_score,
            max_score,
            rating,
            genres,
            genres_exclude,
            order_by,
            sort,
            letter,
            producers,
            start_date,
            end_date,
            sfw,
            sfw_strict,
        )
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

        endpoint, params = routes.get_anime_forum(
            anime_id, filter, page, order_by, sort
        )
        response = self._get(endpoint, params)

        return AnimeForum(**response)

    def get_anime_recommendations(
        self, anime_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> AnimeRecommendations:
        """Get anime recommendations."""
        endpoint, params = routes.get_anime_recommendations(anime_id, sfw, sfw_strict)
        return AnimeRecommendations(**self._get(endpoint, params))

    def get_anime_articles(
        self,
        anime_id: int,
        page: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeArticles:
        """Get articles related to an anime."""
        endpoint, params = routes.get_anime_articles(anime_id, page, order_by, sort)
        return AnimeArticles(**self._get(endpoint, params))

    def get_anime_videos(self, anime_id: int) -> AnimeVideos:
        """Get anime promotional and music videos."""
        endpoint, params = routes.get_anime_videos(anime_id)
        return AnimeVideos(**self._get(endpoint, params))

    def get_anime_episode_videos(
        self, anime_id: int, page: int | None = None
    ) -> AnimeEpisodeVideos:
        """Get videos associated with anime episodes."""
        endpoint, params = routes.get_anime_episode_videos(anime_id, page)
        return AnimeEpisodeVideos(**self._get(endpoint, params))

    def get_anime_pictures(self, anime_id: int) -> AnimePictures:
        """Get anime pictures."""
        endpoint, params = routes.get_anime_pictures(anime_id)
        return AnimePictures(**self._get(endpoint, params))

    def get_anime_statistics(self, anime_id: int) -> AnimeStatistics:
        """Get anime watching statistics."""
        endpoint, params = routes.get_anime_statistics(anime_id)
        return AnimeStatistics(**self._get(endpoint, params))

    def get_anime_moreinfo(self, anime_id: int) -> AnimeMoreInfo:
        """Get additional anime information."""
        endpoint, params = routes.get_anime_moreinfo(anime_id)
        return AnimeMoreInfo(**self._get(endpoint, params))

    def get_anime_relations(
        self, anime_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> AnimeRelations:
        """Get anime relations."""
        endpoint, params = routes.get_anime_relations(anime_id, sfw, sfw_strict)
        return AnimeRelations(**self._get(endpoint, params))

    def get_anime_themes(self, anime_id: int) -> AnimeThemes:
        """Get anime opening and ending themes."""
        endpoint, params = routes.get_anime_themes(anime_id)
        return AnimeThemes(**self._get(endpoint, params))

    def get_anime_external(self, anime_id: int) -> AnimeExternal:
        """Get external links for an anime."""
        endpoint, params = routes.get_anime_external(anime_id)
        return AnimeExternal(**self._get(endpoint, params))

    def get_anime_streaming(self, anime_id: int) -> AnimeStreaming:
        """Get streaming links for an anime."""
        endpoint, params = routes.get_anime_streaming(anime_id)
        return AnimeStreaming(**self._get(endpoint, params))

    def get_anime_reviews(
        self,
        anime_id: int,
        page: int | None = None,
        sort: str | None = None,
        preliminary: bool | None = None,
        spoilers: bool | None = None,
        sentiment: str | None = None,
    ) -> AnimeReviews:
        """Get anime reviews."""
        endpoint, params = routes.get_anime_reviews(
            anime_id, page, sort, preliminary, spoilers, sentiment
        )
        return AnimeReviews(**self._get(endpoint, params))

    def get_anime_stacks(
        self,
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
    ) -> AnimeStacks:
        """Get user-created stacks containing an anime."""
        endpoint, params = routes.get_anime_stacks(
            anime_id,
            q,
            page,
            limit,
            order_by,
            sort,
            spoilers,
            challenges,
            official,
            sfw,
            sfw_strict,
        )
        return AnimeStacks(**self._get(endpoint, params))

    def get_anime_deleted(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeCatalog:
        """Get deleted anime entries."""
        endpoint, params = routes.get_anime_deleted(q=q, page=page, limit=limit, order_by=order_by, sort=sort)
        return AnimeCatalog(**self._get(endpoint, params))

    def get_anime_unapproved(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeCatalog:
        """Get unapproved anime entries."""
        endpoint, params = routes.get_anime_unapproved(q=q, page=page, limit=limit, order_by=order_by, sort=sort)
        return AnimeCatalog(**self._get(endpoint, params))

    def get_anime_denied(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeCatalog:
        """Get denied anime entries."""
        endpoint, params = routes.get_anime_denied(q=q, page=page, limit=limit, order_by=order_by, sort=sort)
        return AnimeCatalog(**self._get(endpoint, params))

    def get_anime_ids(
        self,
        type: str | None = None,
        status: str | None = None,
        rating: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
        include: str | None = None,
        updated_at: str | None = None,
    ) -> AnimeIds:
        """Get anime IDs updated since a specified timestamp."""
        endpoint, params = routes.get_anime_ids(
            type, status, rating, sfw, sfw_strict, include, updated_at
        )
        return AnimeIds(**self._get(endpoint, params))

    def search_manga(
        self,
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
    ) -> MangaSearch:
        """Search for manga."""
        endpoint, params = routes.search_manga(
            query,
            page,
            limit,
            manga_type,
            status,
            sfw,
            sfw_strict,
            score,
            min_score,
            max_score,
            unapproved,
            genres,
            genres_exclude,
            order_by,
            sort,
            letter,
            magazines,
            start_date,
            end_date,
        )
        return MangaSearch(**self._get(endpoint, params))

    def get_manga(self, manga_id: int) -> Manga:
        """Get manga information."""
        endpoint, params = routes.get_manga(manga_id)
        response = self._get(endpoint, params)
        return Manga(**response["data"])

    def get_manga_full(
        self,
        manga_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> Manga:
        """Get manga information with full details."""
        endpoint, params = routes.get_manga_full(manga_id, sfw, sfw_strict)
        response = self._get(endpoint, params)
        return Manga(**response["data"])

    def get_manga_recommendations(
        self, manga_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> MangaRecommendations:
        """Get manga recommendations."""
        endpoint, params = routes.get_manga_recommendations(manga_id, sfw, sfw_strict)
        return MangaRecommendations(**self._get(endpoint, params))

    def get_manga_characters(self, manga_id: int) -> MangaCharacters:
        """Get manga characters."""
        endpoint, params = routes.get_manga_characters(manga_id)
        return MangaCharacters(**self._get(endpoint, params))

    def get_manga_news(
        self,
        manga_id: int,
        page: int | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> MangaNews:
        """Get manga news."""
        endpoint, params = routes.get_manga_news(manga_id, page, sfw, sfw_strict)
        return MangaNews(**self._get(endpoint, params))

    def get_manga_articles(
        self,
        manga_id: int,
        page: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> MangaArticles:
        """Get articles related to manga."""
        endpoint, params = routes.get_manga_articles(manga_id, page, order_by, sort)
        return MangaArticles(**self._get(endpoint, params))

    def get_manga_pictures(self, manga_id: int) -> MangaPictures:
        """Get manga pictures."""
        endpoint, params = routes.get_manga_pictures(manga_id)
        return MangaPictures(**self._get(endpoint, params))

    def get_manga_statistics(self, manga_id: int) -> MangaStatistics:
        """Get manga statistics."""
        endpoint, params = routes.get_manga_statistics(manga_id)
        return MangaStatistics(**self._get(endpoint, params))

    def get_manga_moreinfo(self, manga_id: int) -> MangaMoreInfo:
        """Get additional manga information."""
        endpoint, params = routes.get_manga_moreinfo(manga_id)
        return MangaMoreInfo(**self._get(endpoint, params))

    def get_manga_relations(
        self, manga_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> MangaRelations:
        """Get manga relations."""
        endpoint, params = routes.get_manga_relations(manga_id, sfw, sfw_strict)
        return MangaRelations(**self._get(endpoint, params))

    def get_manga_external(self, manga_id: int) -> MangaExternal:
        """Get external links for manga."""
        endpoint, params = routes.get_manga_external(manga_id)
        return MangaExternal(**self._get(endpoint, params))

    def get_manga_reviews(
        self,
        manga_id: int,
        page: int | None = None,
        sort: str | None = None,
        preliminary: bool | None = None,
        spoilers: bool | None = None,
        sentiment: str | None = None,
    ) -> MangaReviews:
        """Get manga reviews."""
        endpoint, params = routes.get_manga_reviews(
            manga_id, page, sort, preliminary, spoilers, sentiment
        )
        return MangaReviews(**self._get(endpoint, params))

    def get_manga_stacks(
        self,
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
    ) -> MangaStacks:
        """Get user-created stacks containing manga."""
        endpoint, params = routes.get_manga_stacks(
            manga_id,
            q,
            page,
            limit,
            order_by,
            sort,
            spoilers,
            challenges,
            official,
            sfw,
            sfw_strict,
        )
        return MangaStacks(**self._get(endpoint, params))

    def get_manga_deleted(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> MangaCatalog:
        """Get deleted manga entries."""
        endpoint, params = routes.get_manga_deleted(q=q, page=page, limit=limit, order_by=order_by, sort=sort)
        return MangaCatalog(**self._get(endpoint, params))

    def get_manga_unapproved(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> MangaCatalog:
        """Get unapproved manga entries."""
        endpoint, params = routes.get_manga_unapproved(q=q, page=page, limit=limit, order_by=order_by, sort=sort)
        return MangaCatalog(**self._get(endpoint, params))

    def get_manga_denied(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> MangaCatalog:
        """Get denied manga entries."""
        endpoint, params = routes.get_manga_denied(q=q, page=page, limit=limit, order_by=order_by, sort=sort)
        return MangaCatalog(**self._get(endpoint, params))

    def get_manga_ids(
        self,
        type: str | None = None,
        status: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
        include: str | None = None,
        updated_at: str | None = None,
    ) -> MangaIds:
        """Get manga IDs updated since a specified timestamp."""
        endpoint, params = routes.get_manga_ids(
            type, status, sfw, sfw_strict, include, updated_at
        )
        return MangaIds(**self._get(endpoint, params))

    def get_characters(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        letter: str | None = None,
    ) -> CharacterList:
        """Search for characters."""
        endpoint, params = routes.get_characters(q, page, limit, order_by, sort, letter)
        return CharacterList(**self._get(endpoint, params))

    def get_character(self, character_id: int) -> Character:
        """Get character information."""
        endpoint, params = routes.get_character(character_id)
        return Character(**self._get(endpoint, params)["data"])

    def get_character_full(self, character_id: int) -> Character:
        """Get character information with full details."""
        endpoint, params = routes.get_character_full(character_id)
        return Character(**self._get(endpoint, params)["data"])

    def get_character_anime(
        self,
        character_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> CharacterAnimeList:
        """Get anime appearances for a character."""
        endpoint, params = routes.get_character_anime(character_id, sfw, sfw_strict)
        return CharacterAnimeList(**self._get(endpoint, params))

    def get_character_manga(
        self,
        character_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> CharacterMangaList:
        """Get manga appearances for a character."""
        endpoint, params = routes.get_character_manga(character_id, sfw, sfw_strict)
        return CharacterMangaList(**self._get(endpoint, params))

    def get_character_articles(
        self,
        character_id: int,
        page: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeArticles:
        """Get articles about a character."""
        endpoint, params = routes.get_character_articles(character_id, page, order_by, sort)
        return AnimeArticles(**self._get(endpoint, params))

    def get_character_pictures(self, character_id: int) -> AnimePictures:
        """Get character pictures."""
        endpoint, params = routes.get_character_pictures(character_id)
        return AnimePictures(**self._get(endpoint, params))

    def get_character_voices(self, character_id: int) -> VoiceActorList:
        """Get voice actors for a character."""
        endpoint, params = routes.get_character_voices(character_id)
        return VoiceActorList(**self._get(endpoint, params))

    def get_character_ids(self) -> CharacterIds:
        """Get character IDs."""
        endpoint, params = routes.get_character_ids()
        return CharacterIds(**self._get(endpoint, params))

    def get_people(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        letter: str | None = None,
    ) -> PersonList:
        """Search for people."""
        endpoint, params = routes.get_people(q, page, limit, order_by, sort, letter)
        return PersonList(**self._get(endpoint, params))

    def get_person(self, person_id: int) -> Person:
        """Get person information."""
        endpoint, params = routes.get_person(person_id)
        return Person(**self._get(endpoint, params)["data"])

    def get_person_full(self, person_id: int) -> Person:
        """Get person information with full details."""
        endpoint, params = routes.get_person_full(person_id)
        return Person(**self._get(endpoint, params)["data"])

    def get_person_anime(
        self,
        person_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> PersonAnimeList:
        """Get anime credits for a person."""
        endpoint, params = routes.get_person_anime(person_id, sfw, sfw_strict)
        return PersonAnimeList(**self._get(endpoint, params))

    def get_person_manga(
        self,
        person_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> PersonMangaList:
        """Get manga credits for a person."""
        endpoint, params = routes.get_person_manga(person_id, sfw, sfw_strict)
        return PersonMangaList(**self._get(endpoint, params))

    def get_person_articles(
        self,
        person_id: int,
        page: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> AnimeArticles:
        """Get articles about a person."""
        endpoint, params = routes.get_person_articles(person_id, page, order_by, sort)
        return AnimeArticles(**self._get(endpoint, params))

    def get_person_pictures(self, person_id: int) -> AnimePictures:
        """Get person pictures."""
        endpoint, params = routes.get_person_pictures(person_id)
        return AnimePictures(**self._get(endpoint, params))

    def get_person_voices(
        self,
        person_id: int,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> VoiceActorList:
        """Get voice acting roles for a person."""
        endpoint, params = routes.get_person_voices(person_id, sfw, sfw_strict)
        return VoiceActorList(**self._get(endpoint, params))

    def get_person_ids(self) -> PersonIds:
        """Get person IDs."""
        endpoint, params = routes.get_person_ids()
        return PersonIds(**self._get(endpoint, params))

    def get_producers(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        letter: str | None = None,
    ) -> ProducerList:
        """Search for producers."""
        endpoint, params = routes.get_producers(q, page, limit, order_by, sort, letter)
        return ProducerList(**self._get(endpoint, params))

    def get_producer(self, producer_id: int) -> Producer:
        """Get producer information."""
        endpoint, params = routes.get_producer(producer_id)
        return Producer(**self._get(endpoint, params)["data"])

    def get_producer_full(self, producer_id: int) -> Producer:
        """Get producer information with full details."""
        endpoint, params = routes.get_producer_full(producer_id)
        return Producer(**self._get(endpoint, params)["data"])

    def get_producer_external(self, producer_id: int) -> AnimeExternal:
        """Get external links for a producer."""
        endpoint, params = routes.get_producer_external(producer_id)
        return AnimeExternal(**self._get(endpoint, params))

    def get_producer_ids(self) -> ProducerIds:
        """Get producer IDs."""
        endpoint, params = routes.get_producer_ids()
        return ProducerIds(**self._get(endpoint, params))

    def get_genres_anime(self, filter: str | None = None) -> GenreList:
        """Get anime genres."""
        endpoint, params = routes.get_genres_anime(filter)
        return GenreList(**self._get(endpoint, params))

    def get_genres_manga(self, filter: str | None = None) -> GenreList:
        """Get manga genres."""
        endpoint, params = routes.get_genres_manga(filter)
        return GenreList(**self._get(endpoint, params))

    def get_magazines(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        letter: str | None = None,
    ) -> MagazineList:
        """Search for manga magazines."""
        endpoint, params = routes.get_magazines(q, page, limit, order_by, sort, letter)
        return MagazineList(**self._get(endpoint, params))

    def get_random_anime(
        self, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> Anime:
        """Get a random anime."""
        endpoint, params = routes.get_random_anime(sfw, sfw_strict)
        return Anime(**self._get(endpoint, params)["data"])

    def get_random_manga(
        self, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> Manga:
        """Get a random manga."""
        endpoint, params = routes.get_random_manga(sfw, sfw_strict)
        return Manga(**self._get(endpoint, params)["data"])

    def get_random_character(self) -> Character:
        """Get a random character."""
        endpoint, params = routes.get_random_character()
        return Character(**self._get(endpoint, params)["data"])

    def get_random_person(self) -> Person:
        """Get a random person."""
        endpoint, params = routes.get_random_person()
        return Person(**self._get(endpoint, params)["data"])

    def get_recommendations_anime(
        self,
        page: int | None = None,
        limit: int | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> AnimeRecommendations:
        """Get global anime recommendations."""
        endpoint, params = routes.get_recommendations_anime(page, limit, sfw, sfw_strict)
        return AnimeRecommendations(**self._get(endpoint, params))

    def get_recommendations_manga(
        self,
        page: int | None = None,
        limit: int | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> MangaRecommendations:
        """Get global manga recommendations."""
        endpoint, params = routes.get_recommendations_manga(page, limit, sfw, sfw_strict)
        return MangaRecommendations(**self._get(endpoint, params))

    def get_top_anime(
        self,
        page: int | None = None,
        limit: int | None = None,
        type: str | None = None,
        filter: str | None = None,
        rating: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> AnimeSearch:
        """Get top anime."""
        endpoint, params = routes.get_top_anime(page, limit, type, filter, rating, sfw, sfw_strict)
        return AnimeSearch(**self._get(endpoint, params))

    def get_top_manga(
        self,
        page: int | None = None,
        limit: int | None = None,
        type: str | None = None,
        filter: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> MangaSearch:
        """Get top manga."""
        endpoint, params = routes.get_top_manga(page, limit, type, filter, sfw, sfw_strict)
        return MangaSearch(**self._get(endpoint, params))

    def get_top_characters(
        self, page: int | None = None, limit: int | None = None
    ) -> CharacterList:
        """Get top characters."""
        endpoint, params = routes.get_top_characters(page, limit)
        return CharacterList(**self._get(endpoint, params))

    def get_top_people(
        self, page: int | None = None, limit: int | None = None
    ) -> PersonList:
        """Get top people."""
        endpoint, params = routes.get_top_people(page, limit)
        return PersonList(**self._get(endpoint, params))

    def get_top_reviews(
        self,
        page: int | None = None,
        limit: int | None = None,
        type: str | None = None,
        preliminary: bool | None = None,
        spoilers: bool | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> AnimeReviews:
        """Get top reviews."""
        endpoint, params = routes.get_top_reviews(
            page, limit, type, preliminary, spoilers, sfw, sfw_strict
        )
        return AnimeReviews(**self._get(endpoint, params))

    def get_seasons(self) -> SeasonCalendar:
        """Get the available anime seasons."""
        endpoint, params = routes.get_seasons()
        return SeasonCalendar(**self._get(endpoint, params))

    def get_season(
        self,
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
    ) -> SeasonList:
        """Get anime for a specific season."""
        endpoint, params = routes.get_season(
            year,
            season,
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
        return SeasonList(**self._get(endpoint, params))

    def get_seasons_now(
        self,
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
    ) -> SeasonList:
        """Get anime from the current season."""
        endpoint, params = routes.get_seasons_now(
            filter=filter,
            rating=rating,
            sfw=sfw,
            sfw_strict=sfw_strict,
            unapproved=unapproved,
            continuing=continuing,
            kids=kids,
            order_by=order_by,
            sort=sort,
            page=page,
            limit=limit,
        )
        return SeasonList(**self._get(endpoint, params))

    def get_seasons_previous(
        self,
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
    ) -> SeasonList:
        """Get anime from the previous season."""
        endpoint, params = routes.get_seasons_previous(
            filter=filter,
            rating=rating,
            sfw=sfw,
            sfw_strict=sfw_strict,
            unapproved=unapproved,
            continuing=continuing,
            kids=kids,
            order_by=order_by,
            sort=sort,
            page=page,
            limit=limit,
        )
        return SeasonList(**self._get(endpoint, params))

    def get_seasons_upcoming(
        self,
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
    ) -> SeasonList:
        """Get anime from the upcoming season."""
        endpoint, params = routes.get_seasons_upcoming(
            filter=filter,
            rating=rating,
            sfw=sfw,
            sfw_strict=sfw_strict,
            unapproved=unapproved,
            continuing=continuing,
            kids=kids,
            order_by=order_by,
            sort=sort,
            page=page,
            limit=limit,
        )
        return SeasonList(**self._get(endpoint, params))

    def get_schedules(
        self,
        filter: str | None = None,
        kids: bool | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
        unapproved: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> ScheduleList:
        """Get anime broadcast schedules."""
        endpoint, params = routes.get_schedules(
            filter, kids, sfw, sfw_strict, unapproved, page, limit
        )
        return ScheduleList(**self._get(endpoint, params))

    def get_reviews_anime(
        self,
        page: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
        preliminary: bool | None = None,
        spoilers: bool | None = None,
        sentiment: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> AnimeReviews:
        """Get global anime reviews."""
        endpoint, params = routes.get_reviews_anime(
            page, limit, sort, preliminary, spoilers, sentiment, sfw, sfw_strict
        )
        return AnimeReviews(**self._get(endpoint, params))

    def get_reviews_manga(
        self,
        page: int | None = None,
        limit: int | None = None,
        sort: str | None = None,
        preliminary: bool | None = None,
        spoilers: bool | None = None,
        sentiment: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> MangaReviews:
        """Get global manga reviews."""
        endpoint, params = routes.get_reviews_manga(
            page, limit, sort, preliminary, spoilers, sentiment, sfw, sfw_strict
        )
        return MangaReviews(**self._get(endpoint, params))

    def get_stacks(
        self,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
        spoilers: bool | None = None,
        challenges: bool | None = None,
        official: bool | None = None,
        stack_type: str | None = None,
        sfw: bool | None = None,
        sfw_strict: bool | None = None,
    ) -> StackList:
        """Search global stacks."""
        endpoint, params = routes.get_stacks(
            q,
            page,
            limit,
            order_by,
            sort,
            spoilers,
            challenges,
            official,
            stack_type,
            sfw,
            sfw_strict,
        )
        return StackList(**self._get(endpoint, params))

    def get_stack(
        self, stack_id: int, sfw: bool | None = None, sfw_strict: bool | None = None
    ) -> StackDetail:
        """Get stack details."""
        endpoint, params = routes.get_stack(stack_id, sfw, sfw_strict)
        return StackDetail(**self._get(endpoint, params))

    def get_articles(
        self,
        q: str | None = None,
        tag: str | None = None,
        page: int | None = None,
        limit: int | None = None,
        order_by: str | None = None,
        sort: str | None = None,
    ) -> ArticleList:
        """Search global articles."""
        endpoint, params = routes.get_articles(q, tag, page, limit, order_by, sort)
        return ArticleList(**self._get(endpoint, params))

    def get_article(self, article_id: int) -> Article:
        """Get article details."""
        endpoint, params = routes.get_article(article_id)
        return Article(**self._get(endpoint, params)["data"])

    def get_article_tags(self) -> ArticleTags:
        """Get article tags."""
        endpoint, params = routes.get_article_tags()
        return ArticleTags(**self._get(endpoint, params))

    def get_news(
        self,
        q: str | None = None,
        tag: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> NewsList:
        """Search global news."""
        endpoint, params = routes.get_news(q, tag, page, limit)
        return NewsList(**self._get(endpoint, params))

    def get_news_detail(self, news_id: int) -> News:
        """Get news details."""
        endpoint, params = routes.get_news_detail(news_id)
        return News(**self._get(endpoint, params)["data"])

    def get_news_tags(self) -> NewsTags:
        """Get news tags."""
        endpoint, params = routes.get_news_tags()
        return NewsTags(**self._get(endpoint, params))
