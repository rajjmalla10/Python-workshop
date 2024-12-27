# Linked list  Adding at begining, at end, at any point of index,//// retrive length of list //// remove elements of desired index

class Node:
    def __init__(self,data:None,next:None):
        self.data = data
        self.next = next
        
class Linkedlist:
    
    def __init__(self):
        self.head = None   #head variable which points to the head of the linked list
        
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node #now my head is node which we assined through class
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        
        itr.next = Node(data,None)    
        return itr.next  
    
    def insert_values(self, data_list):
        if self.head is None:
            self.head = Node(data_list[0], None)
            
        itr= self.head 
        for data in data_list: #starting from secound element
            self.insert_at_end(data)
            
        pass
    
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
    
    def remove_element(self,index):
        if index < 0 or index >= self.get_length_list():
            raise Exception("Invalid Index")
             
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next 
                break
            itr = itr.next
            count += 1
            
    def insert_at(self, index,data):
        if index < 0 or index > self.get_length_list():
            raise Exception ("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning
            return
        
        ltr = self.head
        count = 0 
        while ltr:
            if count == index-1:
                node = Node(data,ltr.next)
                ltr.next = node
            ltr = ltr.next
            count+=1 
                
            
                
            
            
            
        
        
if __name__=="__main__":
    li = Linkedlist()
    li.insert_at_beginning(20)
    li.insert_at_beginning(30)
    li.insert_at_beginning(45)
    li.insert_values([11,12,14]) 
    li.insert_at(3,'Raj')
    li.insert_at_end(10)
    li.remove_element(5)
    print(li.get_length_list())
    li.print()       
        
    
        
