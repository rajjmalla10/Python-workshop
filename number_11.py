import json

def main_menu():
    stud_grades = {}
    modules = ['4CS001','4CS015','4C1018'] 
    print("\n Welcome!! Would you like to add or view grades of the students? ")
    
    while True:
        view_add = input("If you like to add then enter // add  // or If you like to view then enter // view // or press //Enter// to exit: ").lower()
        
        try:
            if view_add == "add":   
                num_students = int(input("Enter number of students Your want to add grades for: "))
                add_student(stud_grades,modules,num_students)
                
        
            
            elif view_add == "view": 
                students_grades = view_student()
                if students_grades:
                    print(f"Student Data:{students_grades}")
                else:
                    print("No data was Found")
                    
            elif view_add == "":
                print("You Exit The Main Menu")
                break
            else:
                print("You can either enter 'add' to add students, 'view' to view students, '' or enter to exit main menu")    
        except ValueError as e:
            print(f"Error: {e}, Please enter Valid number of students")                        
            
              
    
def add_student(stud_grades,modules,num_students):
    for _ in range(num_students):
        name = input("Enter name of the student: ")
        if name == "":
            break
        grades = {}
        for module in modules:
            while True:
                try:
                    mark = float(input(f"Enter mark for the module {module} "))
                    if 0 < mark <= 100:
                        grades[module] = mark
                        break
                    else:
                        print("Please enter a mark between 0 and 100")
                except:
                    print("Invalid input! Please enter a numeric value.")        
        stud_grades[(f"{name}")] = grades 
    
    with open("student.json",'w') as file:
        json.dump(stud_grades,file,indent=4)
          
    return stud_grades
    
def view_student():
    try:
        with open("student.json", 'r') as f:
            stud_data = json.load(f)    
                   
        if not stud_data:
            print("There are no students Data present on Json File")
        else:
            return stud_data   
    
    except FileNotFoundError: 
        print("The Json file doesnt exist")
    except json.JSONDecodeError:
        print("The file is not a valid json format or is corrupt")          
    
         
            
        

 


result = main_menu()
