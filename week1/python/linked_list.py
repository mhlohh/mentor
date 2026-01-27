class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        
        self.head = None
        self.size = 0
    
    def __repr__(self):
        pass
    #O(n)
    def __contains__(self,value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

#O(n) Leniar Time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    #O(n) linear time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size = 1 
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = None(value)
            self.size += 1
            



   #O(n) Linear case
    def prepend(self,value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node


            

    def insert(self,value, index):
        if index == 0:
            self.prepend(value)
            self.size += 1
        else:
            if self.head == None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range (index -1):
                    if last.next is None:
                        raise ValueError("Index is out of bounds")
                    last = last.next
                
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node
                self.size += 1

    def delete(self, value):
        

    def pop(self, index):
        pass

    def get(self, index):
        pass

    def print(self):
        pass

    if __name__ == '__main__':
        pass

