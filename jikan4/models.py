from typing import List
from pydantic import BaseModel, Field


class Date(BaseModel):
    day: int | None = None
    month: int | None = None
    year: int | None = None


class JPG(BaseModel):
    image_url: str | None = None
    small_image_url: str | None = None
    large_image_url: str | None = None


class Webp(BaseModel):
    image_url: str | None = None
    small_image_url: str | None = None
    large_image_url: str | None = None


class Image(BaseModel):
    jpg: JPG = JPG()
    webp: Webp = Webp()


class Trailer(BaseModel):
    youtube_id: str | None = None
    url: str | None = None
    embed_url: str | None = None


class Title(BaseModel):
    type: str | None = None
    title: str | None = None


class Prop(BaseModel):
    from_: Date = Field(default_factory=Date, alias="from")
    to: Date = Date()
    string: str | None = None


class AirDate(BaseModel):
    from_: str | None = Field(None, alias="from")
    to: str | None = None
    prop: Prop = Prop()


class Broadcast(BaseModel):
    day: str | None = None
    time: str | None = None
    timezone: str | None = None
    string: str | None = None


class Producer(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Licenser(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Studio(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Streaming(BaseModel):
    name: str | None = None
    url: str | None = None


class Genre(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class ExplicitGenre(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class ThemeGenre(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Demographic(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Entry(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Related(BaseModel):
    relation: str | None = None
    entry: List[Entry] = []


class Theme(BaseModel):
    openings: List[str] = []
    endings: List[str] = []


class External(BaseModel):
    name: str | None = None
    url: str | None = None


class Items(BaseModel):
    count: int = 0
    total: int = 0
    per_page: int = 0


class Pagination(BaseModel):
    last_visible_page: int = 1
    has_next_page: bool = False
    current_page: int = 1
    items: Items = Items()


class Character(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    images: Image = Image()
    name: str | None = None


class Person(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    images: Image = Image()
    name: str | None = None


class VoiceActor(BaseModel):
    person: Person = Person()
    language: str | None = None


class Staff(BaseModel):
    person: Person = Person()
    positions: List[str] = []


class News(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    title: str | None = None
    date: str | None = None
    author_username: str | None = None
    author_url: str | None = None
    forum_url: str | None = None
    images: Image = Image()
    comments: int = 0
    excerpt: str | None = None
    content: str | None = None
    published_at: str | None = None
    tags: List[str] = []


class Episode(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    title: str | None = None
    title_japanese: str | None = None
    title_romanji: str | None = None
    duration: float | None = None
    aired: str | None = None
    filler: bool = False
    recap: bool = False
    synopsis: str | None = None
    forum_url: str | None = None


class Anime(BaseModel):
    mal_id: int
    url: str
    images: Image = Image()
    trailer: Trailer = Trailer()
    approved: bool | None = None
    titles: List[Title] = []
    title: str | None = None
    title_english: str | None = None
    title_japanese: str | None = None
    title_synonyms: List[str] = []
    type: str | None = None
    source: str | None = None
    episodes: int | None = None
    status: str | None = None
    airing: bool | None = None
    aired: AirDate = AirDate()
    duration: str | None = None
    rating: str | None = None
    score: float | None = None
    scored_by: int | None = None
    rank: int | None = None
    popularity: int | None = None
    members: int | None = None
    favorites: int | None = None
    synopsis: str | None = None
    background: str | None = None
    season: str | None = None
    year: int | None = None
    broadcast: Broadcast = Broadcast()
    producers: List[Producer] = []
    licensors: List[Licenser] = []
    studios: List[Studio] = []
    genres: List[Genre] = []
    explicit_genres: List[ExplicitGenre] = []
    ThemeGenres: List[ThemeGenre] = []
    demographics: List[Demographic] = []
    relations: List[Related] = []
    theme: Theme = Theme()
    external: list[External] = []
    streaming: List[Streaming] = []


class AnimeSearch(BaseModel):
    data: List[Anime] = []
    pagination: Pagination = Pagination()


class AnimeCharacter(BaseModel):
    character: Character = Character()
    role: str | None = None
    voice_actors: List[VoiceActor] = []


class AnimeCharacters(BaseModel):
    data: List[AnimeCharacter] = []
    pagination: Pagination = Pagination()


class AnimeStaff(BaseModel):
    data: List[Staff] = []
    pagination: Pagination = Pagination()


class AnimeEpisodes(BaseModel):
    data: List[Episode] = []
    pagination: Pagination = Pagination()


class AnimeNews(BaseModel):
    data: List[News] = []
    pagination: Pagination = Pagination()


class Comment(BaseModel):
    url: str
    author_username: str
    author_url: str
    date: str


class Forum(BaseModel):
    mal_id: int
    url: str
    title: str
    date: str
    author_username: str
    author_url: str
    comments: int
    last_comment: Comment


class AnimeForum(BaseModel):
    data: List[Forum] = []


class Recommendation(BaseModel):
    entry: Anime | None = None
    url: str | None = None
    votes: int = 0


class AnimeRecommendations(BaseModel):
    data: List[Recommendation] = []


class Article(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    title: str | None = None
    date: str | None = None
    author_username: str | None = None
    author_url: str | None = None
    forum_url: str | None = None
    images: Image = Image()
    comments: int = 0
    excerpt: str | None = None
    summary: str | None = None
    published_at: str | None = None
    views: int = 0
    tags: List[str] = []


class AnimeArticles(BaseModel):
    data: List[Article] = []
    pagination: Pagination = Pagination()


class Video(BaseModel):
    title: str | None = None
    trailer: Trailer = Trailer()
    views: int = 0
    likes: int = 0
    dislikes: int = 0
    comment_count: int = 0
    published_at: str | None = None
    duration: str | None = None
    privacy_status: str | None = None
    region_restriction: object | None = None
    embeddable: bool | None = None


class AnimeVideos(BaseModel):
    data: dict[str, List[object]] = {}


class AnimeEpisodeVideos(BaseModel):
    data: List[object] = []
    pagination: Pagination = Pagination()


class AnimePictures(BaseModel):
    data: List[Image] = []


class AnimeStatistics(BaseModel):
    data: dict[str, object] = {}


class AnimeMoreInfo(BaseModel):
    data: object | None = None


class AnimeRelations(BaseModel):
    data: List[Related] = []


class AnimeThemes(BaseModel):
    data: Theme = Theme()


class AnimeExternal(BaseModel):
    data: List[External] = []


class AnimeStreaming(BaseModel):
    data: List[Streaming] = []


class Review(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    type: str | None = None
    reactions: dict[str, int] = {}
    date: str | None = None
    review: str | None = None
    score: int | None = None
    tags: List[str] = []
    is_spoiler: bool = False
    is_preliminary: bool = False
    episodes_watched: int | None = None
    user: Person | None = None


class AnimeReviews(BaseModel):
    data: List[Review] = []
    pagination: Pagination = Pagination()


class Stack(BaseModel):
    mal_id: int | None = None
    url: str | None = None
    stack_type: str | None = None
    title: str | None = None
    description: str | None = None
    author_username: str | None = None
    author_url: str | None = None
    is_official: bool = False
    is_challenge: bool = False
    is_spoiler: bool = False
    restack_count: int = 0
    entry_count: int = 0
    created_at: str | None = None


class AnimeStacks(BaseModel):
    data: List[Stack] = []
    pagination: Pagination = Pagination()


class AnimeCatalog(BaseModel):
    data: List[Anime] = []
    pagination: Pagination = Pagination()


class AnimeId(BaseModel):
    mal_id: int | None = None
    title: str | None = None


class AnimeIds(BaseModel):
    data: List[AnimeId] = []
    pagination: Pagination = Pagination()


class Author(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Serialization(BaseModel):
    mal_id: int | None = None
    type: str | None = None
    name: str | None = None
    url: str | None = None


class Manga(BaseModel):
    mal_id: int
    url: str
    images: Image = Image()
    approved: bool | None = None
    titles: List[Title] = []
    title: str | None = None
    title_english: str | None = None
    title_japanese: str | None = None
    title_synonyms: List[str] = []
    type: str | None = None
    chapters: int | None = None
    volumes: int | None = None
    status: str | None = None
    publishing: bool | None = None
    published: AirDate = AirDate()
    score: float | None = None
    scored_by: int | None = None
    rank: int | None = None
    popularity: int | None = None
    members: int | None = None
    favorites: int | None = None
    synopsis: str | None = None
    background: str | None = None
    authors: List[Author] = []
    serializations: List[Serialization] = []
    genres: List[Genre] = []
    explicit_genres: List[ExplicitGenre] = []
    themes: List[ThemeGenre] = []
    demographics: List[Demographic] = []
    relations: List[Related] = []
    external: List[External] = []


class MangaSearch(BaseModel):
    data: List[Manga] = []
    pagination: Pagination = Pagination()


class MangaCharacters(AnimeCharacters):
    pass


class MangaNews(AnimeNews):
    pass


class MangaArticles(AnimeArticles):
    pass


class MangaPictures(AnimePictures):
    pass


class MangaStatistics(AnimeStatistics):
    pass


class MangaMoreInfo(AnimeMoreInfo):
    pass


class MangaRelations(AnimeRelations):
    pass


class MangaExternal(AnimeExternal):
    pass


class MangaReviews(AnimeReviews):
    pass


class MangaStacks(AnimeStacks):
    pass


class MangaRecommendation(BaseModel):
    entry: Manga | None = None
    url: str | None = None
    votes: int = 0


class MangaRecommendations(BaseModel):
    data: List[MangaRecommendation] = []


class MangaCatalog(BaseModel):
    data: List[Manga] = []
    pagination: Pagination = Pagination()


class MangaId(BaseModel):
    mal_id: int | None = None
    title: str | None = None


class MangaIds(BaseModel):
    data: List[MangaId] = []
    pagination: Pagination = Pagination()


class CharacterAnime(BaseModel):
    role: str | None = None
    anime: Entry = Entry()
    character: Character = Character()


class CharacterManga(BaseModel):
    role: str | None = None
    manga: Entry = Entry()
    character: Character = Character()


class PersonAnime(BaseModel):
    position: str | None = None
    anime: Entry = Entry()


class PersonManga(BaseModel):
    position: str | None = None
    manga: Entry = Entry()


class CharacterAnimeList(BaseModel):
    data: List[CharacterAnime] = []
    pagination: Pagination = Pagination()


class CharacterMangaList(BaseModel):
    data: List[CharacterManga] = []
    pagination: Pagination = Pagination()


class PersonAnimeList(BaseModel):
    data: List[PersonAnime] = []
    pagination: Pagination = Pagination()


class PersonMangaList(BaseModel):
    data: List[PersonManga] = []
    pagination: Pagination = Pagination()


class CharacterList(BaseModel):
    data: List[Character] = []
    pagination: Pagination = Pagination()


class PersonList(BaseModel):
    data: List[Person] = []
    pagination: Pagination = Pagination()


class ProducerList(BaseModel):
    data: List[Producer] = []
    pagination: Pagination = Pagination()


class GenreList(BaseModel):
    data: List[Genre] = []


class MagazineList(BaseModel):
    data: List[Genre] = []


class CharacterIds(BaseModel):
    data: List[dict[str, object]] = []


class PersonIds(BaseModel):
    data: List[dict[str, object]] = []


class ProducerIds(BaseModel):
    data: List[dict[str, object]] = []


class VoiceActorList(BaseModel):
    data: List[VoiceActor] = []
    pagination: Pagination = Pagination()


class ArticleList(BaseModel):
    data: List[Article] = []
    pagination: Pagination = Pagination()


class ArticleTag(BaseModel):
    name: str | None = None
    count: int = 0


class ArticleTags(BaseModel):
    data: List[ArticleTag] = []


class NewsList(BaseModel):
    data: List[News] = []
    pagination: Pagination = Pagination()


class NewsTag(BaseModel):
    name: str | None = None
    count: int = 0


class NewsTags(BaseModel):
    data: List[NewsTag] = []


class StackList(AnimeStacks):
    pass


class StackDetail(Stack):
    entries: List[Entry] = []


class SeasonList(AnimeSearch):
    pass


class ScheduleList(AnimeSearch):
    pass


class Season(BaseModel):
    year: int | None = None
    seasons: List[str] = []


class SeasonCalendar(BaseModel):
    data: List[Season] = []
