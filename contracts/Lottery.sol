// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;


import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract Lottery is VRFConsumerBaseV2 {
    VRFCoordinatorV2Interface COORDINATOR;
    LinkTokenInterface LINKTOKEN;
    address vrfCoordinator = 0x6168499c0cFfCaCD319c818142124B7A15E857ab;
    address link = 0x01BE23585060835E02B77ef475b0Cc51aA1e0709;
    bytes32 keyHash = 0xd89b2bf150e3b9e13446986e571fb9cab24b13cea0a43ea20a6049a85cc807cc;
    uint32 callbackGasLimit = 100000;
    uint16 requestConfirmations = 3;
    uint32 numWords =  2;
    uint64 subscriptionId = 638;

    constructor() VRFConsumerBaseV2(vrfCoordinator) {
        COORDINATOR = VRFCoordinatorV2Interface(vrfCoordinator);
        LINKTOKEN = LinkTokenInterface(link);
        owner = msg.sender;
    }

    address public owner;
    address payable[] public couponBuyers;
    address payable public winner;
    uint256 public randomNumber;


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
        COORDINATOR.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );

    }

    function fulfillRandomWords(uint256, /* requestId */ uint256[] memory randomWords) internal override {
        randomNumber = randomWords[0];
        uint256 indexOfWinner = randomNumber % couponBuyers.length;
        winner = couponBuyers[indexOfWinner];
        returnTheWinningPool();
        couponBuyers = new address payable[](0);

    }
}
