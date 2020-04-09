import random
import string
from typing import List

first_name = input("please enter your first name: ")
last_name = input("please enter your last name: ")
email_address = input("please enter your email address: ")
userDetails: List[str] = [first_name, last_name, email_address]
two_names = (first_name[:2] + last_name[-2:])  # getting letters of the first and last name,respectively.
print("Your Concatenated details is ", two_names)

stringLength = 5  # initializing size of string
random_letters = string.ascii_lowercase
random_letters = (''.join(random.choice(random_letters) for i in range(stringLength)))

print("The Random String generated is ", random_letters)
user_password = (two_names + random_letters)

print("Your generated Password is: ", user_password)
password_choice = 0
password_length = 0
status = True
container = []
users = {}
userNumber = 1

print("Are you satisfied with the Password? ")
print("Menu")
print('1.Yes, user satisfied with password')
print('2.No, user not satisfied with password')
while status:
    while True:
        try:
            while (password_choice < 1) or (password_choice > 2):
                password_choice = int(input("Please insert your menu option: "))
            break
        except ValueError:
            print("please type in a number? ")
    if password_choice == 1:
        userDetails.append(user_password)
        container.append(userDetails)
        users[userNumber] = userDetails
        print(userDetails)
        break
    else:
        while (password_length < 7) or (password_length >= 7):
            personal_password = input("please enter preferred password greater than or equal to 7: ")
            if len(personal_password) < 7:
                print("Password must be at least 7 Characters!")
                break
            else:
                userDetails.append(personal_password)
                container.append(userDetails)
                users[userNumber] = userDetails
                print(userDetails)
new_user = input(str("Would you like to enter a new user? Yes or No"))
if new_user == "No":
    status = False
    for item in users:
        print(users.get(item))
else:
    status = True
    userNumber = userNumber + 1
quit()
