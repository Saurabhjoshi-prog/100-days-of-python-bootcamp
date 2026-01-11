
import art
print(art.logo)
data={}
while True:
# TODO-1: Ask the user for input

    name= input("what is your name? ")
    price=int(input("enter bidding amount: "))

# TODO-2: Save data into dictionary {name: price}
    data[name]=price
# TODO-3: Whether if new bids need to be added
    a=input("do you want to add more yes or no?")
    if a=="no":


        break
    else:
        print("\n"*100)
maxi=0
winner=""
# TODO-4: Compare bids in dictionary
for key in data:
    if data[key]>maxi:
        maxi=data[key]
        winner=key
print(f"the winner is {winner} with the bidd amount {maxi}")







