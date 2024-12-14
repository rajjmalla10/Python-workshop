def get_daily_temps(num_weeks):
     weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
     avg_temp={}
     for week in range(1, num_weeks+1):
         daily_temp = {}
         
         for days in weekdays:
             while True:
                  try:
                     temp = float(input(f"enter average temperature for the day {days} "))
                    
                     daily_temp[days] = temp
                     break
                  except ValueError:
                     print("try endering a valid temperature value,")
                
         avg_temp[week] = daily_temp    
     return avg_temp
 
if __name__=="__main__":
    try:
        num_weeks = int(input("enter number of weeks: "))
        if num_weeks <= 0 :
            raise ValueError("Number of weeks should not be less than 1")
        result = get_daily_temps(num_weeks)  
        print(result)    
    except ValueError as e:
        print(f"Invalid entry: {e}")    
                   
         
         
        