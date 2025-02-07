# Doubly Linked list ,/// Print_forward // Print forward from desired index, same for backward as well,/// insert at end, ///insert after value given by user/// remove the value provided by the user

class Node:
    def __init__(self,data:None,next:None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedlist():
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self,data):
        if self.head is None:    
            node = Node(data,self.head,None)
            self.head = node 
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node       

    def print_forward(self):
        if self.head is None:
            raise Exception("No value exist!!")
        
        ltr = self.head
        lisStr = ''
        while ltr:
            lisStr +=   str(ltr.data) + ' <-- --> '
            ltr = ltr.next
        print(lisStr)
        
    def print_backward(self,index_head = None ):
        if self.head is None:
            raise Exception("Invalid Node!!")
        
        ltr = self.head
        
        if index_head is None:
            raise Exception("No value passed of index!!")
        elif index_head == 0:
            print("No element before the head!")
            return None
        
        else:
            count = 0 
            while ltr and count < index_head - 1:
                ltr = ltr.next
                count +=1
                
        result = ''
        while ltr:
            result += str(ltr.data) + ' <-- '
            ltr=ltr.prev 
        print(result)     
        
    def insert_end(self,data):
        if self.head == None:
            self.insert_at_begining(data)
            return 
            
        ltr = self.head
        
        while ltr.next:
            ltr = ltr.next
            
        ltr.next = Node(data,None,ltr)
        
        
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            raise Exception("No element exists currently!!")
        
        ltr = self.head
        while ltr:
            if ltr.data == data_after:
                node = Node(data_to_insert,None,ltr)
                
                if ltr.next:
                    ltr.next.prev = node
                    
                ltr.next = node
                print(f"Insert {data_to_insert} after {data_after}")
                self.print_forward()
                break
            
            
            ltr = ltr.next
        
        else:
            raise ValueError(f"'{data_after}' not found in the list")
        
        
        
    
    def print_forward_index(self,Index:None):
        if self.head is None:
            raise Exception("No value added!!") 
        
        length = self.length_of_dblinkedlist()
        if Index < 0 or  Index >= length:
            raise Exception("Invalid Index")
        
        ltr = self.head
        count = 0
        result = '' 
        while ltr:
            
            if count == Index:
                while ltr:
                    result += str(ltr.data) + ' <-- --> '
                    ltr = ltr.next
                print(result)
                return  
                
            ltr = ltr.next
            count +=1
            
        raise Exception("Invaid Index")    
            
    

    def length_of_dblinkedlist(self):
        if self.head is None:
            raise Exception("No Node currently!!")
        
        ltr =self.head
        count = 0
        while ltr:
            ltr = ltr.next
            count += 1
        return count      
        
    def remove_byvalue(self,value_to_remove):
        if self.head is None:
            raise Exception ("Invalid head!!")
        
        ltr = self.head
        while ltr:
            if ltr.data == value_to_remove:
                
                if ltr.prev and ltr != self.head:
                    ltr.prev.next = ltr.next
                    print(f"Removed {value_to_remove}, New Double Linked list")
                    self.print_forward()
                    break
                
                if ltr == self.head:
                    self.head = ltr.next
                    if self.head:
                        self.head.prev = None
                    return 
            ltr = ltr.next 
                

        # ltr = self.head
        # strLis = ''
        # while ltr:
        #     lisStr += str(ltr.data) + ' <-- '
        #     ltr = ltr.prev
        # print(strLis)        
        
if __name__ == "__main__":
    dlist = DoublyLinkedlist()  
    dlist.insert_at_begining(10)
    dlist.insert_at_begining(20)
    dlist.insert_at_begining(40)
    dlist.insert_end(4)
    dlist.print_forward()
    dlist.print_backward(2)
    dlist.insert_after_value(10,'Raj')
    dlist.remove_byvalue(20)
    print(dlist.length_of_dblinkedlist())
    dlist.print_forward_index(2)
    
    
            
            
            
                
