from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_machine_on = True

while is_machine_on == True :
    options=menu.get_items()
    choice=input(f"What do you like? {options} : ")
    if choice== "off" :
        is_machine_on = False
    elif choice == "report" :
        money_machine.report()
        coffee_maker.report()
    elif choice not in ["off","report","latte","espresso","cappuccino"]:
        print("Please type Valid option.")
    else:
        drink=menu.find_drink(choice)
        is_enough_ingredients=coffee_maker.is_resource_sufficient(drink)
        is_payment_successful=money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
    