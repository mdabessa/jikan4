from jikan4 import AioJikan, Jikan, __version__
from jikan4.aiojikan import AioJikan as ModuleAioJikan
from jikan4.jikan import Jikan as ModuleJikan


def test_public_client_exports():
    assert Jikan is ModuleJikan
    assert AioJikan is ModuleAioJikan
    assert __version__
