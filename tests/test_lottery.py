import pytest
from brownie import Lottery, accounts, VRFCoordinatorV2Mock, config, network
from brownie.exceptions import VirtualMachineError
from brownie.network.web3 import Web3



def test_lottery_workflow():
    # Arrange
    lottery_owner_account = accounts[0]
    first_player_account = accounts[1]
    second_player_account = accounts[2]
    third_player_account = accounts[3]
    lottery_contract, vrf_coordinator = __deploy_and_get_lottery_contract_and_dependencies(lottery_owner_account)

    #Act
    lottery_contract.buyCoupon({"from": first_player_account, "value": Web3.toWei(0.001, 'ether')})
    lottery_contract.buyCoupon({"from": second_player_account, "value": Web3.toWei(0.001, 'ether')})
    lottery_contract.buyCoupon({"from": third_player_account, "value": Web3.toWei(0.001, 'ether')})

    random_result = 4
    __finish_lottery_with_given_random_result(lottery_contract, lottery_owner_account, vrf_coordinator, random_result)

    #Assert
    assert lottery_contract.winner() == second_player_account.address
    assert lottery_contract.balance() == 0
    assert first_player_account.balance() == Web3.toWei(99.999, 'ether')
    assert second_player_account.balance() == Web3.toWei(100.002, 'ether')
    assert third_player_account.balance() == Web3.toWei(99.999, 'ether')


def test_deployer_can_finish_lottery():
    # TODO: to be implemented
    # Arrange
    # Act
    # Assert
    pass


def test_not_deployer_cannot_finish_lottery():
    # TODO: to be implemented
    # Arrange
    # Act
    # Assert
    pass


def test_coupon_for_more_then_one_million_gwei():
    # Arrange
    deployer_account = accounts[0]
    testing_contract,_ = __deploy_and_get_lottery_contract_and_dependencies(deployer_account)


    # Act and Assert
    with pytest.raises(VirtualMachineError):
        testing_contract.buyCoupon(
            {"from": deployer_account, "value": Web3.toWei(0.001, 'ether') + 1}
        )


def test_coupon_for_less_then_one_million_gwei():
    # Arrange
    deployer_account = accounts[0]
    testing_contract,_ = __deploy_and_get_lottery_contract_and_dependencies(deployer_account)

    # Act and Assert
    with pytest.raises(VirtualMachineError):
        testing_contract.buyCoupon({"from": deployer_account, "value": Web3.toWei(0.001, 'ether') - 1})


def __deploy_and_get_lottery_contract_and_dependencies(deploying_account):
    keyhash = '0xd89b2bf150e3b9e13446986e571fb9cab24b13cea0a43ea20a6049a85cc807cc'

    vrf_coordinator = VRFCoordinatorV2Mock.deploy(0, 0, {"from": deploying_account})
    subscription_id = vrf_coordinator.createSubscription().return_value

    lottery_contract = Lottery.deploy(
        vrf_coordinator,
        keyhash,
        subscription_id,
        {"from": accounts[0]},
    )
    return lottery_contract, vrf_coordinator


def __finish_lottery_with_given_random_result(lottery_contract, finisher_account, vrf_coordinator, random_result):
    request_id = __finish_lottery_contract(lottery_contract, finisher_account)
    vrf_coordinator.fulfillRandomWords(
        request_id, lottery_contract.address, random_result
    )


def __finish_lottery_contract(testing_contract, account):
    tx = testing_contract.finishLottery({"from": account})
    request_id = tx.events["RequestedRandomness"]["requestId"]
    return request_id
