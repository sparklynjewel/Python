import random
import string


def user_details():

    first_name = input("please enter your first name: ")
    last_name = input("please enter your last name: ")
    email_address = input("please enter your email address: ")

    detail = [first_name, last_name, email_address]

    return detail


def user_password(detail):

    string_length = 5  # initializing size of string
    letters = string.ascii_lowercase
    random_letters = ''.join(random.choice(letters) for i in range(string_length))
    password = str(detail[0][:2] + detail[1][-2:] + random_letters)
    return password


password_choice = 0
password_length = 0
status = True
container = []
users = {}
userNumber = 1

while status:
    detail = user_details()
    password = user_password(detail)

    print("Your generated password is: " + str(password))

    print("Are you satisfied with the Password? ")

    print("Menu")

    print('1.Yes, user satisfied with password')

    print('2.No, user not satisfied with password')
    while True:
        try:
            while (password_choice < 1) or (password_choice > 2):
                password_choice = int(input("Please insert your menu option: "))
            break
        except ValueError:
            print("please type in a number? ")

    password_loop = True
    while password_loop:
        if password_choice == 1:
            detail.append(password)
            container.append(detail)
            print(detail)
            password_loop = False

        else:
            personal_password = input(str("please enter preferred password greater than or equal to 7: "))
            password_length = True
            while password_length:

                if len(personal_password) >= 7:
                    detail.append(personal_password)
                    container.append(detail)
                    users[userNumber] = detail
                    print(detail)
                    password_length = False
                    password_loop = False
                else:
                    print("Password must be at least 7 characters!")
                    personal_password = input(str("please enter preferred password greater than or equal to 7: "))
    new_user = input(str("Would you like to enter a new user? Yes or No: "))

    if new_user == "No":
        status = False
        for item in users:
            print(users.get(item))
    else:
        status = True
        userNumber = userNumber + 1

