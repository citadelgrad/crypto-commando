import json
import pytest
from unittest.mock import patch

from crypto_commando.views.wallet import (
    CMDOAccount,
    Wallet,
)


def test_wallet(example_wallet):
    w = Wallet(accounts_file=example_wallet)
    assert len(w.accounts) == 2
    assert isinstance(w.accounts[0], CMDOAccount)
