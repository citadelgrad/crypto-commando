import os
import json
from pathlib import Path

from prompt_toolkit.shortcuts.prompt import prompt
from prompt_toolkit.completion import WordCompleter

from crypto_commando.config import APP_HOME
from crypto_commando.views.templates import TRANSACTIONS


class Transaction:
    def __init__(self) -> None:
        self.initialize_file()
        self.entries = self.read_local_data().get("transactions")

    def read_local_data(self):
        """Reads the transactions file.

        Returns:
            dict: transactions: Unprocessed transactions
        """
        with open(f"{APP_HOME}/transactions.json", "r") as f:
            transactions = json.loads(f.read())

        return transactions

    def initialize_file(self):
        """Make sure a transaction file exists or create one.

        Returns:
            [type]: [description]
        """
        p = Path(APP_HOME)
        p.mkdir(exist_ok=True)
        try:
            with open(f"{APP_HOME}/transactions.json", "r") as f:
                json.loads(f.read())
        except FileNotFoundError as error:
            with open(f"{APP_HOME}/transactions.json", "w") as write_file:
                json.dump(TRANSACTIONS, write_file, indent=4)
        except Exception as error:
            raise

    def write_transaction(self, entry):
        """Write pretty print JSON data to transactions.json

        Args:
            entry (dict): empty transaction entry.

        Returns:
            dict: pending transactions
        """
        current_data = self.read_local_data()
        current_data.get("transactions").append(entry)
        with open(f"{APP_HOME}/transactions.json", "w") as write_file:
            json.dump(current_data, write_file, indent=4)


# def transactions_completer():
#     """Get account names from the local file transactions.json.

#     Returns:
#         list: account names
#     """
#     transactions = load_transactions()
#     return [
#         f"{transaction.get('name')}" for transaction in transactions.get("transactions")
#     ]


# def transactions_tuple():
#     """Get account names from the local file transactions.json.

#     Returns:
#         list: account names
#     """
#     transactions = load_transactions()
#     return [
#         (transaction.get("name"), transaction.get("name"))
#         for transaction in transactions.get("transactions")
#     ]
