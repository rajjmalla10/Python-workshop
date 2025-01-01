
def compound_intrest(p, r ,t,headings):
    print(f"\n{headings[0]:<10} {headings[1]:<10} {headings[2]:<15} {headings[3]:<10} {headings[4]:<10}")
    print("-" * 60)
    
    
    rate = r / 100
    quarterly_rate = rate / 4 
    
    for year in range(1,t+1):
        for period in range(1, 5):
            old_amount = p
            new_amount = p*(1 + quarterly_rate) 
            Quaterly_Intrest = new_amount-old_amount
            print(f"{year:<10} {period:<10} {old_amount:<15.2f} {Quaterly_Intrest:<10.2f} {new_amount:<15.2f}")
            p = new_amount
   
            
        
    
    
def main():    
    
    print("\nWelcome to the Raj's compound intrest calculator.\nThis program calculates your potential return when you invest with us.\n")
    Principle = (int(input("How much would you like to invest with us? ")))
    Intrest_rate = (float(input("what is the intrest rate of your account? ")))
    Timee = (int(input("How long are you planning to invest (in years)? ")))
    
    headings = ['Year', 'Period', 'Old_Balance', 'Intrest', 'New_Balance']  
    
    compound_intrest(Principle,Intrest_rate,Timee,headings) 
    final_amount = Principle * (1 + Intrest_rate / 100 / 4) ** (4 * Timee)

    print(f"£{Principle} at {Intrest_rate}% for {Timee} years compunded 4 times per year is: £{final_amount:.2f}")



if __name__ == "__main__":
    main()    
    
    