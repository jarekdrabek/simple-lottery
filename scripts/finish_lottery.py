from brownie import network, accounts, Contract, config


def finish_lottery():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])
    contract_adress = config["contract"][working_network]["address"]
    lottery_contract = Contract(contract_adress)

    transaction_receipt = lottery_contract.finishLottery(
        {"from": account}
    )
    print(
        f"Lottery Finished. The winner will be awarded."
    )
    print(
        f"You can find your transaction on {working_network} network etherscan: https://{working_network}.etherscan.io/tx/{transaction_receipt.txid}"
    )


def main():
    finish_lottery()
