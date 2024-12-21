def square(n):
    i = 1
    while i < n + 1:
        if i == 1 or i == n:
            print("*" * n)
        else:
            print(f"*{' ' * (n - 2)}*")    
        i += 1
def main():
    n = int(input("enter any number: ")) 
    square(n)
main()           