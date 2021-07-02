from functools import lru_cache
import json
import requests

from prompt_toolkit.completion import WordCompleter

from crypto_commando.config import EXCHANGES, TRANSACTION_TYPE


def exchange_tuple():
    return [(name, name) for name, uri in EXCHANGES.items()]


def exchange_completer():
    return list(EXCHANGES)


@lru_cache
def get_tokens(site):
    """Get a list of ticker symbols from an exchange's tokenlist.

    Args:
        site (str): A short name of a defi crypto exchange.

    Returns:
        [list]: list of token symbols.
    """
    try:
        response_content = requests.get(EXCHANGES[site]).content
        token_list = json.loads(response_content).get("tokens")
    except Exception as error:
        print(error)
        return

    list_for_autocomplete = []
    for t in token_list:
        list_for_autocomplete.append(t.get("symbol"))

    return list_for_autocomplete


def harvest_sites():
    return ["Curve", "Badger", "Convex", "Sushi"]


def contract_tuple():
    return ["Curve", "Badger", "Convex", "Sushi"]
