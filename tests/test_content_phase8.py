import pytest

from jikan4 import routes
from jikan4.aiojikan import AioJikan
from jikan4.jikan import Jikan
from jikan4.models import Article, News, StackDetail


@pytest.mark.parametrize(
    ("builder", "args", "expected"),
    [
        (routes.get_stacks, (), ("stacks", {})),
        (routes.get_stack, (1,), ("stacks/1", {})),
        (routes.get_articles, (), ("articles", {})),
        (routes.get_article, (1,), ("articles/1", {})),
        (routes.get_article_tags, (), ("articles/tags", {})),
        (routes.get_news, (), ("news", {})),
        (routes.get_news_detail, (1,), ("news/1", {})),
        (routes.get_news_tags, (), ("news/tags", {})),
    ],
)
def test_content_route_builders(builder, args, expected):
    assert builder(*args) == expected


def test_content_parameters_preserve_falsy_values():
    assert routes.get_stacks(page=0, limit=0, spoilers=False, sfw_strict=True) == (
        "stacks",
        {"page": 0, "limit": 0, "spoilers": False, "sfw-strict": True},
    )
    assert routes.get_articles(q="anime", page=0, limit=0, sort="desc") == (
        "articles",
        {"q": "anime", "page": 0, "limit": 0, "sort": "desc"},
    )
    assert routes.get_news(tag="More Info", page=0, limit=0) == (
        "news",
        {"tag": "More Info", "page": 0, "limit": 0},
    )


def test_content_detail_models():
    assert isinstance(Article(title="Article"), Article)
    assert isinstance(News(title="News"), News)
    assert isinstance(StackDetail(title="Stack"), StackDetail)


def test_sync_content_methods_use_routes(monkeypatch):
    client = Jikan(rate_limit=0)
    captured = []

    def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint in {"articles/1", "news/1"}:
            return {"data": {"title": "sample"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert client.get_article(1).title == "sample"
    assert client.get_news_detail(1).title == "sample"
    client.get_stacks(page=0, spoilers=False)
    client.get_articles(tag="Spoiler", page=0)
    client.get_article_tags()
    client.get_news(page=0)
    client.get_news_tags()
    client.get_stack(1, sfw=False)

    assert captured == [
        ("articles/1", {}),
        ("news/1", {}),
        ("stacks", {"page": 0, "spoilers": False}),
        ("articles", {"tag": "Spoiler", "page": 0}),
        ("articles/tags", {}),
        ("news", {"page": 0}),
        ("news/tags", {}),
        ("stacks/1", {"sfw": False}),
    ]


@pytest.mark.asyncio
async def test_async_content_methods_use_routes(monkeypatch):
    client = AioJikan(rate_limit=0)
    captured = []

    async def fake_get(endpoint, params):
        captured.append((endpoint, params))
        if endpoint in {"articles/1", "news/1"}:
            return {"data": {"title": "sample"}}
        return {}

    monkeypatch.setattr(client, "_get", fake_get)
    assert (await client.get_article(1)).title == "sample"
    assert (await client.get_news_detail(1)).title == "sample"
    await client.get_stacks(page=0, spoilers=False)
    await client.get_articles(tag="Spoiler", page=0)
    await client.get_article_tags()
    await client.get_news(page=0)
    await client.get_news_tags()
    await client.get_stack(1, sfw=False)

    assert captured == [
        ("articles/1", {}),
        ("news/1", {}),
        ("stacks", {"page": 0, "spoilers": False}),
        ("articles", {"tag": "Spoiler", "page": 0}),
        ("articles/tags", {}),
        ("news", {"page": 0}),
        ("news/tags", {}),
        ("stacks/1", {"sfw": False}),
    ]
