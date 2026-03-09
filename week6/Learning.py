from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,standard,module,course):
        self._name = name
        self._standard = standard
        self._module = module
        self.course = course
    @property
    def name(self):
        return self._name
    
    @property
    def stadart(self):
        return self._standard
    
    @property
    def module(self):
        return self._module
    @abstractmethod
    def access_course(self):
        pass

class Instructor(User):
    def __init__(self, name, module, courses):
        super().__init__(name, None, module, courses)
    
    def access_course(self):
        return "Full course acess"
        

class Learner(User):
    def __init__(self, name, standard, module, course):
        super().__init__(name, standard, module, course)
    
    def access_course(self):
        return f"Acess Course: {self.course}"
    

s1 = Learner("Mushil NR",12,3,"python")
print(s1.access_course())
t1 = Instructor("Resham mam",3,"python")
print(t1.access_course())
