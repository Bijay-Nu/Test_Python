number_of_rows=int(input('enter the number of the rows: '))

for row in range(1,number_of_rows+1):
    # space of th ros in teh table
    space = number_of_rows - row
    for spc in range(space):
        print(" " ,end="")
    # what characte should be showed in the outcome
    outcome = row + 1
    for out_come in range(1, outcome):
        print("* ", end="")
    print()