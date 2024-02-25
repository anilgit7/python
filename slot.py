import random
ROWS=3
COLS=3
symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_win(columns,lines,bet,values):
    win=0
    win_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_check=column[line]
            if symbol!= symbol_check:
                break
        else:
            win+=values[symbol]*bet
            win_line.append(line+1)
    return win, win_line   

def slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

min_bet=1
max_bet=100
max_lines=3
def get_deposite():
    while True:
        amount=input("enter the amount you want to deposite $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Number should be greater than zero.")
        else:
            print("enter the number")
    return amount

def get_lines():
    while True:
        line=input("enter the number of lines to bet on (1-"+str(max_lines)+") ")
        if line.isdigit():
            line=int(line)
            if 1<=line<=max_lines:
                break
            else:
                print(f"Number of lines should be between 1 and {max_lines}.")
        else:
            print("enter the number")
    return line

def get_bet():
    while True:
        amount=input(f"enter amount to bet ({min_bet}-{max_bet}) ")
        if amount.isdigit():
            amount=int(amount)
            if min_bet<=amount<=max_bet:
                break
            else:
                print(f"Amount must be between {min_bet} and {max_bet} ")
        else:
            print("enter the number")
    return amount

def main():
    balance=get_deposite()
    while True:
        play=input("Want to play(y/n): ")
        if play.lower()=="y":
            lines=get_lines()
            while True:
                bet=get_bet()
                total= bet*lines
                if total>balance:
                    print(f"you dont have enough balance. you have ${balance}")
                else:
                    break
            print(f"you bet {bet} on {lines} lines, total of ${total}")

            slots=slot_machine(ROWS,COLS,symbol_count)
            print_slot(slots)
            winning,win_line=check_win(slots,lines,bet,symbol_value)
            print(f"You won ${winning}")
            print(f"You won on lines: ",*win_line)
            balance=balance-total+winning
            print(f"Your total balance is ${(balance)}")
        else:
            print("THANK YOU FOR PLAYYING!!")
            break

main()