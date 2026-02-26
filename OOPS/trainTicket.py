availableSeats = 100
try:
    while True:
        print()
        print("Book Ticket[1]\t Quit[2]\n")
        x = int(input("Input: "))
        print()
        if x == 2:
            break
        elif x < 1 or x > 2:
            raise ValueError("Arithematic Error❌")
        elif x ==1:
            print(f"Available seats:{availableSeats}")
            tickets = int(input(f"Enter number of tickets: "))
            print()
            if tickets < 1:
                print("Arithematic Error❌")
                break
            if tickets > availableSeats:
                print("Overflow Error")
                break
            price = int(input("Enter ticket price: "))
            print()
            if price < 1 : 
                print("Run time Error❌")
                break
            
            if price > 20000:
                print("Exception")
                break
            availableSeats -= tickets
        
            print(f"Booking Succesful☑️")
            print(f"Total Cost: {tickets * price}")
            print(f"Remaining seats: {availableSeats}")       
except ValueError as e:
    print("ValueError")
        
        