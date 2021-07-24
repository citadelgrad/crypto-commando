# Crypto Commando

**Start Infomercial**

Are you a DeFi degen earning crazy yields? Does it take you hours each week to Harvest, Swap, and Re-Stake those earnings? Are you tired of stay up late to save on gas? Is your bae mad at you, because you are constantly checking prices to maximize your swaps? Hella slow transaction confirmations got you down?

Crypto Commando cli make it easy to schedule your Harvests, Swaps, and Staking.

- CMDO schedules when gas is cheap
- CMDO checks prices for you and makes that sweet swap when the time is right.
- CMDO restakes your bags to maximize your yields!

Get your life back with Crypto Commandoooooo....

Limited time offer only ~~$29.99~~, if you buy today it's freeeeee.

**End Infomercial**

After you've installed Crypto Commando, open a terminal and run `cmdo` to start the application.

Application Requirements:

- Python 3.9

Supported Platforms:

- Mac OS
- Linux
- Window's with WSL or Git-Bash

---

## Developer Setup

Start local fork of Ethereum

```
npx hardhat node
```

Preferably, use the Hardhat shorthand.

```bash
npm i -g hardhat-shorthand
hh console
```

## Boring details

Automate farming, swapping, and staking of DeFi assets. Self Custodial.

**CMO is pre-production software does not work.**

## Tech stuff

Transactions Data Model

```json
NOW_TRANSACTION = {
    "exchange": "kyber",
    "account": "Scott",
    "transaction_type": "RunNow",
    "swap_from": "BAT",
    "swap_from_amount": "100",
    "price_min": ".75",
    "price_max": "1.2",
    "swap_to": "USDC",
    "gas_option": "fast",
    "price_slippage": ".01",
}
```

```json
SCHEDULED_TRANSACTION = {
    "exchange": "kyber",
    "account": "Scott",
    "transaction_type": "RunNow",
    "swap_from": "BAT",
    "swap_from_amount": "100",
    "price_min": ".75",
    "price_max": "1.2",
    "swap_to": "USDC",
    "gas_option": "fast",
}
```

### Token List

Format of the token list.

```json
{
  "address": "0x0327112423F3A68efdF1fcF402F6c5CB9f7C33fd",
  "chainId": 1,
  "name": "PieDAOBTC++",
  "symbol": "BTC",
  "decimals": 18,
  "logoURI": "https://tokens.1inch.exchange/0x0327112423f3a68efdf1fcf402f6c5cb9f7c33fd.png"
}
```
