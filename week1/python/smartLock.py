#secret number lock
def passWordChecker(password):
    if password == 123456789:
        print("The lock is Unlocked ✅")
    else:
        print("Incorrect Password ❌")
password = int(input("Enter the pin number: "))
passWordChecker(password)