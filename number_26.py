# . Using Sums1toN.py as a prototype, write a program that prompts the user to enter a positive integer nMax and displays n and n! (n-factorial) for n from 1 to nMax.

def main():
    while True:
        try:
            nMax = int(input("enter a positive integer, so you can get its factorial: "))
            if nMax > 0:
                break
            else:
                print("You cannot enter number below 0 or negative integer")
        except ValueError:
            print("Invalid Input!!, Enter valid number")  
    
    n = 1
    while n <= nMax:
        fact = 1
        i = 1 
        while i <= n:
            fact *= i
            i += 1
        print(f"{n:3d} {fact:10d}")
        n +=1

if __name__ == "__main__" :
    main()           
            
            
                  
                    