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

money = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

# Variables
operating = True
active = False
quarters = list(money.items())[0][1]
dimes = list(money.items())[1][1]
nickles = list(money.items())[2][1]
pennies = list(money.items())[3][1]
storedWater = list(resources.items())[0][1]
storedMilk = list(resources.items())[1][1]
storedCoffee = list(resources.items())[2][1]

# TODO: 2. Check Resources are Sufficient.

def resourceCheck(optionWater,optionMilk,optionCoffee):
    storedWater = list(resources.items())[0][1]
    storedMilk = list(resources.items())[1][1]
    storedCoffee = list(resources.items())[2][1]

    if type(storedWater) == str:
        storedWater = storedWater.replace('ml', '')
        storedWater = int(storedWater)
    if type(storedMilk) == str:
        storedMilk = storedMilk.replace('ml', '')
        storedMilk = int(storedMilk)
    if type(storedCoffee) == str:
        storedCoffee = storedCoffee.replace('g', '')
        storedCoffee = int(storedCoffee)
    # Will need to re-order with insufficient being prioritised first

    if storedWater < optionWater or storedMilk < optionMilk or storedCoffee < optionCoffee:
        return print("Insufficient Resources")
    else:
        return True

# TODO: 3. Process Coins - Refunds or Calculation Changes

def funding(optionCost, pennies, nickles, dimes, quarters):
    print('Please insert coins.')
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    return total

# TODO 5. Makes Coffee

def creation(optionWater,optionMilk,optionCoffee):
    if storedWater > optionWater:
        newWater = storedWater - optionWater
        newWater = str(newWater) + "ml"
        updateWater = {"water": newWater}
        resources.update(updateWater)
    if storedMilk > optionMilk:
        newMilk = storedMilk - optionMilk
        newMilk = str(newMilk) + "ml"
        updateMilk = {"milk": newMilk}
        resources.update(updateMilk)
    if storedCoffee > optionCoffee:
        newCoffee = storedCoffee - optionCoffee
        newCoffee = str(newCoffee) + "g"
        updateCoffee = {"coffee": newCoffee}
        resources.update(updateCoffee)

# Need to make function to minimise the print code
def machine(option):
    if option == 'espresso':
        optionCost = float(list(MENU.items())[0][1]['cost'])
        upfrontCost = "{:.2f}".format(optionCost)
        optionWater = list(MENU.items())[0][1]['ingredients'].get('water')
        optionMilk = list(MENU.items())[0][1]['ingredients'].get('milk')
        optionCoffee = list(MENU.items())[0][1]['ingredients'].get('coffee')
        print(f'Contains: '
              f'Water = {optionWater}, '
              f'Milk = {optionMilk}, '
              f'and Coffee = {optionCoffee}, '
              f'with a final Cost: ${upfrontCost}')

        active = resourceCheck(optionWater, optionMilk, optionCoffee)
        if active == True:
            change = funding(optionCost, pennies, nickles, dimes, quarters)
            initial = "{:.2f}".format(change)
            print(f"Your intial total is: ${initial}")
            if change < optionCost:
                change = "{:.2f}".format(change)
                print(f"Refund ${change}, Failure!")
            elif change >= optionCost:
                change = change - optionCost
                creation(optionWater, optionMilk, optionCoffee)
                change = "{:.2f}".format(change)
                print(f"Your change ${change}, enjoy your {option}!")

    elif option == 'latte':
        optionCost = float(list(MENU.items())[1][1]['cost'])
        upfrontCost = "{:.2f}".format(optionCost)
        optionWater = int(list(MENU.items())[1][1]['ingredients'].get('water'))
        optionMilk = int(list(MENU.items())[1][1]['ingredients'].get('milk'))
        optionCoffee = int(list(MENU.items())[1][1]['ingredients'].get('coffee'))
        print(f'Contains: '
              f'Water = {optionWater}, '
              f'Milk = {optionMilk}, '
              f'and Coffee = {optionCoffee}, '
              f'with a final Cost: ${upfrontCost}')

        active = resourceCheck(optionWater, optionMilk, optionCoffee)
        if active == True:
            change = funding(optionCost, pennies, nickles, dimes, quarters)
            initial = "{:.2f}".format(change)
            print(f"Your intial total is: ${initial}")
            if change < optionCost:
                change = "{:.2f}".format(change)
                print(f"${change}, Failure!")
            elif change >= optionCost:
                change = change - optionCost
                creation(optionWater, optionMilk, optionCoffee)
                change = "{:.2f}".format(change)
                print(f"Your change ${change}, enjoy your {option}!")

    elif option == 'cappuccino':
        optionCost = float(list(MENU.items())[2][1]['cost'])
        upfrontCost = "{:.2f}".format(optionCost)
        optionWater = list(MENU.items())[2][1]['ingredients'].get('water')
        optionMilk = list(MENU.items())[2][1]['ingredients'].get('milk')
        optionCoffee = list(MENU.items())[2][1]['ingredients'].get('coffee')
        print(f'Contains: '
              f'Water = {optionWater}, '
              f'Milk = {optionMilk}, '
              f'and Coffee = {optionCoffee}, '
              f'with a final Cost: ${upfrontCost}')

        active = resourceCheck(optionWater, optionMilk, optionCoffee)
        if active == True:
            change = funding(optionCost, pennies, nickles, dimes, quarters)
            initial = "{:.2f}".format(change)
            print(f"Your intial total is: ${initial}")
            if change < optionCost:
                change = "{:.2f}".format(change)
                print(f"${change}, Failure!")
            elif change >= optionCost:
                change = change - optionCost
                creation(optionWater, optionMilk, optionCoffee)
                change = "{:.2f}".format(change)
                print(f"Your change ${change}, enjoy your {option}!")

    # TODO: 1. Print Report - All resources are printed.

    elif option == 'report':
        total = int((pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25))
        updateMoney = {"money": total}
        resources.update(updateMoney)

        storedWater = list(resources.items())[0][1]
        storedMilk = list(resources.items())[1][1]
        storedCoffee = list(resources.items())[2][1]
        if type(storedWater) == str:
            storedWater = storedWater.replace('ml', '')
            storedWater = int(storedWater)
        if type(storedMilk) == str:
            storedMilk = storedMilk.replace('ml', '')
            storedMilk = int(storedMilk)
        if type(storedCoffee) == str:
            storedCoffee = storedCoffee.replace('g', '')
            storedCoffee = int(storedCoffee)

        resources.update({"water": storedWater, "milk": storedMilk, "coffee": storedCoffee, })

        for k, v in resources.items():
            if k == "water":
                v = str(v) + "ml"
                print(k, v)
            elif k == "milk":
                v = str(v) + "ml"
                print(k, v)
            elif "coffee" == k:
                v = str(v) + "g"
                print(k, v)
            elif "money" == k:
                v = "$" + str(v)
                print(k, v)

        resources.update(updateMoney)
    else:
        print("Wrong input.")

# Skeleton
while operating == True:
    storedWater = list(resources.items())[0][1]
    storedMilk = list(resources.items())[1][1]
    storedCoffee = list(resources.items())[2][1]

    option = input('What would you like? (espresso/latte/cappuccino): ').lower()
    machine(option)

# TODO 4. Checks whether transaction is successful


