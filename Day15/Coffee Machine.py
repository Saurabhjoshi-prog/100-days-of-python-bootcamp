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
    "profit": 0
}
stop_flag=False

while True:

        #TODO inout type of coffee

        def coffee():
            a=input("what would you like? latte/cappuccino/espresso")
            return a
        coffee_type=coffee()
        if coffee_type == "report":
            print(resources)
            break
        elif coffee_type == "off":
            break
        elif coffee_type == "replenish":
            resources["water"]=300
            resources["milk"]=200
            resources["coffee"]=100
            break



        # TODO 3 chk for the availibility of ingredients:
        def make_coffee(coffee_type):
            for i in resources:

                if resources[i] > MENU[coffee_type]["ingredients"][i]:
                    resources[i] = resources[i] - MENU[coffee_type]["ingredients"][i]
                    return True
                else:
                    print("sorry", i, "is not enough")
                    print("here is your money back", round(total, 2))

                    return False
        #TODO  Ask for money:
        def money():
            print("enter money")
            quater=int(input("enter no of quater:"))
            dime=int(input("enter no of dime:"))
            nickel=int(input("enter no of nickel:"))
            pennies=int(input("enter no of pennies:"))
            mm=(quater*0.25)+(dime*0.10)+(nickel*0.05)+(pennies*0.01)
            return mm
        total = money()
        #TODO Chk if money is enough or no
        def chk_money(total):
            cm=total-MENU[coffee_type]["cost"]
            if cm>=0:
                return True
            else:
                return False

        #TODO 2. Ask user for the type of coffee:


        if make_coffee(coffee_type):
            if chk_money(total):
                lm=total-MENU[coffee_type]["cost"]
                print("here is your coffee:","and here is your change",round(lm,2))
                resources["profit"]+=MENU[coffee_type]["cost"]
            else:
                print("sorry,money is not enough,here is your money back",round(total,2))



