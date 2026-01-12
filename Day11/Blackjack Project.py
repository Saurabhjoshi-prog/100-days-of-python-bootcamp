def Blackjack():
    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    patte= {"Dealer": [],"User": []}
    patte["Dealer"].append(random.choice(cards))
    patte["Dealer"].append(random.choice(cards))
    patte["User"].append(random.choice(cards))
    patte["User"].append(random.choice(cards))
    def add(key):
        s=0
        for i in key:
            s+=i
        return s
    def give_card_to_leader():
            patte["Dealer"].append(random.choice(cards))
    stop_flag=False
    while True:

        def give_card_to_you():

            patte["User"].append(random.choice(cards))

        print("your cards are",patte["User"])
        print("your total is",sum(patte["User"]))
        print("computer's first card is",patte["Dealer"][0])
        if sum(patte["User"])>21:
            print("comp cards were", patte["Dealer"])
            print("comp total is", sum(patte["Dealer"]))
            print("BUST")
            stop_flag=True
            break
        a=input("do you want to Hit or stand?")
        if a=="stand":
            break
        else:
            give_card_to_you()
            print("\n" * 100)

    while not stop_flag:

        b=sum(patte["Dealer"])
        if b<17:
            give_card_to_leader()
            print("Comp current cards are", patte["Dealer"])

        else:
            break

    k=sum(patte["User"])
    b = sum(patte["Dealer"])
    if not stop_flag:
        if b>21:
            print("comp busted")
            print("you win")
        elif k>b:
            print("Comp cards were",patte["Dealer"])
            print("comp total is",sum(patte["Dealer"]))
            print("you win😁")
        elif k==b:
            print("Comp cards were", patte["Dealer"])
            print("comp total is", sum(patte["Dealer"]))
            print("Draw😑")
        else:
            print("Comp cards were", patte["Dealer"])
            print("comp total is", sum(patte["Dealer"]))
            print("you lose🤣")
        p=input("do you want to play Blackjack?")
        if p.lower()=="yes":
            Blackjack()

Blackjack()
