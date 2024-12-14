from number_7 import get_daily_temps 

def get_weekend_average_temp(result):
    count = 0
    avg_temp = 0 
    for week, day in result.items():
        saturday_temp = day.get('Saturday',0)
        sunday_temp = day.get('Sunday',0)
        count += 2
        
        # add to total temperature
        avg_temp += saturday_temp + sunday_temp
    return avg_temp / count if count > 0 else 0   
        
        
    


if __name__=="__main__":
    
    try:
        num_weeks = int(input("enter number of weeks: "))
        if num_weeks <= 0 :
            raise ValueError("Number of weeks should not be less than 1")
        result = get_daily_temps(num_weeks)  
        print(result)    
        
        print(f"\nThe average temp of the week end is : {get_weekend_average_temp(result)}*C")
    except ValueError as e:
        print(f"Invalid entry: {e}")    
        
        
                   