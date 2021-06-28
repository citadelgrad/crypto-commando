import json
from unittest.mock import patch

from crypto_commando.views.wallet import (
    wallet_completer,
    create_account_file,
    load_wallet,
    create_account,
)

# Test data: not a real account.
wallet_fixture = """{
    "accounts": [
        {
            "network": "Ethereum - MAINNET",
            "name": "Scott",
            "address": "0x5c13C9ef6c923C34d0716d8017f0bfaF13e1f003",
            "private_key": "0x04e2b2c0000a4fe0afaf1ba58510000849c02bfd04c79fd0e063971fdd1a801f"
        }
    ]
}"""


@patch(
    "crypto_commando.views.wallet.load_wallet",
    return_value=json.loads(wallet_fixture),
)
def test_wallet_completer(mocked_load_wallet):
    assert isinstance(wallet_completer(), list)
