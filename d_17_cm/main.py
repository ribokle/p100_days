from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
money_box = MoneyMachine()
menu_list = Menu()

while is_on:
    choice = input(f"What would you like?\n{menu_list.get_items()}\nType the name of coffee to make your selection: ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_machine.report()
        money_box.report()
    else:
        menu_item = menu_list.find_drink(choice)
        if coffee_machine.is_resource_sufficient(menu_item):
            if money_box.make_payment(menu_item.cost):
                coffee_machine.make_coffee(menu_item)

    


