# simple-lottery
Simple lottery blockchain application. This project is working with the Rinkeby Ethereum testnet.

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
brownie run scripts/buy_coupon_and_try_to_win.py --network rinkeby
```


### How to run contract tests

Executing tests
```
brownie test
```

### How to deploy you own version of Lottery:
Deploying to Rinkeby Ethereum network.
Use my Infura project id to deploy to Rinkeby network
```
export WEB3_INFURA_PROJECT_ID=3b60db32abff40358b27faee00f6cc83
```
```
brownie run scripts/deploy.py --network rinkeby
```



