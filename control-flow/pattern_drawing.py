size = int(input("Enter the size of the pattern:"))
row = 1

while row <= size:    # outer loop for rows
    for col in range(size):    # inner loop for columns
        print("*", end="")
    print()    # move to next line after each row
    row += 1
