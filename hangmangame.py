import random
import hangmanwords
import hangmanart

# TODO1 - Randomly choose a word from the word list and assign the word to a variable called chosen_word and then print it
# TODO2 - Ask the user to guess a letter and assign to a variable called guess . (make guess lowercse)
# TODO3 - check if the letter the user guessed is in chosen word and print right if it is and wrong if it's not

chosen_word = random.choice(hangmanwords.word_list)
print(f"{chosen_word} \n")

found_count = 0
guess_count = 6

# create a place holder with the same number of blank underscores as the chosen letter
blank_spaces = ""
for i in range(0, len(chosen_word)):
      blank_spaces+="_ "
print(f"{blank_spaces} \n")


# //////////////////////////////////////////////////////////////////////////////
correct_answers = []


# guess = input("guess a letter: ").lower()


while guess_count != 0:
    # guess_count +=1
    placeholder = ""

   
         
    guess = input("guess a letter: ").lower()
    if guess in correct_answers:
        print("you've already guessed this")
    
   

    for i in chosen_word:
        if i == guess:
            placeholder += i
            correct_answers += guess
        
        elif  i in correct_answers:
             placeholder += i
            
        else:
            placeholder += "_ "
           

  


        
  

    

    if guess not in  correct_answers:
        guess_count -= 1 
        print(f"you have {guess_count} guesses left")
    
    print(hangmanart.stages[guess_count])

    print(placeholder)
    if placeholder == chosen_word:
        print("you guessed the word and you've won")
        break

    
    if guess_count == 0:
        print(f"you have {guess_count} guesses left")
        print(f"game over you lost the word to guess was '{chosen_word}' ")








































#  '''      _______
#       |/      |
#       |      (_)
#       |      \|/
#       |       |
#       |      / \
#       |
#   jgs_|___
#   '''

# ,,,
# #       _______
# #      |/      |
# #      |      (_)
# #      |      \|/
# #      |       |
# #      |      / 
# #      |
# #  jgs_|___
# '''



# #'''      _______
# #      |/      |
# #      |      (_)
# #      |      \|/
# #      |       |
# #      |      
# #      |
# #  jgs_|___
# '''





# #'''     _______
# #      |/      |
# #      |      (_)
# #      |      \ /
# #      |       
# #      |      
# #      |
# #  jgs_|___
# '''


# #'''     _______
# #      |/      |
# #      |      (_)
# #      |      \ 
# #      |       
# #      |     
# #      |
# #  jgs_|___
# '''

# #'''   _______
# #      |/      |
# #      |      (_)
# #      |       
# #      |       
# #      |     
# #      |
# #  jgs_|___
# '''
# #'''  _______
# #      |/      |
# #      |      
# #      |       
# #      |       
# #      |     
# #      |
# #  jgs_|___
# '''