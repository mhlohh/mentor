class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"[{last.value}"
            while last.next is not None:
                last = last.next
                return_string += f",{last.value}"
            return_string += "]"
            return return_string
        
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            last = last.next
            counter += 1
        return counter

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.size = 1
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)
            self.size += 1

    def prepend(self, value):
        first = Node(value)
        first.next = self.head
        self.head = first
        self.size += 1

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                else:
                    last = last.next
            new_node = Node(value)
            new_node.next = last.next
            last.next = new_node 
            self.size += 1

    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
                return
        
        while last is not None:
            if last.next is not None and last.next.value == value:
                last.next = last.next.next
                return
            last = last.next

    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        last = self.head
        for i in range(index - 1):
            if last.next is None:
                raise ValueError("Index out of bounds")
            last = last.next
        if last.next is None:
            raise ValueError("Index out of bounds")
        last.next = last.next.next
        self.size -= 1

    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        last = self.head
        for i in range(index):
            if last.next is None:
                raise ValueError("Index out of bounds")
            last = last.next
        return last.value

    def print(self, index):
        last = self.head
        for i in range(index):
            if last.next is not None:
                print(last.value)
                last = last.next

if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(10)
    list1.append(5)
    list1.append(18)
    list1.append(11)
    list1.prepend(100)
    print(list1)


