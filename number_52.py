def fibonacii(n,memo={}):
    if n in memo:
        return memo[n]
    
    if n<=1:
        return n
    
    memo[n] = fibonacii(n-1,memo) + fibonacii(n-2,memo)
    return memo[n]


if __name__=="__main__":
    n = int(input("enter the number: "))
    result = fibonacii(n)
    print(result)