import string
import random

def randomizer(word1,word2,word3,word4, password_length):
    password_words = []
    password_words.extend(list(word1))
    password_words.extend(list(word2))
    password_words.extend(list(word3))
    password_words.extend(list(word4))
    
    random.shuffle(password_words)

    your_password = (''.join(password_words[0:password_length]))
    print(your_password)


def passgenerator():
    upper_case_string = string.ascii_uppercase
    lower_case_string = string.ascii_lowercase
    numbers_digits = string.digits
    symbols = string.punctuation

    # take input from user to determine the length of password
    try:
        password_length = int(input("Enter your desired password length: .. \n"))
    except:
        print("Sorry, Please enter a digit or number, eg:8")
    
    randomizer(upper_case_string,lower_case_string,numbers_digits,symbols,password_length)

passgenerator()