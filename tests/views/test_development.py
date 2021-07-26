"""
Testing each network seperately because 
we'll look on each network for a specific contract.
"""
from web3 import Web3

from crypto_commando.config import NETWORKS
from crypto_commando.helpers import get_contract


def test_dev_eth_network_setup():
    ETH_MAINNET = NETWORKS[0]
    WBTC_CONTRACT = Web3.toChecksumAddress("0x2260fac5e5542a773aa44fbcfedf7c193bc2c599")
    # HTTPProvider:
    w3_eth = Web3(Web3.HTTPProvider(ETH_MAINNET.get("https_url")))
    assert w3_eth.isConnected()

    # Test if we can find the WBTC contract.
    contract = get_contract(w3_eth, WBTC_CONTRACT)
    assert contract.functions.symbol().call() == "WBTC"

    # WebsocketProvider:
    w3_eth_wss = Web3(Web3.WebsocketProvider(ETH_MAINNET.get("wss_url")))
    assert w3_eth_wss.isConnected()


def test_dev_polygon_network_setup():
    POLYGON_MAINNET = NETWORKS[1]
    # HTTPProvider:
    w3_polygon = Web3(Web3.HTTPProvider(POLYGON_MAINNET.get("https_url")))
    assert w3_polygon.isConnected()

    # WebsocketProvider:
    w3_polygon_wss = Web3(Web3.WebsocketProvider(POLYGON_MAINNET.get("wss_url")))
    assert w3_polygon_wss.isConnected()


def test_local_fork():
    LOCAL = NETWORKS[2]
    # HTTPProvider:
    w3_local = Web3(Web3.HTTPProvider(LOCAL.get("https_url")))
    assert w3_local.isConnected()

    # WebsocketProvider:
    w3_local_wss = Web3(Web3.WebsocketProvider(LOCAL.get("wss_url")))
    assert w3_local_wss.isConnected()
