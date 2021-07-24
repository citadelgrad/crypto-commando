from web3 import Web3

from crypto_commando.config import NETWORKS


def test_dev_eth_network_setup():
    ETH_MAINNET = NETWORKS[0]
    # HTTPProvider:
    w3_eth = Web3(Web3.HTTPProvider(ETH_MAINNET.get("https_url")))
    # WebsocketProvider:
    w3_eth = Web3(Web3.WebsocketProvider(ETH_MAINNET.get("wss_url")))

    assert w3_eth.isConnected()


def test_dev_polygon_network_setup():
    POLYGON_MAINNET = NETWORKS[1]
    # HTTPProvider:
    w3_polygon = Web3(Web3.HTTPProvider(POLYGON_MAINNET.get("https_url")))
    # WebsocketProvider:
    w3_polygon = Web3(Web3.WebsocketProvider(POLYGON_MAINNET.get("wss_url")))

    assert w3_polygon.isConnected()
