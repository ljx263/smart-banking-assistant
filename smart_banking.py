# Simple Smart Banking System

accounts = {
    "A": 0,
    "B": 0
}

history = []


def show_balance():

    print("\nBalances:")

    for acc in accounts:
        print(acc, ":", "$" + str(accounts[acc]))


def deposit():

    account = input("Which account to deposit into? (A/B): ").upper()

    if account not in accounts:
        print("Invalid account")
        return

    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        return

    accounts[account] = accounts[account] + amount

    message = "Deposited $" + str(amount) + " into Account " + account

    history.append(message)

    print("Deposit successful")


def withdraw():

    account = input("Which account to withdraw from? (A/B): ").upper()

    if account not in accounts:
        print("Invalid account")
        return

    amount = float(input("Enter amount: "))

    if amount > accounts[account]:
        print("Not enough money")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    # Simple fraud check
    if amount >= 10000:
        print("Large withdrawal detected")

    confirm = input("Type YES to continue: ")

    if confirm != "YES":
        print("Transaction cancelled")
        return

    accounts[account] = accounts[account] - amount

    message = "Withdrew $" + str(amount) + " from Account " + account

    history.append(message)

    print("Withdrawal successful")


def transfer():

    from_acc = input("Transfer from: ").upper()
    to_acc = input("Transfer to: ").upper()

    if from_acc not in accounts or to_acc not in accounts:
        print("Invalid account")
        return

    amount = float(input("Amount to transfer: "))

    if amount > accounts[from_acc]:
        print("Insufficient funds")
        return

    accounts[from_acc] = accounts[from_acc] - amount
    accounts[to_acc] = accounts[to_acc] + amount

    message = (
        "Transferred $" + str(amount)
        + " from " + from_acc
        + " to " + to_acc
    )

    history.append(message)

    print("Transfer successful")


def view_history():

    print("\nTransaction History")

    if len(history) == 0:
        print("No transactions yet")

    else:
        for item in history:
            print(item)


while True:

    print("\n--- SMART BANKING SYSTEM ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Show Balances")
    print("5. View Transaction History")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdraw()

    elif choice == "3":
        transfer()

    elif choice == "4":
        show_balance()

    elif choice == "5":
        view_history()

    elif choice == "6":
        print("Program ended")
        break

    else:
        print("Invalid option")
