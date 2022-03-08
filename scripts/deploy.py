from brownie import accounts, Lottery, network, config


def deploy_lottery():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])
    vrf_coordinator = config['contract'][working_network]['dependencies']['randomness']['vrf_coordinator']
    keyhash = config['contract'][working_network]['dependencies']['randomness']['keyhash']
    subscription_id = config['contract'][working_network]['dependencies']['randomness']['subscription_id']

    print(f"Deploying lottery contract to {working_network} network")
    contract = Lottery.deploy(vrf_coordinator, keyhash, subscription_id, {"from": account})
    print(f"Lottery Contract deployed. Contract address: {contract.address}")
    print(
        f"You can find it on {working_network} network etherscan: https://{working_network}.etherscan.io/address/{contract.address}"
    )


def main():
    deploy_lottery()
