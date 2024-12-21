def smallestDivisor(n):
    d = 2 
    while d > 0:
        if n % d != 0:
            d += 1
        else:
            return d

def main():
    n = int(input("enter non negative number: "))
    print(smallestDivisor(n))

main()         
            
            