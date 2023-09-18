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
    "coffee": 100
}

# TODO 1 - write all functions here to evaluate answer

def report(resources):
    print("Report:")
    for key in resources:
        if key in ['water','milk']:
            print (f"{key}: {resources[key]}ml")
        elif key in ['coffee']:
            print (f"{key}: {resources[key]}gm")
        else:
            print (f"{key}: ${resources[key]}")

def check_ingredients(ingredient_name, coffee, resources = resources, menu = MENU):
    if ingredient_name in menu[coffee]['ingredients']:
        left_ingredients = resources[ingredient_name] - menu[coffee]['ingredients'][ingredient_name]
    else:
        left_ingredients = False
    return left_ingredients


def check_resources(coffee,resources = resources, menu = MENU):
    resource_status = []
    for key in resources:
        resource_status.append(check_ingredients(key, coffee))
    return resource_status

def coin_checker():
    coin_list = ['quarters', 'dimes', 'nickels', 'pennies']
    coin_number = []
    for coins in coin_list:
        coin_number.append(int(input(f"Insert number of {coins}: ")))
    total_money = (coin_number[0] * 0.25) + (coin_number[1] * 0.1 ) + (coin_number[2] * 0.05 )+ ( coin_number[3] * 0.01)
    return round(total_money,2)


# [x]TODO 2 - show the prompt again after action is completed above
machine_off = "on"
money = {'money': 0}
while not machine_off == 'off':
    coffee_chosen = input("What would you like?\nespresso/latte/cappuccino\nType the name of coffee to make your selection: ").lower()
    if coffee_chosen == 'off':
        machine_off = "off"
    elif coffee_chosen == 'report':
        resource_money = resources.copy()
        resource_money.update(money) 
        report(resource_money)
    else:
        resource_status = check_resources(coffee_chosen)
        # print(list( i<0 for i in resource_status))
        if any( i<0 for i in resource_status):
            for i in range(0,len(resource_status)):
                if resource_status[i] <= 0 :
                    over_resource = list(resources.keys())[i]
            print(f"Sorry there is not enough {over_resource}")
        else:
            total_money = coin_checker()
            if total_money >= MENU[coffee_chosen]['cost']:
                print(f"Your {coffee_chosen} is served!")
                money['money'] += MENU[coffee_chosen]['cost']
                print(resource_status)
                resources["water"] = resource_status[0]
                if resource_status[1] != False:
                    resources["milk"] = resource_status[1]
                resources["coffee"] = resource_status[2]
                return_coin = round(total_money - MENU[coffee_chosen]['cost'],2)
                if return_coin > 0:
                    print(f"Here is your change ${return_coin}")
            else:
                print(f"Money insufficient. Here is your change ${total_money}")

# [x]TODO 3 - Turn of  machine by using code word 'off'

# [x]TODO 4 - typing 'report' should give current status of machine reources

# [x]TODO 5 - Once user request for a drink we should check if sufficient resources are there to make drink else abort

# [x]TODO 6 - if sufficient resources then ask for coins, add the coins

# [x]TODO 7 - If enough coins make coffee else return insufficiemt money or give change and add cost as profit

# [x]TODO 8 - if transcation is successful update report of resources and print msg that coffee is ready



