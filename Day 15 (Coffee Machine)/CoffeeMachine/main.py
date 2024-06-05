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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_report(resource_dict, money_balance):
    """Generates a resource report for the coffee machine and returns it formatted to the user"""
    water = resource_dict["water"]
    milk = resource_dict["milk"]
    coffee = resource_dict["coffee"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money_balance}"


def resources_sufficient(order):
    """Compares the available resources against the order requirements and returns True or False"""
    if order == "latte" or order == "cappuccino":
        water_resource = resources["water"]
        water_req = MENU[order]["ingredients"]["water"]
        coffee_resource = resources["coffee"]
        coffee_req = MENU[order]["ingredients"]["coffee"]
        milk_resource = resources["milk"]
        milk_req = MENU[order]["ingredients"]["milk"]

        if water_resource < water_req:
            print("Sorry. There is not enough water.")
            return False
        elif milk_resource < milk_req:
            print("Sorry. There is not enough milk.")
            return False
        elif coffee_resource < coffee_req:
            print("Sorry. There is not enough coffee.")
            return False
        else:
            return True
    else:
        water_resource = resources["water"]
        water_req = MENU[order]["ingredients"]["water"]
        coffee_resource = resources["coffee"]
        coffee_req = MENU[order]["ingredients"]["coffee"]

        if water_resource < water_req:
            print("Sorry. There is not enough water.")
            return False
        elif coffee_resource < coffee_req:
            print("Sorry. There is not enough coffee.")
            return False
        else:
            return True


def process_coins(ins_quarters, ins_dimes, ins_nickels, ins_pennies):
    """Processes the coins the user inserted and return the total amount of the coins
     or insufficient coins message to the user"""
    tot_quarters = ins_quarters * 0.25
    tot_dimes = ins_dimes * 0.1
    tot_nickels = ins_nickels * 0.05
    tot_pennies = ins_pennies * 0.01
    tot_inserted = tot_quarters + tot_dimes + tot_nickels + tot_pennies
    return tot_inserted


def update_resource(order):
    """Subtracts the resources used for a successful transaction from the machine resources"""
    water_used = MENU[order]["ingredients"]["water"]
    coffee_used = MENU[order]["ingredients"]["coffee"]

    resources["water"] = resources["water"] - water_used
    resources["coffee"] = resources["coffee"] - coffee_used

    if order == "latte" or order == "cappuccino":
        milk_used = MENU[order]["ingredients"]["milk"]
        resources["milk"] = resources["milk"] - milk_used


machine_on = True

while machine_on:
    # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice == "off":
        machine_on = False
    # TODO: 3. Print report.
    elif user_choice == "report":
        print(resource_report(resource_dict=resources, money_balance=profit))
    # TODO: 4. Check resources sufficient?
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        resources_available = resources_sufficient(order=user_choice)
        if resources_available:
            # TODO: 5. Process coins.
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_amount = process_coins(quarters, dimes, nickels, pennies)

            # TODO: 6. Check transaction successful?
            cost = MENU[user_choice]["cost"]
            if total_amount >= cost:
                profit += cost
                if total_amount > cost:
                    change = round(total_amount - cost, 2)
                    print(f"Here is ${change} in change.")
                # TODO: 7. Make coffee
                update_resource(user_choice)
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
