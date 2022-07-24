MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters / 4 + dimes / 10 + nickles / 20 + pennies / 100
    return total


def check_resources(type):
    if resources["water"] >= type["water"]:
        if resources["milk"] >= type["milk"]:
            if resources["coffee"] >= type["coffee"]:
                return True
            else:
                print("No enough coffee. Please refill")
                return False
        else:
            print("No enough milk. Please refill")
            return False
    else:
        print("No enough water. Please refill")
        return False


def transaction(moneypaid, cost):
    if moneypaid >= cost:
        change = moneypaid - cost
        change = float("{:.2f}".format(change))
        if change != 0:
            print(f"Your change is ${change}")
            return cost
        else:
            return cost
    else:
        print("Not enough money.")




MONEY = 0
working = True
while working:
    chosen = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if chosen == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${MONEY}')
    elif chosen == "espresso":
        check = check_resources(MENU["espresso"]["ingredients"])
        if check:
            paid = insert_coins()
            result = transaction(paid, MENU["espresso"]["cost"])
            MONEY += result
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
            resources["coffee"] = resources["water"] - MENU["espresso"]["ingredients"]["coffee"]
            print("Enjoy your espresso!")
    elif chosen == "latte":
        check = check_resources(MENU["latte"]["ingredients"])
        if check:
            paid = insert_coins()
            result = transaction(paid, MENU["latte"]["cost"])
            MONEY += result
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["water"] - MENU["latte"]["ingredients"]["coffee"]
            print("Enjoy your latte!")
    elif chosen == "cappuccino":
        check = check_resources(MENU["cappuccino"]["ingredients"])
        if check:
            paid = insert_coins()
            result = transaction(paid, MENU["cappuccino"]["cost"])
            MONEY += result
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["water"] - MENU["cappuccino"]["ingredients"]["coffee"]
            print("Enjoy your cappuccino!")
    elif chosen == "off":
        print("System closing.")
        working = False
    else:
        print("Invalid answer. Please try again.")




