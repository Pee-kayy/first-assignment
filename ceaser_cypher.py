# ///////////////////////////////ENCRYPT//////////////////////////////////
# def encrypt(original_text, shift_amount):
#     output_encrypt = ""
#     for letter in original_text:
#             # text.append(letter)
#             encrypt = alphabet.index(letter) + shift_amount
#             encrypt %= len(alphabet)
#             encrypted_letter = alphabet[encrypt]
#             output_encrypt += encrypted_letter
#     print ( output_encrypt)


# //////////////////////////////DECRYPT////////////////////////////////
# def decrypt (original_text, shift_amount):
#   output_decrypt = ""
#   for letter in original_text:
#             decrypt = alphabet.index(letter) - shift_amount
#             decrypt %= len(alphabet)
#             decrypyed_letter = alphabet[decrypt]
#             output_decrypt += decrypyed_letter      
#   print( output_decrypt)




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# /////////////////////////////EXECUTION////////////////////////////////
def ceasar(original_text, shift_amount, encode_or_decode):
    output = ""
    
    if direction == "decode":
          shift_amount *= -1


    for letter in original_text:
        if letter in alphabet:
            # text.append(letter)
            encrypt_or_decrypt = alphabet.index(letter) + shift_amount
            encrypt_or_decrypt %= len(alphabet)
            adjusted_letter = alphabet[encrypt_or_decrypt]
            output += adjusted_letter

        else:
            output += letter
        
    print(f"your {encode_or_decode}d text is {output} ")



re_run = True   
while re_run:
    direction = input("type 'encode' to encrypt' or 'decode' to decrypt: ").lower()
    message = input(f"type the message you wish to {direction}: ").lower()
    shift =int(input("enter the amount of shift you want: "))
    ceasar(original_text = message, shift_amount = shift, encode_or_decode = direction)


    answer = True
    while answer:
        restart = input("type 'yes' to go again  otherwise type 'no': \n")       
        if restart == "no":
            answer = False
            re_run = False
            print("thank you for using cesar_cypher")

        elif restart == "yes":
            answer = False

        else:
            print("incorrect entry")

       

       















 
  

