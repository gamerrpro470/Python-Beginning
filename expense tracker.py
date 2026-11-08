expenses = []

while True:
    print("\n1. add expense")
    print("2. view all expenses")
    print("3. show total")
    print("4. exit")

    choice = input("choose an option: ")
    if choice == "1":
        amount = float(input("amount (Rs): "))
        category = input("category (food, transport, etc): ")
        expenses.append({"amount": amount, "category": category})
        print("expense added successfully.")

    elif choice == "2":
        for item in expenses:
            print(item["category"], "-", item["amount"])

    elif choice == "3":
        total = 0
        for item in expenses:
            total += item["amount"]
            print(f"total spent: Rs {total}")

    elif choice == "4":
        print("exiting the program...")
        break
    else:
        print("invalid choice, try again.")

        
