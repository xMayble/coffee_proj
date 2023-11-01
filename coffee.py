import data

# store the prices of each bev
espresso_cost = data.MENU['espresso']['cost']
latte_cost = data.MENU['latte']['cost']
cappuccino_cost = data.MENU['cappuccino']['cost']

# setting up a boolean to keep asking user
keep_going = True

# current storage of resources
water_storage = data.resources['water']
milk_storage = data.resources['milk']
coffee_storage = data.resources['coffee']

while keep_going:

    # var to store total value of user's coins
    total_value = 0

    decision = input("What would you like? (espresso/latte/cappuccino): ")

    if decision == 'report':
        print(f"Water: {water_storage}")
        print(f"Milk: {milk_storage}")
        print(f"Coffee: {coffee_storage}")

    elif data.MENU[decision]['ingredients']['water'] > water_storage:
        print(f"Sorry, there isn't enough resources to make {decision}")
        keep_going = False
        break
    elif data.MENU[decision]['ingredients']['milk'] > milk_storage:
        print(f"Sorry, there isn't enough resources to make {decision}")
        keep_going = False
        break
    elif data.MENU[decision]['ingredients']['coffee'] > coffee_storage:
        print(f"Sorry, there isn't enough resources to make {decision}")
        keep_going = False
        break

    elif decision == 'latte':

        print(f"Price for a cup of latte is: ${format(latte_cost, '.2f')}")

        # ask for number of coins for each coin value
        print("Please insert coins!")
        num_of_quarters = (int(input("How many quarters?: ")) * 0.25)
        num_of_dimes = (int(input("How many dimes?: ")) * 0.10)
        num_of_nickels = (int(input("How many nickels?: ")) * 0.05)
        num_of_pennies = (int(input("How many pennies?: ")) * 0.01)

        # calculate the total value of all the coins the user inputted
        total_value += (num_of_quarters + num_of_dimes + num_of_nickels + num_of_pennies)

        if total_value > latte_cost:
            print(f"Here's your cup of latte, and your change ${format((total_value - latte_cost), '.2f')}")
        elif total_value < latte_cost:
            print(f"Sorry, too low! You gave ${format(total_value, '.2f')}, but the price is ${format(latte_cost, '.2f')}.")
        else:
            print("Here's your latte! Enjoy!")
            water_storage -= data.MENU['latte']['ingredients']['water']
            milk_storage -= data.MENU['latte']['ingredients']['milk']
            coffee_storage -= data.MENU['latte']['ingredients']['coffee']
            print(water_storage)
            print(milk_storage)
            print(coffee_storage)

    elif decision == 'espresso':

        print(f"Price for a cup of espresso is: ${format(espresso_cost, '.2f')}")
        # ask for number of coins for each coin value
        print("Please insert coins: ")
        num_of_quarters = int(input("How many quarters?: "))
        num_of_dimes = int(input("How many dimes?: "))
        num_of_nickels = int(input("How many nickels?: "))
        num_of_pennies = int(input("How many pennies?: "))
        # calculate the total value of all the coins the user inputted
        total_value += (
                (num_of_quarters * 0.25) + (num_of_dimes * 0.10) + (num_of_nickels * 0.05) + (num_of_pennies * 0.01)
        )
        if total_value > espresso_cost:
            print(f"Here's your cup of espresso, and your change ${format((total_value - espresso_cost), '.2f')}")
        elif total_value < espresso_cost:
            print(f"Sorry, too low! You gave ${format(total_value, '.2f')}, but the price is ${format(espresso_cost, '.2f')}.")
        else:
            print("Here's your espresso! Enjoy!")
            water_storage -= data.MENU['espresso']['ingredients']['water']
            milk_storage -= data.MENU['espresso']['ingredients']['milk']
            coffee_storage -= data.MENU['espresso']['ingredients']['coffee']

    else:

        print(f"Price for a cup of cappuccino is: ${format(cappuccino_cost, '.2f')}")
        # ask for number of coins for each coin value
        print("Please insert coins: ")
        num_of_quarters = int(input("How many quarters?: "))
        num_of_dimes = int(input("How many dimes?: "))
        num_of_nickels = int(input("How many nickels?: "))
        num_of_pennies = int(input("How many pennies?: "))
        # calculate the total value of all the coins the user inputted
        total_value += (
                    (num_of_quarters * 0.25) + (num_of_dimes * 0.10) + (num_of_nickels * 0.05) + (num_of_pennies * 0.01)
        )
        if total_value > cappuccino_cost:
            print(f"Here's your cup of cappuccino, and your change ${format((total_value - cappuccino_cost), '.2f')}")
        elif total_value < cappuccino_cost:
            print(f"Sorry, too low! You gave ${format(total_value, '.2f')}, but the price is ${format(cappuccino_cost, '.2f')}.")
        else:
            print("Here's your cappuccino! Enjoy!")
            water_storage -= data.MENU['cappuccino']['ingredients']['water']
            milk_storage -= data.MENU['cappuccino']['ingredients']['milk']
            coffee_storage -= data.MENU['cappuccino']['ingredients']['coffee']





