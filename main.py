matchfield = {}     # Key = (Spalte, Zeile), Value = "O" oder "X"

COLUMNS: int = 7
LINES: int = 6
CELLS = COLUMNS * LINES


def get_int_input():
    while True:
        try:
            user_input = int(input("It´s your Turn (Column 0-6):"))
            if 0 <= user_input <= 6:
                return user_input
            else:
                print("Error: Please enter a valid number. Between 0 and 6 ")
        except ValueError:
            print("Error: Please enter a valid number.")

def ValidColumn(column):
    if (column, 0) in matchfield.keys():
        print("Error: Column is full")
        return False
    else:
        return True

def findDeppestCell (column):
    for line in reversed(range(LINES)):
        if (column, line)  not in matchfield:
            return line


while True:
    while True:
        column = get_int_input()
        if ValidColumn(column):
            break
    line = findDeppestCell(column)
    print(column, line)
    matchfield[column, line] = "O"