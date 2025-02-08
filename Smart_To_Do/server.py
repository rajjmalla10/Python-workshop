from http.server import HTTPServer
import logging

from Smart_To_Do import todo


class MainApp:
    def __init__(self):
        #initialize components 
        # self.db = database()
        self.server= HTTPServer(("localhost",8080),todo.TOdoHandler)
        self.logger = logging.getLogger('main')
        logging.basicConfig(level = logging.DEBUG)
    
    def run(self):  
        self.logger.info("Starting the server...")  
        # self.db.connect()
        self.server.serve_forever()
        # This is the part of the program that makes the app interactive—it waits for requests (like a user accessing localhost:8080) and responds with data accordingly.
        # The server will keep running indefinitely until you manually    stop it (e.g., by pressing Ctrl+C in your terminal)

    
if __name__=="__main__":
    app = MainApp()
    app.run()        