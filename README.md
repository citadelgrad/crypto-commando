# defi-automation

Automate farming and staking of DeFi assets. Self Custodial.

## Update #1

Here's what our team is working on so far:

**Name**: Personal Defi Automation

**Description**: Automate farming, swapping, and staking of DeFi assets. Self Custodial.

**Github**: https://github.com/citadelgrad/defi-automation

**Development progress**

Most of my development so far has been focused on prototyping in web3/solidity since I'm completely new to the language.

**Idea**: It takes a lot of work to regularly check on farming and staking stake rewards across a dozen different applications. I'm often farming late in the evening because I'm trying to do this transactions when gas is cheaper. But I'd also love to automate certain tasks.

A menu-driven command line tool to allow the user to automate farming, swapping, and staking of assets. The application runs locally on their secured personal computer or server. The user will be able to schedule checking their farms/stakes regular, set limits on gas, and only farm tokens if they meet minimums. Schedule swaps based on price, gas, etc. Schedule staking of tokens.

My focus for this hackathon is to get the auto farming and scheduled swapping implemented. I hope to make this available on both ETH and Polygon.

- Probably use Token lists https://tokenlists.org/
- Possibly initial targets are to farm from Curve, Sushi, Convex
- Swap on 1inch, uniswap, paraswap
- I'd like to also try go package these swaps and submit them on the Flashbots network

**Blockers**:

- Time: I'd love help.
- I'm doing the project solo. I'm not opposed to getting help but I just don't want to spend a bunch of time looking for and vetting a teammate. Everything's going to be written in Python using web3py. I'm considering using the Cement CLI app framework. https://cement.readthedocs.io/en/stable-2.0.x/
- It's going to be important to find the best ways to secure the wallet private keys. Options: running the app in docker, encrypting the private key, storing the private key in the cloud, sharing the private key, running the app in the cloud, Open Zeppelin Defender.

Public URL: https://showcase.ethglobal.co/hackmoney2021/personal-defi-automation
