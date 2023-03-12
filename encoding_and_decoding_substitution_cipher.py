# NAME: Zulkifli Temitope Salami	
# DATE: 11/17/2022
# PROGRAM DESCRIPTION: A program used to decode or encode a plain text input from a user. The input would be run through a cipher that encodes or decodes the text, with a key value which indicates the number of times the cipher (substitution cipher) will run.
# PROGRAM NAME: Encoding and Decoding Substitution Cipher



# Declarations:
# english_alphabets as a string
english_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# al_bhed_alphabets as a string
al_bhed_alphabets = 'YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow'
# input_selection as an integer
input_selection = 0
# MINIMUM_VALUE as a constant
MINIMUM_VALUE = 0
# float_value as a float 
float_value = 0.0
# input_encode as a string
input_encode = str
# input_decode as a string
input_decode = str

# Display a message welcoming the user to the program
print ('Welcome to a Encoding and Decoding Cipher using Substitution method and Al Bhed alphabets')
# Define function for encoding a text with parameters message and key. 
def encrypt (message,key):
    for count in range (0,key,1):
        print(count)
        result = ''
        for char in message:
            location = english_alphabets.find(char)
            if location == -1:
                result += char
            else:    
                result += al_bhed_alphabets[location]
            message = result
    return result
# Define function for decoding text with parameters message and key. 
def decrypt (message,key):
    for count in range (0,key,1):
        print(count)
        result = ''
        for char in message:
            location = al_bhed_alphabets.find(char)
            if location == -1:
                result += char
            else:
                result += english_alphabets[location]
            message = result
    return result
# Input, Process and Output:
# Display a menu, “1” to encode, “2” to decode and “3” to exit the program
need_input = True
while need_input == True:
    print('\nWhat would you like to do today:\n1. Encode text\n2. Decode text\n3. Exit the program')
# Prompt the user to choose between 1 to 3 and validate the input as between “1” to “3” inclusive.
    need_input_selection = True
    while need_input_selection == True:
        try:
            input_selection = int(input('\nPlease select an option (1-3): '))
            is_valid = True
        except:
            is_valid = False
            print ('The input has to be a whole number')
            continue
        if input_selection < 1 or input_selection > 3:
            print('The input has to be between 1 and 3 inclusive')
            continue
        else:
            need_input_selection = False
# If the user chooses “1”, prompt user to input text to be encoded and store in input_encode variable. 
# Pass the variable into the encoding function and print the encoded text. 
# Display the menu and prompt user to input choice again.
    if input_selection == 1:
        input_encode = str(input('\nPlease enter the text to encode: '))
        encode_key_times = True
        while encode_key_times == True:
            try:
                encode_key = int(input('How many times would you like to run encryption: '))
            except:
                encode_key = MINIMUM_VALUE - 1
                continue
            if encode_key == float_value or encode_key < 0:
                print('The input has to be a positive whole number')
                continue
            else:
                encode_key_times = False
        encrypted = encrypt(input_encode,encode_key)
        print(encrypted)
        continue
# If the user chooses “2”, prompt user to input text to be decoded and store in input_decode variable. 
# Pass the variable into the decoding function and print the decoded text. 
# Display the menu and prompt user to input choice again.
    elif input_selection == 2:
        input_decode = str(input('\nPlease enter the text to decode: '))
        decode_key_times = True
        while decode_key_times == True:
            try:
                decode_key = int(input('How many times would you like to run encryption: '))
            except:
                decode_key = MINIMUM_VALUE - 1
                continue
            if decode_key == float_value or decode_key < 0:
                print('The input has to be a positive whole number')
                continue
            else:
                decode_key_times = False
        decrypted = decrypt(input_decode,decode_key)
        print(decrypted)
        continue
# If user chooses “3”, prompt the user to press enter to end the program.
    elif input_selection == 3:
        need_input = False
        input('\nPress enter to exit the program......')



