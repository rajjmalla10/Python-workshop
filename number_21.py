class Student():
    def __init__(self,first_name, last_name, roll_number):
        self.first_name = first_name
        self.last_name = last_name 
        self.roll_number = roll_number
        
    def __str__(self):
        return f"{self.first_name, self.last_name, self.roll_number}"    

    def display(self):
        return f"{self.first_name, self.last_name, self.roll_number}"  
    
student = Student('Raj','Malla',21)   
print(student)       