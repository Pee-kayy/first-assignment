import random
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
safe_symbols_web = ['-', '#', '_', '$', '!', '*', '(', ')', '%', '&']

alphabet_input = int(input("please enter how many letters you want in your password: "))
num_input = int(input("please enter how many numbers you want in your password: "))
symbol_input = int(input("please enter how many symbols you want in your password: "))




# i initially used an empy stirng to hold the values of the inputs but as i went on i relised that i had challenges randomizing 
# outputs with random.shuffle so i had to hold the user's inputs in a string in order to conviniently make use of the random.shuffle
# functiion

password = []


for int in range (0, alphabet_input):
    randomchar = random.choice(alphabets)
    password.append(randomchar)

for int in range (0, num_input):
    randomnum = random.choice(numbers)
    password.append(randomnum)
   

for int in range (0, symbol_input):
    randomsymbols = random.choice(safe_symbols_web)
    password.append(randomsymbols)
    
 



# //////////////THE SIMPLE LOGIC TO RANDOMIZE THE "PASSWORD" LIST//////////////// 
random.shuffle(password)



# ////////////////////THE SIMPLE LOGIC TO CONVERT "PASSWORD" FROM LIST BACK TO STRING USING A FOR LOOP////////////////////////////////////
real_password = ""
for char in password:
    real_password += char
print(f"your password is {real_password}")


