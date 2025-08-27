from termcolor import colored

board = []
for i in range(8):
    if i == 1 or i == 6:
        row = [colored("b", "red") for i in range(8)]
    else:
        row = ["." for i in range(8)]

    board.append(row)
for row in board:
    print("| " + " | ".join(row) + " |")
