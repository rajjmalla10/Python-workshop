def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left] , lst [right] = lst[right], lst[right]
        left +=1
        right -=1
      
a = [1,2,3,4,5,6] 
print(reverse_list(a))           
        