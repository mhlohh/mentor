import random

MIN_LINE = 1
MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

COLS = 3
ROWS = 3

symbol_count = {
    "🤑": 2,
    "🤡": 4,
    "😇": 6,
    "😍": 8
}

symbol_values = {
    "🤑": 5,
    "🤡": 4,
    "😇": 3,
    "😍": 2
}

def check_winnings(columns,lines,bet,symbol_values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_values[symbol] * bet
            winning_line.append(line+1)
    return winnings,winning_line
            
def get_slot_machine_spint(rows,cols,symbols):
        all_symbols = []
        for symbol ,symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)
        
        columns = []
        for _ in range(cols):
            column = []
            current_symbol = all_symbols[:]
            for _ in range(rows):
                value = random.choice(current_symbol)
                current_symbol.remove(value)
                column.append(value)
            columns.append(column)
        return columns
    
def print_slot_machine(columns):
    l = len(columns)-1
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if ( i != l):
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()
                
             
             

def deposit():
    while True:
        amount = input("Enter the deposit amount $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("The deposit amount should be greater than zero")
            else:
                break
        else:
            print("The value should be a digit!")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines ({MIN_LINE} - {MAX_LINE}): ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINE <= lines <= MAX_LINE:
                break
            else:
                print(f"The value should be btw ({MIN_LINE} - {MAX_LINE}):")
        else:
            print("The value should be a number!")
    return lines
                     
def get_bet():
    while True:
        bet = input("Bet: $")
        if bet.isdigit():
            bet= int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"The value should be btw ({MIN_BET} - {MAX_BET}):")
        else:
            print("The value should be a number!")
    return bet


def spin(amount):
    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > amount:
            print(f"You doesnt have enoug money depost ${amount} bet money ${total_bet}")
        else:
            break
    grid = get_slot_machine_spint(COLS,ROWS,symbol_count)
    print_slot_machine(grid)
    winnings,winning_line = check_winnings(grid,lines,bet,symbol_values)
    print(f"You won ${winnings}.")
    print("You won on lines: ",winning_line)
   
    return  winnings - total_bet
    
def main():
    amount = deposit()   
    while True:
        print(f"Current balance is: ${amount}")
        answer = input("Press enter to spin (q to quit).")
        if answer == 'q':
            break
        amount += spin(amount)
    print(f"You left with ${amount}")

main()