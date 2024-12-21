def perfectDivisor(n:int)-> int:
    i = 1 
    sumDivs =0
    while i < n:
        if n % i == 0:
            sumDivs += i
        i+=1
    if sumDivs == n:
        return(f"It is a perfect divisior: {sumDivs}")
    else:
        return(f": {sumDivs}It is not a perfect divisior") 
    
def main():
    n = int(input("enter number : "))
    result = perfectDivisor(n)
    print(result)
    
main()               