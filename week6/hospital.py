from abc import ABC, abstractmethod
class HospitalMember(ABC):
    def __init__(self,name,age,occupation):
        self._name = name
        self._age = age
        self._occupation = occupation
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def occupation(self):
        return self._occupation
    
    @abstractmethod
    def show_details():
        pass

class Doctor(HospitalMember):
    def __init__(self, name, age,no_patients,good,bad):
        if age < 18:
            raise ValueError("Doctor Should be 18+")
        if good < 1 or bad < 1 or good + bad != no_patients:
            raise ValueError("feedback should be positive and is eaqual to no_patients")
        super().__init__(name, age, "Doctor")
        self.patients = no_patients
        self.good_feedback = good
        self.bad_feedback = bad
    
    def show_details(self):
        print("-----Doctor Details-----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")
        print(f"No patientes: {self.patients}")
        print(f"Medical Recod: Good: {self.good_feedback},Bad: {self.bad_feedback}\n")
    

class Patient(HospitalMember):
    def __init__(self, name, age,medicalRecord):
        self.medicalReport = medicalRecord
        super().__init__(name, age, "patient")
    
    def show_details(self):
        print("------Patient Record------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Occupation : {self.occupation}")
        print(f"Medical Record: {self.medicalReport}\n")
        
       
d1 = Doctor("Muhsil NR",age= 19,no_patients=40,good= 35,bad=5)
d1.show_details()

record = "Left leg pain and diabetics"
p1 = Patient(name= "Muhsil NR",age= 34,medicalRecord=record)
p1.show_details()