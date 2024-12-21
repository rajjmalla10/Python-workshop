# 4. Write a program that prints n,  s1(n)=∑k=1nk  ,  s2(n)=∑k=1nk2  , and  3s2(n)s1(n)  for n = 1, 2, 3, ..., 20. Try to guess the general formula for  ∑k=1nk2  from the resulting table.

def main():
    n = 20 
    k = 1
    while k <= n:
        s1 = 0
        s2 = 0
        i = 1 
        while i <= k:
            s1 += i 
            s2 += i ** 2
            i += 1
        s3 = 3 * s2 / s1    
        print(f'{k:3d} {s1:8d} {s2:8d} {s3:15.2f}') 
        k+=1   
        
if __name__=="__main__":
    main()       