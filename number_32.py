def Square(m,n):
    i = 0
    while i < m:
        print('*' * n)
        i+=1 

def main():
    m = int(input("enter number of row: "))
    n = int(input("enter number of row: "))
    Square(m,n)

main()    