#  Write and test a function that takes a list with four or more elements and returns the index of the element that makes the greatest sum with its left and right neighbors. Hint: a good solution here might be similar to your answer to Q1.

def test(lis):
    i = 1 
    max_value = -float('inf') 
    
    # print(-1000000000000000000000000000 > -float('inf'))  # True

    max_index = -1
    
    while i <= len(lis)-2:
        total = lis[i-1]+lis[i]+lis[i+1]
        if total > max_value:
            max_value = total
            max_index = i
        i+=1
    return max_index         


lis = [1,2,3,4,5,6]
print(f'List: {lis}')
print(f"\nThe index of the element that makes the greatest sum with its left and right neighbors: {test(lis)}th element")