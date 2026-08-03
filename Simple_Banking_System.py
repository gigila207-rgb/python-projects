account = {
    "owner": "Ali",
    "balance": 15000
}
print("""
==== BANK SYSTEM ====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")
while True:
    choice = int(input("choose: "))
    if choice == 1:
        print(account.get("balance"))

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            account["balance"] += amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > account["balance"]:
            print("Not enough money.")
        else:
            account["balance"] -= amount
            print("Withdrawal successful!")

    elif choice == 4:
        print("Thank you for using the bank!")
        break
          
    
  
  
        

  
