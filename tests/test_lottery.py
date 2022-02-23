import pytest
from brownie import Lottery, accounts
from brownie.exceptions import VirtualMachineError

ONE_MILLION_GWEI_IN_WEI = 1000000000000000  # is 0.001ETH

def test_buying_coupon_every_third_is_winning():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})


    # Act
    testing_contract.buyCouponAndTryToWin(
        {"from": accounts[0], "value": ONE_MILLION_GWEI_IN_WEI}
    )
    testing_contract.buyCouponAndTryToWin(
        {"from": accounts[1], "value": ONE_MILLION_GWEI_IN_WEI}
    )
    testing_contract.buyCouponAndTryToWin(
        {"from": accounts[2], "value": ONE_MILLION_GWEI_IN_WEI}
    )

    account1_balance = accounts[0].balance().to("ether")
    account2_balance = accounts[1].balance().to("ether")
    account3_balance = accounts[2].balance().to("ether")

    # Assert
    assert account1_balance == 99
    assert account2_balance == 99
    assert account3_balance == 102


def test_coupon_for_more_then_one_million_gwei():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})

    # Act
    with pytest.raises(VirtualMachineError):
        testing_contract.buyCouponAndTryToWin(
            {"from": accounts[0], "value": ONE_MILLION_GWEI_IN_WEI+1}
        )


def test_coupon_for_less_then_one_million_gwei():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})

    # Act
    with pytest.raises(VirtualMachineError):
        testing_contract.buyCouponAndTryToWin(
            {"from": accounts[0], "value": ONE_MILLION_GWEI_IN_WEI-1}
        )
