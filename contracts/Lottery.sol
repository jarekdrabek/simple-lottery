// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

contract Lottery {

    uint256 private counter;

    constructor() {
        counter = 0;
    }

    function isWinningCoupon() private view returns (bool) {
        return counter % 3 == 0;
    }

    function returnTheWinningPool() private {
        payable(msg.sender).transfer(address(this).balance);
    }

    function buyCouponAndTryToWin() public payable {
        counter++;
        if (isWinningCoupon()) {
            returnTheWinningPool();
        }
    }
}