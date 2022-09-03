# Caesar Cipher Project, 100Days of code, Angela Yu
# Student: Łukasz Świątek Brzeziński
#The program allows to encode the message in the way as Caesar make it in the ancient times.
#You can also decode the message from the Caesar :)

logo = '''
           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
#print(logo)

def caesar (message, shift, option):
    new_message = ""
    if option == "decode":
        shift *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift 
            new_message += alphabet[new_position]
        else:
            new_message += char
    if option == "encode":
        print(f"Encoded message is {new_message}")
    elif option == "decode":
            print(f"Decoded message is {new_message}")


go_again = "yes"
while go_again == "yes":

    alphabet = 2*[chr(element) for element in range(97,123)]
    print(alphabet)


    option = input("What do you want to do (encode, decode)?").strip().lower()
    message = input("Type the message to encode").lower()
    shift = int(input("Type the number of shifts"))
    shift = shift % 26 #26 is the number of letters or avid bugs in huge numbers
    caesar(message, shift, option)

    go_again = input("would you like to continue (yes, no)?").strip().lower()
    if go_again == "no":
        print("Good bye! :)")

