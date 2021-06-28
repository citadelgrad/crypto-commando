#!/usr/bin/env python3
from prompt_toolkit.shortcuts.prompt import confirm
from prompt_toolkit.shortcuts import yes_no_dialog
from pyfiglet import Figlet
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator
from prompt_toolkit.shortcuts import radiolist_dialog

from crypto_commando.views.wallet import load_wallet, create_account, wallet_completer
from crypto_commando.views.tokens import (
    token_completer,
    exchange_completer,
    transaction_type_completer,
)
from crypto_commando.config import *


TITLE = "DeFi Automation"
main_menu_style = ("bg_green", "fg_black")


def is_number(text):
    return text.isdigit()


number_validator = Validator.from_callable(
    is_number,
    error_message="This input contains non-numeric characters",
    move_cursor_to_end=True,
)


def harvest():
    # TODO: Select account
    #     scheduled_menu = TerminalMenu(
    #         ["Convex >= 50cvx", "Curve 3Pool >= 40 tokens"],
    #         menu_highlight_style=main_menu_style,
    #     )
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
    # Might be better as a List.
    new_swap["exchange"] = prompt(
        "Select the exchange: ",
        completer=WordCompleter(exchange_completer, ignore_case=True),
    )
    new_swap["account"] = prompt(
        "Select your account: ",
        completer=WordCompleter(wallet_completer, ignore_case=True),
    )
    # TODO: Type of transaction: Depends on Harvest, Scheduled, RunNow.
    new_swap["transaction_type"] = prompt(
        "Transaction type: ", completer=transaction_type_completer
    )
    new_swap["swap_from"] = prompt("You Pay: ", completer=token_completer, style="")
    new_swap["swap_from_amount"] = prompt(
        f'Amount of {new_swap["swap_from"]}: ',
        validator=number_validator,
        completer=None,
    )
    new_swap["price_min"] = prompt(
        f'Price minimum {new_swap["swap_from"]}: ', validator=number_validator
    )
    new_swap["price_max"] = prompt(
        f'Price maximum {new_swap["swap_from"]}: ', validator=number_validator
    )
    new_swap["swap_from"] = prompt("You Receive: ", completer=token_completer)
    new_swap["gas_option"] = radiolist_dialog(
        title="Gas",
        text="Allows you to automate common DeFi tasks.",
        values=[
            ("trader", "trader"),
            ("fast", "fast"),
            ("standard", "standard"),
            ("custom", "custom"),
        ],
    ).run()
    if new_swap["gas_option"] == "Custom":
        new_swap["gas_option"] = prompt(f"Custom gas: ", validator=number_validator)

    confirm = yes_no_dialog(
        title="Confirm Swap", text="Do you want to save this swap?"
    ).run()

    if confirm:
        # WRITE transaction to JSON
        data = locals()
        print(data)
        print("Swap saved")

    return


def stake():
    return


def wallet():
    #     wallet_menu = TerminalMenu(
    #         ["Account: 123123 - ETH", "Account: 445445 - Polygon"],
    #         menu_highlight_style=main_menu_style,
    #     )
    return


def main():
    """
    When transaction run, they are validated at that moment.

    If you don't have enough GAS(eth, matic), tokens, or connectivity issues the tranaction will not run.
    """
    wallet = load_wallet()
    if len(wallet.get("accounts")) == 0:
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
        # Show existing wallet
        # Ability to Add or Delete Wallets.
        wallet()
    elif selected == "exit":
        return


if __name__ == "__main__":
    f = Figlet(font="slant")
    print(f.renderText("DeFi Automation"))
    main()
