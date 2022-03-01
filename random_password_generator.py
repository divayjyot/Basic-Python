import array
import random
import string

lowCaseLetters = list(string.ascii_lowercase)
upCaseLetters = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(''' !@#$%^&*()_-+={[}]|\:;"'<,>.?/ ''')

characters = lowCaseLetters + upCaseLetters + digits + symbols


def generate_password():

    Random_Lowletters = random.choice(lowCaseLetters)
    Random_Upletters = random.choice(upCaseLetters)
    Random_digits = random.choice(digits)
    Random_symbols = random.choice(symbols)

    Random_characters = Random_Lowletters + Random_Upletters + Random_digits + Random_symbols

    length = int(input("Enter the length: "))

    if length < 12:
        print("Password too short: Cannot be less than 12 letters")
        return

    elif length > 25:
        print("Password too long: Cannot be more than 25 letters")
        return

    else:
        random.shuffle(characters)

        for i in range(length - 4):
            Random_characters = Random_characters + random.choice(characters)

            temp_pass = array.array('u', Random_characters)
            random.shuffle(temp_pass)

        password = ""
        for i in temp_pass:
            password = password + i

    print(password)


generate_password()
