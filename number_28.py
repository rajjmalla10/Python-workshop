def printSqare(n):
    i = 0
    while i < n:
        if i == 0 or i == n-1:
            print(f"{n * '*'}")
        else:
            print(f"{'*'} {(n-4) * ' ' } {'*'}")
        i +=1
        
printSqare(5)