from brownie import accounts, Lottery, network, config


def deploy_lottery():
    working_network = network.show_active()
    account = accounts.load(config["contract"][working_network]["account_name"])
    randomness = config['contract'][working_network]['dependencies']['randomness']
    vrf_coordinator = randomness['vrf_coordinator']
    keyhash = randomness['keyhash']
    request_confirmations = randomness['request_confirmations']
    subscription_id = randomness['subscription_id']

    print(f"Deploying lottery contract to {working_network} network")
    contract = Lottery.deploy(vrf_coordinator, keyhash, request_confirmations, subscription_id, {"from": account})
    print(f"Lottery Contract deployed. Contract address: {contract.address}")
    print(
        f"You can find it on {working_network} network etherscan: https://{working_network}.etherscan.io/address/{contract.address}"
    )


def main():
    deploy_lottery()
