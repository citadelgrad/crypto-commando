from unittest.mock import MagicMock
from prompt_toolkit.completion.word_completer import WordCompleter
from crypto_commando.views.tokens import (
    exchange_completer,
    exchange_tuple,
)


def test_exchange_completer():
    exchange_list = exchange_completer()
    assert isinstance(exchange_list, list)
    assert exchange_list[0] == "aave"


def test_exchange_tuple():
    ex = exchange_tuple()
    assert isinstance(ex, list)
    assert isinstance(ex[0], tuple)
