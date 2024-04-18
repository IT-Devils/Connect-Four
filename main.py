matchfield = {}     # Key = (Spalte, Zeile), Value = "O" oder "X"
                    # Key = (Column, Line) , Value = "O" or "X"
COLUMNS: int = 7
LINES: int = 6
CELLS = COLUMNS * LINES
DIRECTIONS = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
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

def printMatchField():
    for i in range(CELLS):
        if i % COLUMNS == 0:
            print()
        position = (i % COLUMNS, i // COLUMNS)
        if position in matchfield:
            print(matchfield[position],end=" ")
        else:
            print(".",end=" ")

def win(player):
    stone = "O" if player else "X"
    for pos in matchfield:
        for dir in DIRECTIONS:
            connect_four = True
            for i in range(4):
                column, line = pos
                delta_column, delta_line = dir
                p1 = (column + delta_column+i, line + delta_line*i)
                if p1 in matchfield and matchfield[p1] == stone: continue
                connect_four = False
                break
            if connect_four:
                return True

player = True

while True:
    printMatchField()
    while True:
        column = get_int_input()
        if ValidColumn(column):
            break
    line = findDeppestCell(column)
    matchfield[column, line] = "O" if player else "X"
    if win(player):
        printMatchField()
        print("You've won!")
        break
    player = not player