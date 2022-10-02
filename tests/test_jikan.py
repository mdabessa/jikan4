import json
import pytest

from jikan4.jikan import Jikan


@pytest.fixture
def jikan():
    return Jikan()


def test_get_anime(jikan: Jikan):
    resp = jikan.get_anime(1)
    with open('./tests/responses/get_anime(1).json', 'r') as f:
        expected = json.load(f)

    assert resp == expected, 'Response does not match expected response'
