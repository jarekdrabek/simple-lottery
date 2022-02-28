from brownie import network, accounts, Contract, config

ONE_MILLION_GWEI_IN_WEI = 1_000_000_000_000_000  # is 0.001ETH


def buy_coupon():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])
    contract_adress = config["contract"][working_network]["address"]
    lottery_contract = Contract(contract_adress)

    transaction_receipt = lottery_contract.buyCoupon(
        {"from": account, "value": ONE_MILLION_GWEI_IN_WEI}
    )
    print(
        f"You took part in Lottery."
    )
    print(
        f"You can find your transaction on {working_network} network etherscan: https://{working_network}.etherscan.io/tx/{transaction_receipt.txid}"
    )


def main():
    buy_coupon()
