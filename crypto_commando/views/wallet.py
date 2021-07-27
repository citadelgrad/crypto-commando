import os
import json
from pathlib import Path

from eth_account import Account
from prompt_toolkit.shortcuts.prompt import prompt
from prompt_toolkit.completion import WordCompleter

from crypto_commando.config import APP_HOME, NETWORKS_SIMPLE
from crypto_commando.views.templates import WALLET


def create_account_file(template):
    """Write pretty print JSON data to accounts.json

    Args:
        template (dict): empty account template.

    Returns:
        dict: wallet accounts
    """
    #
    with open(f"{APP_HOME}/accounts.json", "w") as write_file:
        json.dump(template, write_file, indent=4)

    with open(f"{APP_HOME}/accounts.json", "r") as f:
        accounts = json.loads(f.read())

    return accounts


def load_wallet():
    p = Path(APP_HOME)
    p.mkdir(exist_ok=True)
    try:
        with open(f"{APP_HOME}/accounts.json", "r") as f:
            return json.loads(f.read())
    except FileNotFoundError as error:
        return create_account_file(WALLET)
    except Exception as error:
        raise


def create_account():
    """Create a Ethereum compatible wallet."""
    wallet = load_wallet()
    new_account = dict()
    new_account["network"] = prompt(
        "Select the network: ",
        completer=WordCompleter(NETWORKS_SIMPLE, ignore_case=True),
    )
    new_account["name"] = prompt("Name this account: ")
    new_account["address"] = prompt("Your public address 0x123...dEfI: ")
    new_account["private_key"] = prompt("Private Key (DANGER): ")
    wallet.get("accounts").append(new_account)
    create_account_file(wallet)


def wallet_completer():
    """Get account names from the local file accounts.json.

    Returns:
        list: account names
    """
    wallet = load_wallet()
    return [f"{account.get('name')}" for account in wallet.get("accounts")]


def wallet_tuple():
    """Get account names from the local file accounts.json.

    Returns:
        list: account names
    """
    wallet = load_wallet()
    return [
        (account.get("name"), account.get("name")) for account in wallet.get("accounts")
    ]


class CMDOAccount(Account):
    def __init__(self, account) -> None:
        super().__init__()
        self.from_key(account.get("private_key"))


class Wallet:
    def __init__(self, accounts_file=f"{APP_HOME}/accounts.json") -> None:
        self.__accounts_file = accounts_file
        self.accounts = self._load_wallet()

    def _load_wallet(self):
        accounts = list()
        with open(self.__accounts_file) as f:
            local_accounts = json.loads(f.read())
            for account in local_accounts.get("accounts"):
                accounts.append(CMDOAccount(account))
        return accounts
