import os

from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider
from web3.auto.infura import w3
from flashbots import flashbot
from eth_account.account import Account

WEB3_INFURA_PROJECT_ID = os.environ.get("WEB3_INFURA_PROJECT_ID")
WEB3_INFURA_API_SECRET = os.environ.get("WEB3_INFURA_API_SECRET")

# If you don't have a valid ETH mainnet connection this assert will fail.
assert w3.isConnected()

# pyfiglet font options: https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts

HOME = os.environ["HOME"]
APP_HOME = f"{HOME}/.defi"

TRANSACTION_TYPE = ["Scheduled", "RunNow"]


# RPC urls are specific to this application.
NETWORKS = [
    dict(
        name="Ethereum",
        symbol="ETH",
        chain_id=1,
        network_type="MAINNET",
        block_explorer="https://etherscan.io",
        rpc_url=f"https://mainnet.infura.io/v3/{WEB3_INFURA_PROJECT_ID}",
    ),
    dict(
        name="Polygon",
        symbol="MATIC",
        chain_id=137,
        network_type="MAINNET",
        block_explorer="https://polygonscan.com/",
        rpc_url=f"https://polygon-mainnet.infura.io/v3/{WEB3_INFURA_PROJECT_ID}",
    ),
]

""" Used for Autocomplete """
NETWORKS_SIMPLE = [
    f"{network.get('name')} - {network.get('network_type')}" for network in NETWORKS
]

EXCHANGES = {
    "aave": "http://tokenlist.aave.eth.link",
    "compound": "https://raw.githubusercontent.com/compound-finance/token-list/master/compound.tokenlist.json",
    "gemini": "https://www.gemini.com/uniswap/manifest.json",
    "1inch": "http://tokens.1inch.eth.link",
    "kyber": "https://api.kyber.network/tokenlist",
    "uniswap": "https://gateway.ipfs.io/ipns/tokens.uniswap.org",
    "uniswap-30k-pairs": "https://raw.githubusercontent.com/jab416171/uniswap-pairtokens/master/uniswap_pair_tokens.json",
    "zapper": "https://zapper.fi/api/token-list",
}

STAKING = {"yearn": "https://yearn.science/static/tokenlist.json"}
