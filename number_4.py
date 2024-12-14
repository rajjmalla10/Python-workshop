import random


contestents = {}

class contestent:
    def __init__(self, name:str,address:str,mobile_no:str):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no
        
contestent_no = int(input("enter number of contestent: "))

def add_contestent():
    while True:
        name = input(f"Enter name of the contestent, press enter to stop: ")
        if name == "":
            break
        address = input(f"Address for the contestent{name}: ")
        mobile_no =  input(f"mobile_no for the contestent{name}: ")
    
        # Create a Contestant object and store it in the dictionary
        contestant_object = contestent(name,address,mobile_no)
        contestents_id = f"Contestent{len(contestents) + 1}"
        
        # contestant_object.name = "John"
        # contestant_object.address = "123 Elm St"
        # contestant_object.mobile_no = "123-456-7890"
        
        contestents[contestents_id] = vars(contestant_object)
        
        # {
        # 'name': 'John',
        # 'address': '123 Elm St',
        # 'mobile_no': '123-456-7890'
        # }
        
       


def menu():
    while True:
        print("Add contestent or Quit")
        print("enter 1 for 'Add Contestent'")
        print("2 for Determine Winner")
        print("3 to view current list of contestent")
        print("4 to delete contestents")
        print("5 To Exit!!")
        
        try:
            choicea  = int(input("Enter 1 to Add Contestant, 2 to Determine Winner, 3 to View Contestants, 4 to delete contestent and 5 to Exit!!: "))
        except ValueError:
            print("invalid input. please enter between 1 and 5.")
            continue
        
        if choicea  == 1:
            add_contestent()
        
        elif choicea == 2:
            pickk = input("enter 1 to determine the winner: ")
            if pickk == "1":
                select_winner()
            else:
                print("Returning to the main menu")    
                
         
        elif choicea == 3:
            print("Checking current list of contestents: ")
            view_menu()
            
        elif choicea == 4:
            print("Are you Sure want to Delete the contestent? : ")
            ans = input("Enter yes to delete and no to return: ").lower()
            if ans == "yes":
                Delete_contestant(contestents)
            else:
                print("Returning to main menu")           
        
        elif choicea == 5:
            print("exiting the menu")
            break
        
        else:
            print("Invalid choice pick 1 , 2 , 3 or 4 ")
        
        
            
def select_winner():

    if len(contestents) > 1:
                winner_key,winner = random.choice(list(contestents.items()))
                print("\nThe winner of the competition is : ")
                print(f"Contestant key: {winner_key}")
                print(f"The winner name is: {winner['name']}")
                print(f"The winner address is: {winner['address']}")
                print(f"The winner mobile_no is: {winner['mobile_no']}")
            
    else:
        print("Not enough candidate to determine the winner, should be more than 1.")    
               
def view_menu():
    if not contestents:
        print("No contestent added yet")
        return
    
    for index, details in contestents.items():
        print(f"Id:{index}:")
        print(f"Name: {details['name']}")
        print(f"address: {details['address']}")
        print(f"mobile_number: {details['mobile_no']}")
        print("-"* 20)
        
def Delete_contestant(contestents):
    key_to_remove = input("\n enter the contestent key to delete (e.g, contestent1): ").strip()
    key_to_remove = key_to_remove.capitalize()
    if key_to_remove in contestents:
        del contestents[key_to_remove] 
        print(f'contestent {key_to_remove} has been deleted.')
    else:
        print(f"contestent with {key_to_remove} does not exist")
         

menu()
