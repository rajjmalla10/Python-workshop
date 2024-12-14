from number_5 import add_daily_temp

def moderate_days(daily_temp):
    result = {}
    for week, days in daily_temp.items():
        filterd_day={}
        for day, temp in days.items():
            temp_as_int = int(temp)
            if 70 <= temp_as_int <= 79:
                filterd_day[day] = temp_as_int
        if filterd_day:
            result[week] = filterd_day        
    return result

if __name__ == "__main__":
    print("hello world \n")
    daily_temp = {}
    
    try:
        weeks = int(input("Enter the number of weeks to enter temperature data for: "))
        if weeks <= 0 :
            raise ValueError("Number of week should be greater than 0")
    except ValueError as e:
        print(f"Invalid input: {e}") 
    else:
        daily_temp = add_daily_temp(daily_temp, weeks)
        print(f"Temperature data collected: {daily_temp}")  # Add this print statement
    
        days_in_range = moderate_days(daily_temp)
        
        print("\nDays with an average temperature between 70 and 79°F:")
        if days_in_range:
            for week, day, temp in days_in_range.items():
                print(f"Week {week}, Day {day}: {temp}°F")
        else:
            print("No days found in this temperature range")
