from brownie import Contract, network, config, Lottery


def get_the_winner_address():
    contract_adress = config["contract"][network.show_active()]["address"]
    lottery_contract = Contract.from_abi('Lottery', contract_adress, Lottery.abi)

    winner_address = lottery_contract.winner()
    print(
        f"The winner is {winner_address}"
    )


def main():
    get_the_winner_address()
