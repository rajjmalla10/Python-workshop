

from http.server import HTTPServer
import json

import logging
import requests



def create_task(title,description):
    task_data = {"title": title , "description": description}
        
    send_data = requests.post("http://localhost:8080/tasks/create",json= task_data)
        
    if send_data.status_code == 201:
        print("Task Created Sucesfully!!")
    else:
        print(f"Failed:{send_data.status_code}") 
               
            
        
    print("\nServer Response: ",send_data.json())
    
def get_tasks():
    get_data = requests.get('http://localhost:8080/tasks')
    if get_data.status_code == 200:
        tasks = get_data.json()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Task: {task['title']}, Description: {task['description']}")
            
        
def get_taskID(id):
    task_id = id
    get_data = requests.get(f'http://localhost:8080/tasks/{task_id}')
    if get_data.status_code == 200:
        tasks = get_data.json()
        if tasks:
            print(f"ID: {tasks['id']}, Title: {tasks['title']}, Description: {tasks['description']}")
            
        
        
    


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
        
        create_task(title,description)
        
    if Choice == '2':
        get_tasks()    
        
    if Choice == "3":
        get_id = int(input("Enter the ID of the task you want to retrieve: ex: 1,2,3 ..."))
        get_taskID(get_id)    
        
        
        
    
    pass

if __name__=="__main__":
    print("\nWelcome to Smart TODO Managment!!")
    print("We faciliate task to be Created, view, update and delete.")
    main()
    