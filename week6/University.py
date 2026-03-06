from abc import ABC, abstractmethod
class LibraryUser(ABC):
    def __init__(self,name,books):
        self.name = name
        self._book = books
    
    @property
    def book(self):
        return self._book

    @abstractmethod
    def borrow_limit(self):
        pass

class StudentMember(LibraryUser):
    def __init__(self, name, books):
        super().__init__(name, books)
        self.limit = 5
    def borrow_limit(self):
        return f"Student can take {self.limit} books"
    
    
class FacultyMember(LibraryUser):
    def __init__(self, name, books):
        super().__init__(name, books)
        self.limit = 25
    def borrow_limit(self):
        return f"Faculties can take {self.limit} books"
    
s1 = StudentMember("Mushil NR","Alice in a Wonder Land")
print(f"{s1.borrow_limit()}")
t1 = FacultyMember("Athulya","Avengers")
print(f"{t1.borrow_limit()}")