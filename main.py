cost = 0
extraCost = 0
done = False
shoppingList = []

print("-----| Coffee Menu |-----\n")
print("-------| Black |------------|")
print("1. Espresso..............2.50 EUR")
print("2. Americano.............3.25 EUR\n")
print("-------| White |------------|")
print("3. Cappuccino............3.00 EUR")
print("4. Latte.................3.20 EUR")
print("5. Flat White............3.50 EUR\n")

coffee_prices = {
    1: ("Espresso", 2.50),
    2: ("Americano", 3.25),
    3: ("Cappuccino", 3.00),
    4: ("Latte", 3.20),
    5: ("Flat White", 3.50)
}

extra_prices = {
    "a": ("Extra Sugar", 0.25),
    "b": ("Extra Milk", 0.50)
}

while not done:
    choice = int(input("Make your choice (1-5): "))
    if choice in coffee_prices:
        drink, price = coffee_prices[choice]
        cost += price
        shoppingList.append(f"{drink}..............{price:.2f} EUR")

        extra_added = {"a": False, "b": False}
        extraDone = False
        while not extraDone:
            print("\n-------| Extras |------------|")
            if not extra_added["a"]:
                print("A. Extra Sugar.............0.25 EUR")
            if not extra_added["b"]:
                print("B. Extra Milk...............0.50 EUR\n")
            print("N. No extras\n")

            extra = input("Would you like to add extras (a/b)? (n for no extra): ").lower()

            if extra in extra_prices:
                extra_name, extra_price = extra_prices[extra]
                extraCost += extra_price
                shoppingList.append(f"- {extra_name}..............{extra_price:.2f} EUR")
                extra_added[extra] = True
            elif extra == "n":
                extraDone = True
            else:
                print("Invalid choice, please try again")

        more = input("Would you like to order another drink (y/n): ").lower()
        if more == "n":
            done = True

    else:
        print("Invalid choice, please try again")

print("\n-----| Receipt |-----")
for item in shoppingList:
    print(item)
total = cost + extraCost
print(f"\nTotal: {total:.2f} EUR")
