def squaredSum(n : list) -> int:
    i = 0 
    sum = 0
    while i < len(n):
        n[i] *= n[i]
        sum += n[i]
        i+=1
    return sum    
def main():
    liste = input("enter numbers: ")
    n = list(map(int, liste.split()))
    print(squaredSum(n))
    
main()    