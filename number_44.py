class Node:
    def __init__(self,data:None, next:None, prev:None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_data(self,data):
        node = Node(data,self.head, None)
        self.head = node
        
    def end_insert_data(self,data):
        if self.head is None:
            self.head = Node(data, None,None)
            
        
        ltr = self.head
        while ltr.next:
            ltr = ltr.next
               
        ltr.next = Node(data,None,ltr)     
        
    def insert_data_list(self,data_list):
        if self.head is None:
            self.head = Node(data_list[0], None) 
        
        ltr = self.head
        for data in data_list:
            self.insert_data(data)
            
    def get_length_list(self):
        if self.head is None:
            print("linked list have no current values")
            return
        
        itr = self.head
        count = 0
        while itr:
            count +=1
            itr = itr.next
            
        return count        
            
    def reversing_linkedList(self):
        ltr = self.head
        prev = None
        
        if ltr is None:
            raise Exception ("No List found")
        
        if ltr.next == None:
            raise Exception ("Only one element on list")
        
        while ltr:
            next_node = ltr.next
            ltr.next = prev
            prev = ltr
            ltr = next_node
        
        self.head = prev  
        
    def print(self):  
        if self.head is None:
            print("Head doesn't exist!!")
            return
        
        itr =   self.head
        listStr = ""
        while itr:
            listStr +=  str(itr.data) + "-->"
            itr = itr.next
            
        print(listStr)
        
              
        
        
if __name__ == "__main__":
    lt = Linkedlist()
    lt.insert_data(20)        
    lt.insert_data(70)  
    lt.insert_data(30)  
    lt.insert_data(50)
    lt.reversing_linkedList()
    lt.print()
            
            
            
             
                 
            
               
                
                    
             
             