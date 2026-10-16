import inspect

from jikan4 import AioJikan, Jikan, __version__
from jikan4.aiojikan import AioJikan as ModuleAioJikan
from jikan4.jikan import Jikan as ModuleJikan


def test_public_client_exports():
    assert Jikan is ModuleJikan
    assert AioJikan is ModuleAioJikan
    assert __version__


def test_public_client_methods_have_docstrings():
    for client in (Jikan, AioJikan):
        public_methods = inspect.getmembers(client, predicate=inspect.isfunction)
        assert all(
            inspect.getdoc(method)
            for name, method in public_methods
            if not name.startswith("_")
        )
