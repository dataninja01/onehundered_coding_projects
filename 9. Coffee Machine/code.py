# Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

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

money = 0
remaining_water = resources["water"]
remaining_milk = resources["milk"]
remaining_coffee = resources["coffee"]


def cost(item):
    return MENU[item]["cost"]


class Report:
    def __init__(self):
        self.water = remaining_water
        self.milk = remaining_milk
        self.coffee = remaining_coffee
        self.money = money

    def __str__(self):
        return """
    Water: {0}
    Milk: {1}
    Coffee: {2}
    Money: ${3}
    """.format(self.water, self.milk, self.coffee, self.money)


def total_money(q=0, d=0, n=0, p=0):
    sum_total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    return sum_total


def check_ingredients(item, water=0, milk=0, coffee=0):
    water = MENU[item]["ingredients"]["water"]
    if item != "espresso":
        milk = MENU[item]["ingredients"]["milk"]
    coffee = MENU[item]["ingredients"]["coffee"]
    return water, milk, coffee


def check_remaining(item, rem_water, water, rem_milk, milk, rem_coffee, coffee, tot):
    if total < cost(item):
        print("Sorry that's not enough money. Money refunded.")
    else:
        if rem_water < water:
            print("Sorry not enough water ☹️Money Refunded.")
        elif rem_milk < milk:
            print("Sorry there is not enough milk ☹️Money Refunded.")
        elif rem_coffee < coffee:
            print("Sorry there is not enough coffee ☹️Money Refunded.")
        else:
            print(f"Here is ${round(tot - cost(user_input), 2)} in change")
            print(f"Here is your {item} ☕. Enjoy!")
            


# # TODO Print the report
print("Welcome to the Coffee Machine ! ☕")
# user_input = input("What would you like? (expresso/latte/cappuccino): ").lower()

off = False
while not off:
    user_input = input("What would you like? (expresso/latte/cappuccino): ").lower()
    if user_input == "off":
        off = True
    elif user_input == 'report':
        print(Report())
    else:
        print("Please insert coins")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        print(round(total_money(quarters, dimes, nickles, pennies), 2))
        total = total_money(quarters, dimes, nickles, pennies)
        water_needed = check_ingredients(user_input)[0]
        milk_needed = check_ingredients(user_input)[1]
        coffee_needed = check_ingredients(user_input)[2]
        if total < cost(user_input):
            print("Sorry that's not enough money. Money refunded.")
        else:
            money += round(cost(user_input), 2)
            remaining_water -= water_needed
            remaining_milk -= milk_needed
            remaining_coffee -= coffee_needed
            check_remaining(item=user_input, rem_water=remaining_water, water=water_needed, rem_milk=remaining_milk, milk=milk_needed, rem_coffee=remaining_coffee, coffee=coffee_needed, tot=total)
            






