# Write a function called intersection that takes 2 lists of integers and returns a third list values that occur in both lists ie. intersection([2, 3, 4], [1, 2, 5]) should return [2]. Write your solution in pure Python to show the logic in your solution, do not use any library functions.

def intersection(lis1,lis2):
    i = 0
    inter = []
    while i < len(lis1):
        temp1 = lis1[i]
        j = 0
        while j < len(lis2):
            if temp1 == lis2[j]:
                if temp1 not in inter:
                    inter.append(temp1)
            j+=1
        i+=1    
    return inter    


def optimized_intersection(lis1,lis2):
    set_lis2 = set(lis2)
    return [x for x in lis1 if x in set_lis2]
        
    


lis1 = [1,2,3,4]
lis2 = [4,5,6,1]
print(intersection(lis1,lis2))
print(optimized_intersection(lis1,lis2))
