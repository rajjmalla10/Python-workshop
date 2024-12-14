def add_vegetable(empty_vegetable,update_vegetable):
    
    if update_vegetable in empty_vegetable:
        raise ValueError(f"The vegetable already exist")
    
    else:
        empty_vegetable.add(update_vegetable)
             
    return empty_vegetable
    
    
    
    
empty_vegetable = {'Carrot','Redish','Potato'}    
update_vegetable = 'Carrot'

result = add_vegetable(empty_vegetable,update_vegetable)
print(f'Updated Result: {result} ')