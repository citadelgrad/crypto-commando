import os

from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from flashbots import flashbot
from web3 import HTTPProvider, Web3

ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY")

ETH_HTTP_API = os.environ.get("ALCHEMY_MAINNET_HTTPS")
ETH_WSS_API = os.environ.get("ALCHEMY_MAINNET_WSS")

POLYGON_HTTP_API = os.environ.get("ALCHEMY_POLYGON_MAINNET_HTTPS")
POLYGON_WSS_API = os.environ.get("ALCHEMY_POLYGON_MAINNET_WSS")

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
        https_url=ETH_HTTP_API,
        wss_url=ETH_WSS_API,
    ),
    dict(
        name="Polygon",
        symbol="MATIC",
        chain_id=137,
        network_type="MAINNET",
        block_explorer="https://polygonscan.com/",
        https_url=POLYGON_HTTP_API,
        wss_url=POLYGON_WSS_API,
    ),
    dict(
        name="TestLocal",
        symbol="ETH",
        chain_id=31337,
        network_type="TESTNET",
        block_explorer="https://etherscan.io",
        https_url="http://127.0.0.1:8545",
        wss_url="ws://127.0.0.1:8545",
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
