def sumDigits(n: int) -> int:
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i +=1
    return sum

def main():
    n = int(input("enter a positive number:"))
    result = sumDigits(n)
    if result == result:
        print("No valid divisor exist for number less than or equal to 1")
    else:
        print(result)       

main()        
    