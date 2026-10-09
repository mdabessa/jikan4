# Development Plan
Apply each change to both `Jikan` and `AioJikan`.
Each phase should be a separate branch, and each step should be a separate commit. 
After each phase, merge the branch into `main` and tag it with the next semantic version number, and publish to PyPI.

## Phase 1: Close Partial Parameter Gaps
branch: `feat/close-parameter-gaps`

- [x] Update `search_anime` with optional Tenrai parameters:
    `limit`
    `status`
    `score`
    `min_score`
    `max_score`
    `rating`
    `genres`
    `genres_exclude`
    `order_by`
    `sort`
    `letter`
    `producers`
    `start_date`
    `end_date`
    `sfw`
    `sfw_strict`
- [x] Update `get_anime_full` with:
    `sfw`
    `sfw_strict`
- [x] Update `get_anime_episodes` with:
    `page`
- [x] Update `get_anime_news` with:
    `sfw`
    `sfw_strict`
    Keep the existing `page` argument.
- [x] Update `get_anime_forum` with:
    `page`
    `order_by`
    `sort`
    Keep `filter` and document that Tenrai currently supports only the episode filter.
- [x] Standardize parameter handling:
    Convert `sfw_strict` to the Tenrai query name `sfw-strict`.
    Preserve `genres_exclude` as the Tenrai query name.
    Omit parameters whose value is `None`.
    Preserve valid falsy values such as `False` and `0`.
    
Avoid duplicating parameter-building logic between sync and async clients where practical.

## Phase 2: Add Parameter Parity Tests

- [ ] Add mocked request tests for both clients that verify:
    The correct endpoint is used.
    Optional parameters are forwarded.
    `sfw_strict` is converted to `sfw-strict`.
    `None` values are omitted.
    `False` values are preserved.
    Existing positional calls still work.
- [ ] Complete this phase before adding new endpoint wrappers.

## Phase 3: Add Anime Endpoint Coverage

- [ ] Implement the remaining anime routes:
    Recommendations
    Articles
    Videos
    Episode videos
    Pictures
    Statistics
    More info
    Relations
    Themes
    External links
    Streaming links
    Reviews
    Stacks
    Deleted anime
    Unapproved anime
    Denied anime
    Anime IDs
- [ ] Add corresponding Pydantic models as required by each response.

## Phase 4: Add Manga Support

- [ ] Add manga models and client methods for:
    Search
    Details
    Full details
    Recommendations
    Characters
    News
    Articles
    Pictures
    Statistics
    More info
    Relations
    External links
    Reviews
    Stacks
    Deleted manga
    Manga IDs

## Phase 5: Add Catalog Resources

- [ ] Implement catalog resources:
    Characters
    People
    Producers
    Genres
    Magazines
- [ ] Share reusable pagination, image, person, and entry models where schemas are compatible.

## Phase 6: Add Discovery Endpoints

- [ ] Implement discovery endpoints:
    Random anime, manga, characters, and people
    Anime and manga recommendations
    Top anime, manga, people, characters, and reviews
    Seasons
    Reviews
    Schedules

## Phase 7: Add Articles, News, and Stacks

- [ ] Implement content endpoints:
    Global stacks
    Stack details
    Articles
    Article tags
    Article details
    News
    News tags
    News details

## Phase 8: Update Documentation and Public API

- [ ] Update project documentation and public API:
    `README.md`
    `__init__.py`
    Public API tests
    Sync and async usage examples