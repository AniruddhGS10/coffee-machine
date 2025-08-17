MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 120,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 240,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def check_resources():
    chosen_coffee = MENU[coffee_type]["ingredients"]
    for item in chosen_coffee:
        if chosen_coffee[item] > resources[item]:
            return f"The {item} is not enough for {coffee_type}, please come back later", False #This step only gets to execute if the required item is less than resources
    return  f"The resources are enough for {coffee_type}",True


def subtract_resources():
    for item in resources:
        resources[item] -= MENU[coffee_type]["ingredients"][item]
    return resources

balance = 0
coffee_type = "" #if service person types keyword "service mode" the program will stop executing

while True :
    can_deposit = "Yes"
    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
    print("\n"*20)
    if coffee_type == "service mode": #maintainance personals should know the code "service mode"
        print("Coffee machine is now in service mode")
        service_type = input("Please enter service type. To turn off the machine enter 'Off' and to check the resources enter 'Report' :- ").lower()
        if service_type == "report":
            for ingredients,quantity in resources.items():
                print(f"{ingredients}:{quantity},")
            print(f"Money:{balance}.")
            print("The machine is now off, Re-run the program to start the machine")
        elif service_type == "off":
            print("The machine is now off, Re-run the program to start the machine")
        break
    money = 0
    message, can_accept_money = check_resources()


    #prints the availability of the resources and if available accepts the money
    if  can_accept_money:
        print(message)
        money += int(input(f"please enter Rs {MENU[coffee_type]["cost"]} :- Rs "))
        while money < MENU[coffee_type]["cost"]  :
            can_deposit = input(f"You are a bit short on payment can you deposit Rs {(MENU[coffee_type]["cost"]) - money} more, if so type 'Yes' if not type 'No' And you'll get the refund :  ").title()
            if can_deposit == "No":
                print("Here is your Refund.")
                money = 0
                break
            if money < MENU[coffee_type]["cost"]:
                money += int(input(f"please deposit Rs {(MENU[coffee_type]["cost"]) - money} more : "))
    else:
        print(message)




    if money == MENU[coffee_type]["cost"] or money > MENU[coffee_type]["cost"]:
        print("Here is your coffee! Enjoy.")
        subtract_resources()
    if money > MENU[coffee_type]["cost"]:
        change = money - (MENU[coffee_type]["cost"])
        print(f"Here is your change {change}")
        subtract_resources()
        money -= change

    balance += money
    money = 0

    #printing resources

    if coffee_type == "report":
        print(resources)