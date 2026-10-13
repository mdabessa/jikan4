class BaseClient:
    """Shared configuration for sync and async API clients."""

    def __init__(self, base_url: str, rate_limit: int) -> None:
        self.base_url = base_url.rstrip("/")
        self.rate_limit = rate_limit

        if rate_limit:
            self._setup_limiter(rate_limit)

    def _setup_limiter(self, rate_limit: int) -> None:
        raise NotImplementedError