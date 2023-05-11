from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_object = CoffeeMaker()
menu_object = Menu()
money_machine_object = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"​What would you like? ({menu_object.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_object.report()
        money_machine_object.report()
    else:
        drink = menu_object.find_drink(choice)
        if coffee_maker_object.is_resource_sufficient(drink):
            if money_machine_object.make_payment(drink.cost):
                coffee_maker_object.make_coffee(drink)