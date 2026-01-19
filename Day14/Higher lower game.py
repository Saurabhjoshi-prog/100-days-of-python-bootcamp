def HorL():
    import game_data
    import random
    import art

    print(art.logo)
    player_won=False
    choice_1=random.choice(game_data.data)
    choice_2=random.choice(game_data.data)
    c=0
    while not player_won:
        while choice_2==choice_1:
            choice_2=random.choice(game_data.data)
        print("Compare A: ",choice_1['name']," a ",choice_1['description']," from ",choice_1['country'])
        print(art.vs)
        print("Compare B: ", choice_2['name'], " a ", choice_2['description'], " from ", choice_2['country'])
        k=input("Enter which one has higher instagram followers")
        if k=="A":
            if choice_2["follower_count"] < choice_1["follower_count"]:
                print("You won")
                temp = choice_2
                choice_1 = temp
                choice_2=random.choice(game_data.data)
                c+=1
                print("your score is",c)


            else:
                print("You lost")
                player_won = True
        elif k=="B":
            if choice_2["follower_count"] > choice_1["follower_count"]:
                print("You won")
                temp = choice_2
                choice_1 = temp
                choice_2 = random.choice(game_data.data)
                c+=1
                print("your score is", c)


            else:
                print("You lost")
                player_won = True
    print("your final score was",c)
    a=input("do you want to play again?").lower()
    if a=="yes":
        HorL()

HorL()
