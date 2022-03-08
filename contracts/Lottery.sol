// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;


import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract Lottery is VRFConsumerBaseV2 {
    VRFCoordinatorV2Interface COORDINATOR;
    bytes32 keyHash;
    uint64 subscriptionId;

    address public owner;
    address payable[] public couponBuyers;
    address payable public winner;
    uint256 public randomNumber;

    event RequestedRandomness(uint256 requestId);

    constructor(address _vrfCoordinator, bytes32 _keyHash, uint64 _subscriptionId) VRFConsumerBaseV2(_vrfCoordinator) {
        COORDINATOR = VRFCoordinatorV2Interface(_vrfCoordinator);
        keyHash = _keyHash;
        subscriptionId = _subscriptionId;
        owner = msg.sender;
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
        uint16 requestConfirmations = 3;
        uint32 callbackGasLimit = 100000;
        uint32 numWords = 1;
        uint256 requestId = COORDINATOR.requestRandomWords(
        keyHash,
        subscriptionId,
        requestConfirmations,
        callbackGasLimit,
        numWords
        );
        emit RequestedRandomness(requestId);
    }

    function fulfillRandomWords(uint256, /* requestId */ uint256[] memory randomWords) internal override {
        randomNumber = randomWords[0];
        uint256 indexOfWinner = randomNumber % couponBuyers.length;
        winner = couponBuyers[indexOfWinner];
        returnTheWinningPool();
        couponBuyers = new address payable[](0);
    }

    function returnTheWinningPool() private {
        winner.transfer(address(this).balance);
    }
}
