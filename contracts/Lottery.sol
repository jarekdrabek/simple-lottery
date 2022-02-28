// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;


contract Lottery {
    address public owner;
    address payable[] public couponBuyers;
    address payable public winner;

    constructor()  {
        owner = msg.sender;
    }

    function returnTheWinningPool() private {
        winner.transfer(address(this).balance);
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    modifier isCouponPrice() {
        //Coupon price = 0.001ETH
        uint256 couponPriceInWei = 1000000000000000;
        require(
            couponPriceInWei == msg.value,
            "You need to pay exactly 0.001ETH for coupon"
        );
        _;
    }

    function buyCoupon() public payable isCouponPrice {
        couponBuyers.push(payable(msg.sender));
    }

    function finishLottery() public payable onlyOwner {
        uint256 randomNumber = 17;
        uint256 indexOfWinner = randomNumber % couponBuyers.length;
        winner = couponBuyers[indexOfWinner];
        returnTheWinningPool();
        couponBuyers = new address payable[](0);
    }
}
