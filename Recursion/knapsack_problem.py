def knapsack_prob(items,max_weigth):
    
    table = [[0 for _ in range(max_weigth+1)] for _ in range(len(items)+1)]
    for row in range(1, len(items)+1):
        items_profit = items[row]['profit']
        items_weight = items[row]['weight']
        for col in range(max_weigth+1):
                
            if col >= items_weight:
                 table[row][col] = max(table[row-1] [col],
                                       table[row-1][col-items_weight] + items_profit )
            
                 
            else:
                table[row][col] = table[row-1][col]  
                
    selected_items = []                 
    weig = max_weigth
    for row in range(len(items),0,-1):
        
        if  table[row][weig] != table[row-1][weig]:
            selected_items.append(row)
            weig -= items[row]['weight']
                   
    
    return selected_items     
    


def main():
    items= {}
    max_weigth = 8
    num_items = int(input("enter number of items: "))
    for i in range(1, num_items+1):
        items_weight = int(input(f"enter the weight of the item {i}: "))
        items_profit = int(input(f"enter the profit of the item {i}: "))
        items[i] = {"profit" : items_profit , "weight": items_weight}
        
    print(items)
    print(knapsack_prob(items,max_weigth))

if __name__=="__main__":
    main()
    
    