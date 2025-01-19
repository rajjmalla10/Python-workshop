def knapsack_prob(items):
    max_weigth = 8
    table = [[0 for _ in range(max_weigth+1)] for _ in range(len(items)+1)]
    for row in range(1, len(items)+1):
        items_profit = items[row]['profit']
        items_weight = items[row]['weight']
        for col in range(max_weigth+1):
            
            
            
            if row == 0 or col == 0:
                table[row][col] = 0
                
            elif col < items_weight:
                 table[row][col] = max(table[row-1] [col],
                                       table[row-1][col-items_weight] + items_profit )
            
                 
            else:
                table[row][col] = table[row-1][col]       
    
    return table[len(items)+1][max_weigth]
            
           
                   

def main():
    items= {}
    num_items = int(input("enter number of items: "))
    for i in range(1, num_items+1):
        items_weight = int(input(f"enter the weight of the item {i}: "))
        items_profit = int(input(f"enter the profit of the item {i}: "))
        items[i] = {"profit" : items_weight , "weight": items_profit}
        
    print(items)
    print(knapsack_prob(items))

if __name__=="__main__":
    main()
    
    