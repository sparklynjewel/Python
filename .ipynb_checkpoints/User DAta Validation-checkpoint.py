import random
import string
first_name = input("please enter your first name?: ")
last_name = input("please enter your last name?: ")
email_address = input("please enter your email address?: ")
two_names = (first_name[:2] + last_name[-2:])
print("Your Concatenated details are ", two_names)
stringLength = 5  # initializing size of string
random_letters = string.ascii_lowercase
random_letters = (''.join(random.choice(random_letters) for i in range(stringLength)))
print("The Random String is ", random_letters)
user_password = two_names + random_letters
print("Your random password ", user_password)
