from brownie import accounts, Lottery, network, config


def deploy_lottery():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])

    print(f"Deploying lottery contract to {working_network} network")
    contract = Lottery.deploy({"from": account})
    print(f"Lottery Contract deployed. Contract address: {contract.address}")
    print(
        f"You can find it on {working_network} network etherscan: https://{working_network}.etherscan.io/address/{contract.address}"
    )


def main():
    deploy_lottery()
