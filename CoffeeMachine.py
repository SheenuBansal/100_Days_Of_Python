MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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


Money_in_machine=0
secret_word=False
while secret_word!=True:
    users_order=input("What would you like today? (espresso/latte/cappuccino/) or Type 'report' for checking contents.\n").lower()

    if users_order=="off":
        secret_word=True

    elif users_order=='report':
        
        # Displaying the contents of Coffee Machine.
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} g")
        print(f"Money : $ {Money_in_machine}")

    elif users_order=='espresso' or users_order=='latte' or users_order=='cappuccino':

        # Check if sufficient content is there in machine.

        if resources['water']< MENU[users_order]['ingredients']['water']:
            print(f"Sorry!! 🙁 There is not enough water.")
        elif resources['milk']< MENU[users_order]['ingredients']['milk']:
            print(f"Sorry!! 🙁 There is not enough milk.")
        elif resources['coffee']< MENU[users_order]['ingredients']['coffee']:
            print(f"Sorry!! 🙁 There is not enough coffee.")
        
        # Ask user For Coins and serve coffee.
        else:
            print("Please insert coins")
            quarters=float(input("How many quarters?: "))*0.25
            dimes=float(input("How many dimes?: "))*0.10
            nickles=float(input("How many nickles?: "))*0.05
            pennies=float(input("How many pennies?: "))*0.01
            money_given_by_user=quarters+dimes+nickles+pennies

            if money_given_by_user < MENU[users_order]['cost'] :
                print("Sorry that's not enough money. Money refunded.")
            else:
                # Money to give back to user
                money_to_return=round(money_given_by_user-MENU[users_order]['cost'],2)

                # Money to deposit in our machine.
                Money_in_machine+=MENU[users_order]['cost']

                print(f"Here is $ {money_to_return} in change.")
                print(f"Here is your {users_order} ☕. Enjoy!!! ")

                # Updating the ingredients of machine.

                for ingredient in MENU[users_order]['ingredients']:
                    resources[ingredient]-=MENU[users_order]['ingredients'][ingredient]
                
    else:
        print("Please type correct value.")


