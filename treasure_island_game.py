print("Welcome to treasure island, your mission is to find the treasure")

decision = input("you're waling along a path and you come at cross roads, whith path are you taking next (left or right): ")
if decision == "left":
    decision = input("you take the left path and it leads you to a big body of water, enter swim to swim across the body of water, " \
    "type wait to wait for a boat: ")
    if decision == "wait":
        decision = input("a friendly boatman arrives and has taken you to an island. you get off the boat and have 3 doors of different colours before you." \
                "'red', 'yelllow', 'blue'. type in the colour to go through the door: ")
        if decision == "yellow":
               print('''you found the treasure!!, YOU WIN!! \n
                     
                    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
                     
                     ''')
               

        elif decision == "red":
             print("you entered a room engulfed in fire, YOU LOST!")

        elif decision == "blue":
             print("you entered a room filled with wild cats, YOU LOST!")
        else:
            print("you entered the wrong door!")
              
    else:
        print("you were ayyacked by sharks! YOU LOST!!")
    
else:
    print("you were attacked by ghosts. Game over!! ")



 