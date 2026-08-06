
    inventory = {
    "Sword": 1,
    "Potion": 5,
    "Gold": 200,
    "Shield": 1
}
print("""
1. Show Inventory
2. Pick Up Item
3. Use Item
4. Add Gold
5. Exit
""")
while True:
    choose = int(input("choose an operation ="))

    if choose == 1:
        for item, count in inventory.items():
            print(f"{item}: {count}")

    elif choose == 2:
        item = input("What item did you pick up? ")
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
        print(f"You picked up 1 {item}.")

    elif choose == 3:
        item = input("What item do you want to use? ")
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
            print(f"You used one {item}.")
            print(f"{item} left: {inventory[item]}")
        else:
            print("You don't have that item.")

    elif choose == 4:
        amount = int(input("How much gold did you find? "))
        if amount > 0:
            inventory["Gold"] += amount
            print(f"You found {amount} gold!")
            print(f"Total gold: {inventory['Gold']}")
        else:
            print("Invalid amount.")

    elif choose == 5:
        print("Thanks for playing!")
        break

    
    
