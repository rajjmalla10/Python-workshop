def myPow(x,n):
    result = 1 
    counter = n
    while counter > 0:
        result *= x
        counter -= 1
    return result    
             

x = int(input("enter a non negative integer: "))
n = int(input("enter a non negative integer, which act as power of x"))
print(myPow(x,n))

