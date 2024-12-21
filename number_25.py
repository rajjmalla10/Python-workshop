def main():
    while True:
        try:
            n = int(input("Enter number of integer u want multiple of:"))
            if n > 0:
                break
            else:
                print("Enter positive integer, Non negative real number")
        except ValueError:
            print("Invalid input. please enter a valid positive integer")
                
    
    multiple = 6 
    while multiple <= n:
        print(multiple)
        multiple +=6
        
if __name__=="__main__":
    main()        
    
            
            
         
        
                    