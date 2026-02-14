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
            raise ValueError("Value out of bound❌")
        elif x ==1:
            print(f"Available seats:{availableSeats}")
            tickets = int(input(f"Enter number of tickets: "))
            if tickets > availableSeats or tickets < 1:
                raise ValueError("Value out of bound")
            price = int(input("Enter ticket price: "))
            if price < 1 or price > 20000: 
                raise ValueError("Value out of bound❌")
            availableSeats -= tickets
        
            print(f"Booking Succesful☑️")
            print(f"Totla Cost: {tickets * price}")
            print(f"Remaining seats: {availableSeats}")       
except ValueError as e:
    print("Invalid Input❌")
        
        