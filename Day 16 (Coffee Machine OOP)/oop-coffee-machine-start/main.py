from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

# TODO 1: prompt user for choice and repeat the prompt with every completed run
is_on = True

while is_on:

    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    # TODO 2: Turn off machine by entering prompt "off"
    if choice == "off":
        is_on = False
    # TODO 3: Generate a report of the machine resources and profit balance
    elif choice == "report":
        machine.report()
        money.report()
    # TODO 4: Check the whether the resources are sufficient to make the order
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            # TODO 5: Process coins if the resources are sufficient
            if money.make_payment(drink.cost):
                # If payment successful, add the cost of the drink to the machine money and deduct resources
                machine.make_coffee(drink)

