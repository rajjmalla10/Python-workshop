

from http.server import HTTPServer
import json

import logging
import requests





def main():
    
    print("\nPress - 1 : If you want to create New Task.")
    print("Press - 2 : If you want to View Existing Tasks.")
    print("Press - 3 : If you want to View Existing Task By its ID.")
    print("Press - 4 : If you want to Update Existing Task.")
    print("Press - 5 : If you want to Delete Existing Tasks.")
    print("Press - 6 : If you want to Delete Existing Tasks by ID.\n")
    
    Choice = input("Enter the number: ")

    if Choice == '1':
        title = input("enter the title of your Task: ")
        description = input("Enter Description for your task: ")
        
        task_data = {"title": title , "description": description}
        
        send_data = requests.post("http://localhost:8080/tasks",json= task_data)
        
        if send_data.status_code == 201:
            print("Task Created Sucesfully!!")
        else:
            print(f"Failed:{send_data.status_code}") 
               
            
        
        print("\nServer Response: ",send_data.json())
        
        
        
    
    pass

if __name__=="__main__":
    print("\nWelcome to Smart TODO Managment!!")
    print("We faciliate task to be Created, view, update and delete.")
    main()
    