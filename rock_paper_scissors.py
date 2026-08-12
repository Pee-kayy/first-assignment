import random
hand_sign_initials = ["r","p","s"]
human_entry = input("enter 'r' for rock, 'p' for paper 's' and s for 'scissors': ")
computer_entry = random.choice(hand_sign_initials)
# print (computer_entry)

r = hand_sign_initials[0]
p = hand_sign_initials[1]
s = hand_sign_initials[2]




hand_signs = [''' ROCK!! \n    _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
''', 

''' PAPER!! \n   _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)''', 
      
      ''' SCISSORS!! \n
                  _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)''']





if human_entry in hand_sign_initials:
    index_humanentry = hand_sign_initials.index(human_entry)
    output_human_handsign = hand_signs[index_humanentry]
    print(f"you selected {output_human_handsign} \n")

    index_computerentry = hand_sign_initials.index(computer_entry)
    output_computer_handsign = hand_signs[index_computerentry]
    print(f"computer selected {output_computer_handsign}")

else:
    print(f"{human_entry} is an invalid input")



# index_computerentry = hand_sign_initials.index(computer_entry)
# output_computer_handsign = hand_signs[index_computerentry]
# print(f"computer selected {output_computer_handsign}")








# /////////////logic/////////////////////////
if human_entry == r and computer_entry == s:
    print("you win")

elif  human_entry == s and computer_entry == p:
    print("you win")

elif  human_entry == p and computer_entry == r:
    print("you win")

elif human_entry == computer_entry:
    print("its a draw, go again")

elif human_entry not in hand_sign_initials:
    print("please try again")

else:
    print("you loose")
