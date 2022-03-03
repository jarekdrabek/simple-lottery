# Simple Lottery
Simple lottery blockchain application. This project is working with the Rinkeby Ethereum testnet. 
You can interact with the lottery executing commands in console (see below). 

## How it works
You can buy a lottery coupon for 0.001ETH.
The Owner(the address that deployed the lottery) of the lottery can finish it at any time.
The process of finishing is drowing the winning coupon and sending all the collected money to the address that bought it.
The more coupons you buy, the bigger chance you have to win.

## How it works technically
We collect the addresses that bought the coupon in an **couponBuyers** array. Every purchase is another 
element in the array.  

After the owner of the lottery finish the lottery we use [chainlink VRF v2](https://docs.chain.link/docs/get-a-random-number/) to get a random number. 
Then this random number is [mod](https://en.wikipedia.org/wiki/Modulo_operation) by the array length. The result is the index of the winner in the **couponBuyers** array.   


## Installation and running

### Requirements:
you need to have `Python 3.9` and [brownie](https://eth-brownie.readthedocs.io/en/stable/install.html) installed


### Prerequisuites

Installing project dependencies:
```
pip install -r requirements.txt
```

In order to interact with Rinkeby Ethereum testnet you need to create Rinkeby account 
(you need to provide private key to your Metamask account - PLEASE DON'T USE THE ONE WITH REAL MONEY ON IT!)
```
brownie accounts new rinkeby-account1 
```

### How to take part in the current Lottery:
```
brownie run scripts/buy_coupon.py --network rinkeby
```


### How to run contract tests

Executing tests
```
brownie test
```

### How to deploy you own version of Lottery and take part in it:
Deploying to Rinkeby Ethereum network.
Use my Infura project id to deploy to Rinkeby network
```
export WEB3_INFURA_PROJECT_ID=3b60db32abff40358b27faee00f6cc83
```
```
brownie run scripts/deploy.py --network rinkeby
```

you should see message similar to following:

> Lottery Contract deployed. Contract address: 0xA7fEe2a153C32e28914226D1CC9CDa27FA9194a9
> 
> You can find it on rinkeby network etherscan: https://rinkeby.etherscan.io/address/0xA7fEe2a153C32e28914226D1CC9CDa27FA9194a9


Coppy the contract address and paste in `brownie-config.yaml` file similarly like below
```
contract:
  rinkeby:
    address: '0xA7fEe2a153C32e28914226D1CC9CDa27FA9194a9' 
```

You can now take part in your own Lottery executing:

```
brownie run scripts/buy_coupon.py --network rinkeby
```

### How to finish your deployed Lottery and figure out who won:

