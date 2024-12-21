def perfectDivisor(n:int)-> int:
    i = 1 
    sumDivs =0
    while i < n:
        if n % i == 0:
            sumDivs += i
        i+=1
    if sumDivs == n:
        return True  # It's a perfect number
    else:
        return False   
     
def next_perfect(n:int)->int:
    n+=1
    while not perfectDivisor(n):
        n+=1
    return n        
    
def main():
    n = int(input("enter number : "))
    result = next_perfect(n)
    print(f"the next perfect number {n} is : {result}")
    
main()               