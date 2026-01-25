from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
drinks=Menu()
maker=CoffeeMaker()
money=MoneyMachine()
is_onn=True

while is_onn:

    print(drinks.get_items())
    ordername=input("Please enter your drink name: ")
    if ordername=="report":
        maker.report()
        money.report()
        is_onn=False
    elif ordername=="off":
        is_onn=False
    else:
        Menuitem=drinks.find_drink(ordername)

        if maker.is_resource_sufficient(Menuitem):
            if money.make_payment(Menuitem.cost):
                maker.make_coffee(Menuitem)





