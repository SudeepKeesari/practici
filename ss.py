#patterns using loops
rows=int(input("rows: "))
for i in range(0, rows):
    for j in range(0, i+1):
        print("*",end=" ")
    print()

    