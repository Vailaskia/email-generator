import random
import string


def email_gen():

    chars_after_at = int(input("Enter how much chars you want after @gmail.com between 4 and 20 max :"))

    if(chars_after_at < 4 or chars_after_at > 20):
        print("Please enter between 4 and 20 chars max")
        exit()
    else:

        letters_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase]

        letters_list_to_str = "".join(letters_list)

        email_format = "@gmail.com"

        email_generated = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + email_format
        password_generated = "".join(random.choices(letters_list_to_str, k=chars_after_at)) 

        print(email_generated)
        print(password_generated)

# call email generator function
email_gen()
