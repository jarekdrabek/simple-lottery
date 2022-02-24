# simple-lottery
Simple lottery blockchain application. This project is working with the Rinkeby Ethereum testnet.

You can buy a lottery coupon for 0.001ETH and try to win. 

if you are not lucky, your money will be added to the winning pool.

If you are lucky you will get the whole collected winning pool.
After that the lottery start over.

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

> Lottery Contract deployed. Contract address: 0x7D09cE020034AB069EC1723ED4518E4db0Cba1BE

Coppy the contract address and paste in `brownie-config.yaml` file similarly like below
```
contract:
  rinkeby:
    address: '0x7D09cE020034AB069EC1723ED4518E4db0Cba1BE' 
```

You can now take part in your own Lottery executing:

```
brownie run scripts/buy_coupon_and_try_to_win.py --network rinkeby
```

