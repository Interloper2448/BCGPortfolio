def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    first_name = get_first_name(full_name)
    print()
    valid_email = get_valid_email()
    print()
    phone_num = get_phone_num()
    print()
    phone_num
    print("Hi " + first_name + ", thanks for creating an account.")
    print("Your email is ", valid_email, "and your password is", "*" * len(password))
    print("We will text you a confirmation to your phone number ",phone_format(phone_num))
    print()

def phone_format(n):
    return format(int(n[:-1]), ",").replace(",", ".") + n[-1]

def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_phone_num():
    while True:
        num = input("Enter a phone number    ").strip()
        num = num.replace(".", "")
        num = num.replace("-", "")
        num = num.replace("(", "")
        num = num.replace(")", "")
        num = num.replace("/", "")
        num = num.replace(" ", "")
        num = num.replace("\\", "")
        if len(num) is 10:
            if num.isdigit():
                return num
        print("Please enter a 10-digit phone number: You entered",num)


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password


def get_valid_email():
    while True:
        email = input("Enter email Address:       ").strip()
        if "@" in email:
            seperate = email.split("@")
            if len(seperate[0]) > 0 and len(seperate[1]) > 0:
                if ".com" in email or ".edu" in seperate[1] or ".gov" in seperate[1]:
                    if " " not in email:
                        return email
        print("You must enter a valid email Address.")


if __name__ == "__main__":
    main()
