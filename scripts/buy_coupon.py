from brownie import network, accounts, Contract, config
from brownie.network.web3 import Web3


def buy_coupon():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])
    contract_adress = config["contract"][working_network]["address"]
    lottery_contract = Contract(contract_adress)

    transaction_receipt = lottery_contract.buyCoupon(
        {"from": account, "value": Web3.toWei(0.001, 'ether')}
    )
    print(
        f"You took part in Lottery."
    )
    print(
        f"You can find your transaction on {working_network} network etherscan: https://{working_network}.etherscan.io/tx/{transaction_receipt.txid}"
    )


def main():
    buy_coupon()
