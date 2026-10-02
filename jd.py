p1 = 2
p2 = 2
import random 
player = random.choice(["player1","player2"])
while p1>0 and p2 > 0:
    print(player) 

    gun = random.choice(["blank","shot"])
    if player == "player1":
       a = input("shoot on player2 or yourself : ")
       while a not in ["player2","yourself"]: 
        a = input("shoot on player2 or yourself : ")  
       if a == "player2":
            if gun == "shot":
                p2 = p2 - 1
                print(f"health of player 1 is{p1} and player 2 is {p2}")
            elif gun == "blank":   
                print(f"health of player 1 is{p1} and player 2 is {p2}")
       elif a == "yourself":
            if gun == "shot":
                p1 = p1 - 1
                print(f"health of player 1 is{p1} and player 2 is {p2}")
            while gun == "blank" and a == "yourself": 
                        print("click,player1 got extra turn")
                        gun = random.choice(["blank","shot"]) 
                        a = input("shoot player2 or yourself : ")
                        while a not in ["player2","yourself"]: 
                            a = input("shoot player2 or yourself : ")
                        if a == "player2":
                                    if gun == "shot":
                                        p2 = p2 - 1
                                        print(f"health of player 1 is{p1} and player 2 is {p2}")
                                    else:   
                                        print(f"health of player 1 is{p1} and player 2 is {p2}")
                        elif a == "yourself":
                                    if gun == "shot":
                                        p1 = p1 - 1
                                        print(f"health of player 1 is{p1} and player 2 is {p2}")
    if player == "player2":
      a = input("shoot on player1 or yourself : ")
      while a not in ["player1","yourself"]:
        a = input("shoot on player1 or yourself : ")
      if a == "player1":
            if gun == "shot":
                p1 = p1 - 1
                print(f"health of player 1 is{p1} and player 2 is {p2}")
            elif gun == "blank":  
                print(f"health of player 1 is{p1} and player 2 is {p2}")
      elif a == "yourself":
            if gun == "shot":
                p2 = p2 - 1
                print(f"health of player 1 is{p1} and player 2 is {p2}")
            while gun == "blank" and a == "yourself":
               print("click,player2 got extra turn")
               gun = random.choice(["blank","shot"]) 
               a = input("shoot player1 or yourself : ")
               while a not in ["player1","yourself"]:
                   a = input("shoot player1 or yourself : ")
               if a == "player1":
                if gun == "shot":
                  p1 = p1 - 1
                  print(f"health of player 1 is{p1} and player 2 is {p2}")
                else:   
                  print(f"health of player 1 is{p1} and player 2 is {p2}")
               elif a == "yourself":
                    if gun == "shot":
                     p2 = p2 - 1
                     print(f"health of player 1 is{p1} and player 2 is {p2}")      
    if player == "player1":
        player = "player2"
    elif player == "player2":
        player = "player1"    
if p1 <= 0:
    print("player2 is the winner")
elif p2 <= 0:
    print("player1 is the winner")  