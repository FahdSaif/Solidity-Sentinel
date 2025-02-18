pragma solidity ^0.8.0;

contract Vulnerable {
    function withdraw(uint amount) public {
        // This pattern could be dangerous
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");
    }
}
