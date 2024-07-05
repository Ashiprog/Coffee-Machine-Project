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
    "money": 0
}

types_of_coffee = ['espresso', 'latte', 'cappuccino']
ingredients = ["water", "milk", "coffee"]

machine_on = 'yes'
total_change = 0


def machine_report():
    print(f"water:{resources['water']}\nmilk:{resources['milk']}\ncoffee:{resources['coffee']}\nmoney:${resources['money']}")


def check_coffee_resources(coffee):
    global flag
    for items in ingredients:
        if resources[items] >= MENU[coffee]["ingredients"][items]:
            flag += 1

        else:

            print(f"there is not enough {items}")
        if flag == 3:
            return 'sufficient'


def check_money(coffee):
    global total_change
    total_amount_paid = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
    coffee_cost = MENU[coffee]["cost"]
    if total_amount_paid >= coffee_cost:
        total_change = round(total_amount_paid - coffee_cost, 2)

        resources["money"] += coffee_cost
        return "sufficient"
    else:
        print("That's not sufficient money")


def make_coffee(coffee):
    for items in ingredients:
        resources[items] = resources[items] - MENU[coffee]["ingredients"][items]


while machine_on == 'yes':
    flag = 0
    user_choice = input("What would you like to have?(espresso/latte/cappuccino):").lower()
    if user_choice == "report":
        machine_report()
    elif user_choice == "off":
        machine_on = "no"
    elif user_choice in types_of_coffee:

        if check_coffee_resources(coffee=user_choice) == "sufficient":
            print("Please insert coins")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("How many nickles: "))
            pennies = float(input("How many pennies: "))
            if check_money(coffee=user_choice) == "sufficient":
                print(f"Please enjoy your {user_choice}. Here is your change ${total_change}")
                make_coffee(coffee=user_choice)

    else:
        print("Invalid choice")
