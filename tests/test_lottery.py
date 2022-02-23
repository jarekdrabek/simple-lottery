from brownie import Lottery, accounts

def test_buyingCouponEveryThirdIsWinning():
    # Arrange
    testing_contract = Lottery.deploy({"from": accounts[0]})
    one_ether_in_wei = 1000000000000000000

    # Act
    testing_contract.buyCouponAndTryToWin({'from':accounts[0], 'value':one_ether_in_wei})
    testing_contract.buyCouponAndTryToWin({'from':accounts[1], 'value':one_ether_in_wei})
    testing_contract.buyCouponAndTryToWin({'from':accounts[2], 'value':one_ether_in_wei})

    account1_balance = accounts[0].balance().to("ether")
    account2_balance = accounts[1].balance().to("ether")
    account3_balance = accounts[2].balance().to("ether")

    # Assert
    assert account1_balance == 99
    assert account2_balance == 99
    assert account3_balance == 102

