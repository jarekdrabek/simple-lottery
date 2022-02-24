from brownie import network, accounts, Contract, config

ONE_MILLION_GWEI_IN_WEI = 1_000_000_000_000_000  # is 0.001ETH


def buy_coupon_and_try_to_win():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])
    contract_adress = config["contract"][working_network]["address"]
    lottery_contract = Contract(contract_adress)

    transaction_receipt = lottery_contract.buyCouponAndTryToWin(
        {"from": account, "value": ONE_MILLION_GWEI_IN_WEI}
    )
    print(
        f"You took part in Lottery. If you win you get the whole Lottery Pool to your address."
    )
    print(
        f"You can find it on {working_network} network etherscan: https://{working_network}.etherscan.io/tx/{transaction_receipt.txid}"
    )


def main():
    buy_coupon_and_try_to_win()
