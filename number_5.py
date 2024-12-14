
def add_daily_temp(daily_temp,weeks):
    for i in range(weeks):
        week={}
        for j in range(7):
            day = input(f"Enter the day of the week for day {j + 1} of week {i + 1} ").capitalize().strip() 
            if day not in week: 
                temp = int(input(f"Enter the average temperatur for the day {day} of the week {i + 1} "))
                week[day] = temp   # Add the day and its temperature to the week dictionary
            else:
                print("Average temperature already exist")
        
        daily_temp[str(i + 1)] = week            
                
                        
    return daily_temp    
          
             
    

daily_temp = {}    

weeks = int(input("enter the number of week to enter temperature data for: "))
result = add_daily_temp(daily_temp, weeks)
print(result)

