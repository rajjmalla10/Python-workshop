from http.server import BaseHTTPRequestHandler
import json
import os



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
           
        
        with open(TASKS_FILE,"w") as file:
            json.dump(existing_file,file, indent=4)
                
        print(f'Tasks saved to "{TASKS_FILE}"')        
        
           
    
    def do_POST(self):
        if self.path == "/tasks":
            content_length = int(self.headers['Content-Length']) # Get the length of the data
            post_data = self.rfile.read(content_length) #read contact length in bytes from the request boody 
        
            try:
                task = json.loads(post_data)
                
                if 'title' not in task or 'description' not in task:
                    self.send_error(400, "Missing required fileds: 'title' and 'description'.")
                    return
                
                
                
                
                new_task = {
                    "id": len(self.tasks) + 1,
                    "title": task["title"],
                    "description":task["description"]  
                }
                
                
                self.save_tast_to_file(new_task)
                
                
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
        pass            
                
                
                
                    