#!/usr/bin/env python3
# from pyfiglet import Figlet
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import input_dialog, radiolist_dialog, yes_no_dialog
from prompt_toolkit.validation import Validator

from crypto_commando.config import *
from crypto_commando.views.tokens import (
    contract_tuple,
    exchange_tuple,
    get_tokens,
    harvest_sites,
)
from crypto_commando.views.transactions import Transaction
from crypto_commando.views.wallet import create_account, load_wallet, wallet_tuple

TITLE = "DeFi Automation"
main_menu_style = ("bg_green", "fg_black")


def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


number_validator = Validator.from_callable(
    is_float,
    error_message="This input contains non-numeric characters",
    move_cursor_to_end=True,
)


def harvest():
    harvest = dict()
    harvest["site"] = radiolist_dialog(
        title="Defi Harvest",
        text="",
        values=harvest_sites(),
    ).run()
    harvest["contract"] = radiolist_dialog(
        title="Contract",
        text="Select your account: ",
        values=contract_tuple(),
    ).run()
    harvest["minimum_amount"] = prompt(
        f"Minimum before harvesting: ",
        validator=number_validator,
        completer=None,
    )
    harvest["gas_option"] = radiolist_dialog(
        title="Gas",
        text="",
        values=[
            ("trader", "trader"),
            ("fast", "fast"),
            ("standard", "standard"),
            ("custom", "custom"),
        ],
    ).run()
    if harvest["gas_option"] == "custom":
        harvest["gas_option"] = input_dialog(
            title="Custom Gas", text="Maximum gwei:"
        ).run()
        # harvest["gas_option"] = prompt(f"Custom gas: ", validator=number_validator)
    """

    ## FARMING
    Get the contract
    Get a balance of available rewards

    Only harvest >= 50 tokens
    AND
    What's the price of gas?
    - Gas Range or immediate.
    - Standard, Fast, Trader
    AND
    Check frequency

    - Requires: Network, Wallet, ETH for fees.
    """
    return


def swap():
    new_swap = dict()
    new_swap["exchange"] = radiolist_dialog(
        title="Exchange",
        text="",
        values=exchange_tuple(),
    ).run()
    new_swap["account"] = radiolist_dialog(
        title="Account",
        text="Select your account: ",
        values=wallet_tuple(),
    ).run()
    new_swap["transaction_type"] = radiolist_dialog(
        title="Transaction",
        text="When do you want to run?",
        values=[(trans, trans) for trans in TRANSACTION_TYPE],
    ).run()
    if new_swap["transaction_type"] == "Scheduled":
        new_swap["price_min"] = prompt(
            f'Price minimum {new_swap["swap_from"]}: ', validator=number_validator
        )
        new_swap["price_max"] = prompt(
            f'Price maximum {new_swap["swap_from"]}: ', validator=number_validator
        )
    else:
        new_swap["price_slippage"] = prompt(
            f"Price slippage, for example: .01 = 1%", validator=number_validator
        )

    new_swap["swap_from"] = prompt(
        "You Pay: ",
        completer=WordCompleter(
            get_tokens(new_swap["exchange"]),
            ignore_case=True,
        ),
        style="",
    )
    new_swap["swap_from_amount"] = prompt(
        f'Amount of {new_swap["swap_from"]}: ',
        validator=number_validator,
        completer=None,
    )
    new_swap["swap_to"] = prompt(
        "You Receive: ",
        completer=WordCompleter(
            get_tokens(new_swap["exchange"]),
            ignore_case=True,
        ),
    )
    new_swap["gas_option"] = radiolist_dialog(
        title="Gas",
        text="",
        values=[
            ("trader", "trader"),
            ("fast", "fast"),
            ("standard", "standard"),
            ("custom", "custom"),
        ],
    ).run()
    if new_swap["gas_option"] == "custom":
        new_swap["gas_option"] = input_dialog(
            title="Custom Gas", text="Maximum gwei:"
        ).run()
        # new_swap["gas_option"] = prompt(f"Custom gas: ", validator=number_validator)

    confirm = yes_no_dialog(
        title="Confirm Swap", text="Do you want to save this swap?"
    ).run()

    if confirm:
        # WRITE transaction to JSON
        print(new_swap)
        transaction = Transaction()
        transaction.write_transaction(new_swap)
        print("Swap saved")

    return


def stake():
    return


def wallet():
    accounts = load_wallet()
    for counter, entry in enumerate(accounts.get("accounts")):
        print(f"Wallet #{counter}")
        print(f"  - {entry['name']}")
        print(f"    {entry['address']}")
        print(f"    {entry['network']}")


def main():
    """
    When transaction run, they are validated at that moment.

    If you don't have enough GAS(eth, matic), tokens, or connectivity issues the transaction will not run.
    """
    # f = Figlet(font="slant")
    # print(f.renderText("Crypto"))
    # print(f.renderText("Commando"))

    if len(load_wallet().get("accounts")) == 0:
        create_account()

    selected = radiolist_dialog(
        title="DeFi Automation",
        text="Allows you to automate common DeFi tasks.",
        values=[
            ("swap", "Swap tokens"),
            ("harvest", "Harvest"),
            # ("stake", "Stake"),
            ("wallet", "Wallet"),
            ("exit", "Exit"),
        ],
    ).run()

    if selected == "harvest":
        harvest()
    elif selected == "swap":
        swap()
    elif selected == "stake":
        stake()
    elif selected == "wallet":
        # Ability to Add or Delete Wallets.
        wallet()
    elif selected == "exit":
        return
