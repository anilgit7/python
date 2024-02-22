import random

def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score=21
player_score=[0 for _ in range(players)]

while max(player_score)<max_score:
    for i in range(players):
        current_score=0
        print("\nPlayer ", i+1 ,"turn.")
        while True:
            turn=input("type 'y' to roll the dice: ")
            if turn.lower()!= "y":
                continue
            while True:
                temp = roll()
                if temp!=1 and temp!=6:
                    current_score+=temp
                    print("You got ", temp)
                    break
                print("you got",temp," and got chance again")
                player_score[i] += temp
                if(player_score[i]>max_score):
                    player_score[i] -= temp      
            break
        player_score[i] += current_score
        if(player_score[i]>max_score):
            player_score[i] -= current_score
        print("Your score till now is: ",player_score[i])

        for a in range(players):
            if i!=a:
                if player_score[i]==player_score[a]:
                    player_score[a]=0
                    print("total of player",a+1,"becomes zero")

max_score=max(player_score)
winner=player_score.index(max_score)
print("Player number", winner + 1, "is the winner with a score of:", max_score)
for i in range(players):
    if(i!=(winner)):
        print("player ",i+1,"got total of",player_score[i])
        
            
