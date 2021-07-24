import json
import requests
from eth_account import Account
import secrets

from crypto_commando.config import ETHERSCAN_API_KEY


def test_account():
    """
    Create a temp private key for testing.
    """
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    print("SAVE BUT DO NOT SHARE THIS:", private_key)
    acct = Account.from_key(private_key)
    print("Address:", acct.address)


def get_contract_abi(contract):
    response = requests.get(
        f"https://api.etherscan.io/api?module=contract&action=getabi&address={contract}&apikey={ETHERSCAN_API_KEY}"
    )
    data = json.loads(response.text)
    if data.get("message") == "OK":
        return data.get("result")
    else:
        raise "Unable to get contract ABI"
