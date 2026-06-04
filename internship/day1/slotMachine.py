def deposit():
    while True:
        amount = input("Depost: ")
        if amount.isdigit():
            if amount < 0:
                print("The deposit amount should be above 0")
                continue
            else:
                amount = int(amount)
        else:
            print("This deposit amount should be a digit")
    
    return amount
            
def main():
    amount = deposit()

main()