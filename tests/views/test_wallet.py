from web3 import Web3
import pytest
from unittest.mock import patch

from crypto_commando.views.wallet import (
    CMDOAccount,
    Wallet,
)


def test_wallet(example_wallet):
    w = Wallet(accounts_file=example_wallet)
    assert len(w.accounts) == 2
    account = w.accounts[0]
    assert isinstance(account, CMDOAccount)
    assert account.name
    assert account.network == "Ethereum - MAINNET"
    assert Web3.isChecksumAddress(account.eth_acc.address)
    assert not Web3.isChecksumAddress("0x000000")
