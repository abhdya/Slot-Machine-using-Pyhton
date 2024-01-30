import random

MAX_LINES = 3 # maximum no of lines in the slot machine
MAX_BET = 100 # maximum bet a user can make
MIN_BET = 1 # minimum bet a user can make

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: #used when we didnt break from second for loop
            winnings = values[symbol] * bet
            winning_lines.append(lines + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(cols, rows, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items() gives us the access to iterate through dictionary by both key and value pair
        for _ in range(symbol_count):
            all_symbols.append(symbol) # TO explain A is appended 2 times, B is appended 4 times and so on

    columns = []
    curr_list = all_symbols[:] #copies the list
    
    # The for loop below randomly selects the output at that moment and at the same time ensures that other column doesnt give same element as output by deleting it from the list
    for col in range(cols):
        column = []
        for row in range(rows):
            value = random.choice(curr_list)
            curr_list.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    # Here we will be doing transposing of matrix and printing it, that means the horizontally present elements will be printed vertically
    # if initial output was [0,0,0]
    #                       [1,2,4]
    #                       [3,3,4]
    # it will be printed as [0,1,3]
    #                       [0,2,3]
    #                       [0,4,4]
    
    for row in range(len(columns[0])):
        for i,col in enumerate(columns): # enumerate gives us the index and the item at that particular index
            if i != len(columns) -1:
                print(col[row], end = " | ") # '|' is used to seperate the output values in matrix
            else:
                print(col[row], end = '')

        print()


def deposit():
    while True: # We are going to continuously ask user to enter an amount until they give me a valid amount
        amount = input("What would you like to deposit??? $")
        # Chceking if input amount is a number
        if amount.isdigit(): # isdigit() tells if entered amount is a valid whole number. It will be wrong if entered amount is -ve or decimal 
            amount = int(amount) # convert string amount to integer
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: # isdigit() returns false when string is entered
            print("Please enter a number.")

    return amount


def get_no_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (1 - " + str(MAX_LINES) + ")??? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Please enter valid no of lines.")
        else:
            print("Please enter a number.")
    
    return lines


def get_bet():
    while True: 
        amount = input("What would you like to bet each line??? $")
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else: 
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_no_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet, your current balance is ${balance}")
        else:
            break
            
    print(f"You are betting ${bet} on {lines} lines. Total bet amount is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.") 
    print(f"You won on lines : ", *winning_line)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press ENTER to play (q to quit)")
        if ans == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()