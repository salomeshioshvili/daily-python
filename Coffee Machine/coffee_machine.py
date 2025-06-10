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

profit = 0


def get_user_choice():
    """Prompt the user for their choice of drink."""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        return "off"
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        return "report"
    elif choice in MENU:
        return choice
    else:
        return choice


def check_resources(choice):
    """Check if there are enough resources to make the chosen drink."""
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(choice):
    """Deduct the required ingredients from resources and return the cost of the drink."""
    ingredients = MENU[choice]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")
    return MENU[choice]["cost"]


def process_coins():
    """Return the total amount of coins inserted by the user."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies


def coins_sufficient(cost, inserted_coins):
    """Check if the inserted coins are sufficient to cover the cost."""
    if inserted_coins < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(inserted_coins - cost, 2)
    global profit
    profit += cost
    if change > 0:
        print(f"Here is ${change} in change.")
    return True


def coffee_machine():
    """Main function to run the coffee machine."""
    choice = get_user_choice()
    while choice != "off":
        if choice == "report":
            choice = get_user_choice()
        elif choice in MENU:
            if check_resources(choice):
                cost = MENU[choice]["cost"]
                inserted_coins = process_coins()
                if coins_sufficient(cost, inserted_coins):
                    make_coffee(choice)
            choice = get_user_choice()
        else:
            print("Invalid choice. Please try again.")
            choice = get_user_choice()


coffee_machine()