require("@nomiclabs/hardhat-waffle");

module.exports = {
  solidity: "0.7.6",
  networks: {
    hardhat: {
      forking: {
        url: process.env.ALCHEMY_MAINNET_HTTPS,
        blockNumber: 12720945
      }
    }
  }
};

