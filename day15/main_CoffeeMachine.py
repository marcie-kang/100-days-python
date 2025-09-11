MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

is_operation = True
total_sales = 0


def check_resource(ordered_menu, current_resource):
    for resource in current_resource:
        if resource in MENU[ordered_menu]["ingredients"]:
            if current_resource[resource] < MENU[ordered_menu]["ingredients"][resource]:
                print(f"Sorry there is not enough {resource}.")

                return False

    return True


def check_money(ordered_menu):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.01) + (pennies * 0.05)

    if MENU[ordered_menu]["cost"] < total:
        change = total - MENU[ordered_menu]["cost"]
        print(f"Here is ${round(change, 3)} in change")
        print(f"Here is your {ordered_menu} Engoy!")
    elif MENU[ordered_menu]["cost"] == total:
        print(f"Here is your {ordered_menu} Engoy!")
    else:
        print(f"Sorry, that's not enough money. Money is refunded.")

        return False

    return True


while is_operation:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        is_operation = False
    elif order == "resource":
        print(
            f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: ${total_sales}")
    else:
        final_resource = check_resource(order, resources)
        final_money = False

        if final_resource:
            final_money = check_money(order)

            resources["water"] -= MENU[order]["ingredients"]["water"]
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

            if "milk" in MENU[order]["ingredients"]:
                resources["milk"] -= MENU[order]["ingredients"]["milk"]

        if final_money:
            total_sales += MENU[order]["cost"]
