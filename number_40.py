def cretes(row,column):
    table = []
    i = 0
    while i < row:
        j = 0
        while j < column:
            table.append(column*[None])
            j+=1
        i+=1
    return table

print(cretes(1,1))        
    