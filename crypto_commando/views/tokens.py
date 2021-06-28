from functools import lru_cache
import json
import requests

from prompt_toolkit.completion import WordCompleter

from crypto_commando.config import EXCHANGES, TRANSACTION_TYPE


def exchange_completer():
    return [exchange for exchange in EXCHANGES]


@lru_cache
def get_tokens(site):
    try:
        response_content = requests.get(EXCHANGES[site]).content
        token_list = json.loads(response_content).get("tokens")
    except Exception as error:
        print(error)
        return

    # (t.get("symbol"), t.get("name"))

    list_for_autocomplete = []
    for t in token_list:
        list_for_autocomplete.append(t.get("symbol"))

    return list_for_autocomplete


def token_completer(name):
    WordCompleter(
        get_tokens(name),
        ignore_case=True,
    )


def transaction_type_completer():
    WordCompleter(
        TRANSACTION_TYPE,
        ignore_case=True,
    )
