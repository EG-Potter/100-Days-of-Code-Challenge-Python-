from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

active = True

while active:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == 'off':
        '''Turns off the coffee machine'''
        active = False
    elif choice == 'report':
        '''Prints out list of relevant resources'''
        coffee_maker.report()
        money_machine.report()
    else:
        '''checks if resources are sufficient'''
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            '''If there are and the correct money inserted, drink is created'''
            coffee_maker.make_coffee(drink)


