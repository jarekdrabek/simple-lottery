from brownie import accounts, Lottery, network


def deploy_lottery():
    # TODO: make account configurable
    working_network = network.show_active()
    account = accounts.load("rinkeby-account1")
    print(f"Deploying lottery contract to {working_network} network")
    contract = Lottery.deploy({"from": account})
    print(f"Lottery Contract deployed. Contract address: {contract.address}")
    print(
        f"You can find it on {working_network} network etherscan: https://{working_network}.etherscan.io/address/{contract.address}"
    )


def main():
    deploy_lottery()
