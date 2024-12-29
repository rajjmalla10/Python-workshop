def reverseList(lst):
    count = len(lst) - 1
    new_lst = []
    while count >= 0:
        new_lst.append(lst[count])
        count -=1
    return new_lst

a = [1,2,3,4,5,6] 
print(reverseList(a))   
            
        