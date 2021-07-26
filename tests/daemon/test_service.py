from web3 import Web3, HTTPProvider

from crypto_commando.daemon.service import get_contract, cvxCRV_rewardsconvex
from crypto_commando.config import NETWORKS

ETH_MAINNET = NETWORKS[0]
# HTTPProvider:
w3 = Web3(HTTPProvider(ETH_MAINNET.get("https_url")))


def test_contract():
    weth = Web3.toChecksumAddress("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    assert get_contract(w3, weth).functions.symbol().call() == "WETH"


def test_convex_cvxCRV_rewards():
    rewards = cvxCRV_rewardsconvex()
    assert isinstance(rewards, dict)
