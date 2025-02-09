
from http.server import BaseHTTPRequestHandler
import json
import os
import tempfile


TASKS_FILE = 'tasks.json'

class TOdoHandler(BaseHTTPRequestHandler):
    
    

    tasks = []
    
    def load_Task(self):
        print('Loading tasks from file...')
        if os.path.exists(TASKS_FILE):
            print(f'file {TASKS_FILE}  exist')
            with open(TASKS_FILE,'r') as file:
                try:
                    data =  json.load(file)
                    if isinstance(data,list):
                        print(f'Loaded data: {data}')
                        return data
                    else:
                        print("File doesnt not contain a valid list. returning empty list")
                        return []
                except json.JSONDecodeError:
                    print("File is corrupt or empty. returning empty list")
                    return [] #return empty file if file is corrupt
        print(f'file  "{TASKS_FILE}"  Doesnot exist. Returning Empty List')
        return []     
    
    
    def save_tast_to_file(self,new_task):
        print("Saving new tasks to file...")
        
        existing_file = self.load_Task()
        print(f'Existing Tasks: {existing_file}')
        

        existing_file.append(new_task)
        print(f'Updated tasks:{existing_file}')
           
        try:
            with tempfile.NamedTemporaryFile('w', dir=os.path.dirname(TASKS_FILE), delete=False) as temp_file:
                json.dump(existing_file,temp_file, indent=4)
                temp_file_name = temp_file.name #full path of temp_file
        except IOError as e:
            print(f'Error writing to temporary file: {e}')
            return False
        
        #replace the original file now 
        #it is atomic if it happens in single step, otherwise the original file remains unchanged
        try:
            os.replace(temp_file_name,TASKS_FILE)
        except IOError as e:
            print(f'Error replacing file : {e}')
            return False  
        
        print(f'Task saved to "{TASKS_FILE}" ')
        return True      
                        
        
    def max_id(self):
        tasks = self.load_Task()
        if not tasks:
            return 0 
        else:
            return max((task.get('id',0)for task in tasks), default=0)
        
    def do_PATCH(self):
        path_url = self.path.strip('/').split('/')
        if len(path_url) == 2 and path_url[0] == 'task':
            content_length = int(self.headers.get('content-length',0))
            if content_length == 0:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Empty request body")
                return
            
            body = self.rfile.read(content_length).decode("utf-8")
            
            try:
                update_tasks = json.loads(body)
                
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write("Invalid Json")
                return
            
            tasks = self.load_Task()
            task_id = path_url[1]
            
            if task_id.isdigit():
                task_id = int(task_id)
                
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid Task ID")
                return    
            
            tasks_found = None
            
            for task in tasks:
                if task['id'] == task_id:
                    tasks_found = task       
                    break
            
            if not tasks_found:
                self.send_response(404)
                self.send_header()
                self.wfile.write(b"Task not found")
                return
                  
                
            for key , value in update_tasks.items():
                if key in tasks_found  and value is not None: #update_task is what we recieved from client -side
                    tasks_found[key] = value
                    
            try:
                with tempfile.NamedTemporaryFile('w', dir=os.path.dirname(TASKS_FILE), delete=False) as temp_file:
                    json.dump(tasks,temp_file,indent=4)
                    temp_filename = temp_file.name
                    
                os.replace(temp_filename,TASKS_FILE) #renames the temporary file temp_filename to the original file name that is TASK_FILE
                
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Task updated Sucesfully!!")
                
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Task not found")
                    
                
 
    
    def do_POST(self):
        print("Post revieved request at:", self.path)
        if self.path == "/tasks/create":
            content_length = int(self.headers['Content-Length']) # Get the length of the data
            post_data = self.rfile.read(content_length).decode('utf-8') #read contact length in bytes from the request boody 
        
            try:
                task = json.loads(post_data)
                
                if 'title' not in task or 'description' not in task:
                    self.send_error(400, "Missing required fileds: 'title' and 'description'.")
                    return
                
                new_id = self.max_id()
                
                
                new_task = {
                    "id": int(new_id) + 1,
                    "title": task["title"],
                    "description":task["description"]  
                }
                
                print("Calling save_tast_to_file...")
                self.save_tast_to_file(new_task)
                print(f'\n Json file : {TASKS_FILE}')
                
                
                self.tasks.append(new_task)
                
                self.send_response(201)
                self.send_header('Content-Type','application/json')
                self.end_headers()
                
                response = json.dumps({'message':"Task Created Sucesfully",'task':new_task})
                self.wfile.write(response.encode('utf-8'))
                
            except json.JSONDecodeError:
                self.send_error(400,"invalid json format")
            except Exception as e:
                self.send_error(500,f"server error: {str(e)}")        
    
    def do_GET(self):
        path_parts = self.path.strip("/").split("/")
        
        if len(path_parts) == 1 and path_parts[0]== "tasks":
            tasks = self.load_Task()
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            response = json.dumps(tasks)
            self.wfile.write(response.encode('utf-8'))
            
        elif len(path_parts)==2 and path_parts[0] == "tasks":
            task_id = path_parts[1]
            
            
            if task_id.isdigit():
                task_id = int(task_id)
                datas = self.load_Task()
                
                if isinstance(datas,list):
                    
                
                
                    found_task = None    
                    for task in datas:
                        if task['id'] == task_id:
                            found_task = task
                            break
                    
                    if found_task:
                        self.send_response(200)
                        self.send_header('Content-Type','application/json')
                        self.end_headers()
                        
                        response = json.dumps(found_task).encode()            
                        self.wfile.write(response)     
                    else:
                        self.send_error(404,'Task Not Found')
                
                else:
                    self.send_error(500)
                    self.end_headers()
                    self.wfile.write(b"Internal Server Error: Invalid data format")        
            else:
                self.send_response(400)    
                self.end_headers()
                self.wfile.write(b"Invalid Task Id") 
                                  
            
    def do_DELETE(self):
        path_parts = self.path.strip("/").split("/")
        
        if len(path_parts) == 3 and path_parts[0] == 'tasks':
            task_id = path_parts[-1]
            
            if task_id.isdigit():
                task_id = int(task_id)
                
            get_task = self.load_Task()
            
            if get_task is None:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Could not load the json file in do_delete method")
                return
            
            if isinstance(get_task,list):
                
                new_task = []
                if get_task:
                    for task in get_task:
                        if task['id'] != task_id:
                            new_task.append(task)
                    
                            
                            
                elif len(new_task) == len(get_task):
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"Task not found")
                    return 
                
                
                try:
                    with tempfile.NamedTemporaryFile("w", dir=os.path.dirname(TASKS_FILE), delete=False) as temp_file:
                        json.dump(new_task, temp_file, indent=4)
                        tempfilename = temp_file.name
                        
                    os.replace(tempfilename, TASKS_FILE)
                    
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b"Task deleted sucesfully")
                    
                except Exception as e:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(f"Error deleting task: {str(e)}".encode('utf-8')) 
        
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid Request")                                   
                        
               
                
                
                
                    