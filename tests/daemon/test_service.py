from web3 import Web3

from crypto_commando.daemon.service import contract


def test_contract():
    weth = Web3.toChecksumAddress("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    assert contract(weth)
