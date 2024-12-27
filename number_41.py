def greatest(a:list)-> list:
    if not a:
        return None
    max_value = a[0]
    i = 0
    while i < len(a):
        if max_value < a[i]:
            max_value = a[i]
        i+=1
        
    return max_value            
        
                
     
       
a= [1,2,3,4,5]        
print(greatest(a))        