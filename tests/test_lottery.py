import pytest
from brownie import Lottery, accounts
from brownie.exceptions import VirtualMachineError

from scripts.buy_coupon_and_try_to_win import ONE_MILLION_GWEI_IN_WEI


def test_buying_coupon_every_third_is_winning():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})

    # Act
    testing_contract.buy_coupon_and_try_to_win(
        {"from": accounts[0], "value": ONE_MILLION_GWEI_IN_WEI}
    )
    testing_contract.buy_coupon_and_try_to_win(
        {"from": accounts[1], "value": ONE_MILLION_GWEI_IN_WEI}
    )
    testing_contract.buy_coupon_and_try_to_win(
        {"from": accounts[2], "value": ONE_MILLION_GWEI_IN_WEI}
    )

    account1_balance = accounts[0].balance().to("gwei")
    account2_balance = accounts[1].balance().to("gwei")
    account3_balance = accounts[2].balance().to("gwei")

    # Assert
    assert account1_balance == 99999000000
    assert account2_balance == 99999000000
    assert account3_balance == 100002000000


def test_coupon_for_more_then_one_million_gwei():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})

    # Act
    with pytest.raises(VirtualMachineError):
        testing_contract.buy_coupon_and_try_to_win(
            {"from": accounts[0], "value": ONE_MILLION_GWEI_IN_WEI + 1}
        )


def test_coupon_for_less_then_one_million_gwei():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})

    # Act
    with pytest.raises(VirtualMachineError):
        testing_contract.buy_coupon_and_try_to_win(
            {"from": accounts[0], "value": ONE_MILLION_GWEI_IN_WEI - 1}
        )
