from brownie import Contract, network, config


def get_the_winner_address():
    lottery_contract_adress = config["contract"][network.show_active()]["address"]
    lottery_contract = Contract(lottery_contract_adress)

    winner_address = lottery_contract.winner()
    print(
        f"The winner is {winner_address}"
    )


def main():
    get_the_winner_address()
