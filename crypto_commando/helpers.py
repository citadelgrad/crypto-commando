from eth_account import Account
import secrets


def test_account():
    """
    Create a temp private key for testing.
    """
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    print("SAVE BUT DO NOT SHARE THIS:", private_key)
    acct = Account.from_key(private_key)
    print("Address:", acct.address)
