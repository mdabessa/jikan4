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
    
## Phase 2: Centralize Request Specs and Shared Client Base
branch: `refactor/centralize-request-specs`

Goal: a single source of truth for routes, parameter names, defaults, and
parameter normalization, without changing the public API.

Constraint: the public client methods keep explicit signatures, type hints, and
Google-style docstrings on both clients, so VS Code hover, signature help, and
static analysis keep working. Code generation and dynamic `*args`/`**kwargs`
dispatch are intentionally out of scope because they would break
IDE-trackable signatures and documentation.

- [x] Add a transport-agnostic spec module (e.g. `jikan4/routes.py`) of pure
    builder functions. Each builder accepts an endpoint's arguments and returns
    an `(endpoint, params)` tuple.
- [x] Move endpoint paths, Tenrai parameter names, defaults, the `sfw_strict` to
    `sfw-strict` conversion, and `exclude_none` usage into the builders.
    Preserve valid falsy values such as `False` and `0`.
- [x] Add a shared base client (e.g. `jikan4/base.py`) holding `base_url`
    normalization/storage and `rate_limit` handling, with a transport-specific
    limiter setup hook.
- [ ] Refactor `Jikan` and `AioJikan` to inherit from the base client, keeping
    each public method's existing signature, type hints, and docstring.
    Reduce each method body to: build the spec, call `_get`, construct the
    response model.
- [ ] Preserve the current public surface exactly: same method names, arguments,
    defaults, endpoints, request parameters, and returned models. This phase
    must not break existing usage.
- [ ] Keep the thin call-and-parse line duplicated on purpose between the sync
    and async clients; only route/parameter logic and shared configuration are
    centralized.

## Phase 3: Add Parameter Parity Tests

- [ ] Drive both clients from one parametrized test suite built on the shared
    spec table, so sync/async parity is enforced in a single place.
- [ ] Add mocked request tests for both clients that verify:
    The correct endpoint is used.
    Optional parameters are forwarded.
    `sfw_strict` is converted to `sfw-strict`.
    `None` values are omitted.
    `False` values are preserved.
    Existing positional calls still work.
- [ ] Complete this phase before adding new endpoint wrappers.

## Phase 4: Add Anime Endpoint Coverage

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

## Phase 5: Add Manga Support

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

## Phase 6: Add Catalog Resources

- [ ] Implement catalog resources:
    Characters
    People
    Producers
    Genres
    Magazines
- [ ] Share reusable pagination, image, person, and entry models where schemas are compatible.

## Phase 7: Add Discovery Endpoints

- [ ] Implement discovery endpoints:
    Random anime, manga, characters, and people
    Anime and manga recommendations
    Top anime, manga, people, characters, and reviews
    Seasons
    Reviews
    Schedules

## Phase 8: Add Articles, News, and Stacks

- [ ] Implement content endpoints:
    Global stacks
    Stack details
    Articles
    Article tags
    Article details
    News
    News tags
    News details

## Phase 9: Update Documentation and Public API

- [ ] Update project documentation and public API:
    `README.md`
    `__init__.py`
    Public API tests
    Sync and async usage examples