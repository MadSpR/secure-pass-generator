import string
import random

#### EXPAND TO SAVE THE GENERATED PASSWORDS IN A FILE


#### INICIALIZACIÓN VARIABLES
length = 0
amount = 0
option = 0
keyword = ""
chars = string.ascii_letters + string.digits + string.punctuation
password = ""
list_password = []


#### FUNCTIONS

def pass_keyword(keyword, long, amount):
    ## creates an array with the keywords characters plus digits
    charset = ""
    for i in keyword:
        charset += i
    charset += string.digits
    
    ## creates a list with the amount of passwords and the length specified
    for i in range(amount):
        password = "".join(random.choice(charset) for i  in range(long))
        list_password.append(password)

    return list_password


def pass_random(long, amount):
    ## creates a list with the amount of passwords and the length specified
    for i in range(amount):
        password = "".join(random.choice(chars) for i in range(long))
        list_password.append(password)
    
    return list_password


#### PROGRAM

## if the variable is a number equal to or greater than 10, creates the password. Otherwise asks again.
while ((type(length) != int) | (int(length) < 10)):
    try:
        length = int(input("Enter the length of the password (minimum length of 10): "), 10)
    except:
        print("You must enter a number.")

## asks the user how many passwords wants to generate (1-10)
while ((type(amount) != int) | (int(amount) > 10) | (int(amount) < 1)):
    try:
        amount = int(input("Enter the amount of passwords you want to generate (1-10): "), 10)
    except:
        print("You must enter a valid number.")


## gives two options, create a password from a word
# or create it with random characters
while ((type(option) != int) | (int(option) > 2) | (int(option) < 1)):
    try:
        option = int(input("If you want to create the password from a keyword press 1,\nif you want to create it with random characters press 2: "), 10)
    except:
        print("Invalid option.")

if option == 1:
    keyword = input("Enter the keyword: ")
    list_password = pass_keyword(keyword, length, amount)
    for i, passw in enumerate(list_password):
        print(str(i + 1) + "º password is: " + passw)
    
elif option == 2:
    list_password = pass_random(length, amount)
    for i, passw in enumerate(list_password):
        print(str(i + 1) + "º password is: " + passw)