import json
from unittest import mock
from unittest.mock import patch

from crypto_commando.views.transactions import Transaction

NOW_TRANSACTION = {
    "exchange": "kyber",
    "account": "Scott",
    "transaction_type": "RunNow",
    "swap_from": "BAT",
    "swap_from_amount": "100",
    "price_min": ".75",
    "price_max": "1.2",
    "swap_to": "USDC",
    "gas_option": "fast",
}


def test_read_local_data():
    transaction = Transaction()
    assert isinstance(transaction, Transaction)
    assert isinstance(transaction.read_local_data(), dict)
    assert isinstance(transaction.read_local_data().get("transactions"), list)


def test_write_transaction():
    transaction = Transaction()
    with patch.object(transaction, "write_transaction"):
        transaction.write_transaction(NOW_TRANSACTION)
        assert transaction.write_transaction.called_once
