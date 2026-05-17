# Simple ATM System

balance = 5000

while True:

    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)

        else:
            print("Insufficient balance")

    elif choice == "3":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")