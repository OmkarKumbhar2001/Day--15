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
    "Profit" :0.0,
}
rupee = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.001
}

def ingredients_is_present(drink, money):
    all_ingri = MENU[drink]['ingredients']
    for i in all_ingri:
        if resources[i] < all_ingri[i]:
            print("inefficient resources. Money refunded. ")
            question_user()
            break

    for i in all_ingri:
        resources[i] -= all_ingri[i]
    change = MENU[drink]['cost']-money
    resources['Profit'] += MENU[drink]['cost']
    print(f"Here is ${change} in change.")
    print(f"Here is your {drink} ☕️. Enjoy!")
    question_user()

def checkDrink(price, drink_name):
    if MENU[drink_name]['cost'] > price:
        print(f"Sorry that's not enough money. Money refunded.")
    else:
        ingredients_is_present(drink_name, price)


def calculation(quarters, dimes, nickles, pennies, drink_name):
    quarter = quarters * rupee['quarters']
    dime = dimes * rupee['dimes']
    nickle = nickles * rupee['nickles']
    pennie = pennies * rupee['pennies']
    total = quarter + dime + nickle + pennie
    checkDrink(total, drink_name)



def ruppees_que(drink_name):
    print("Please Insert Coin")
    quarters = float(input("how many quarters?"))
    dimes = float(input("how many dimes?"))
    nickles = float(input("how many nickles?"))
    pennies = float(input("how many pennies?"))
    calculation(quarters, dimes, nickles, pennies, drink_name)


def question_user():
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "report":
        print(resources)
        question_user()
    else:
        ruppees_que(choice)


question_user()
