from abc import ABC, abstractmethod
class GameCharecter(ABC):
    def __init__(self,name,power,health,range,level):
        self.name = name
        self.power = power
        self._health = health
        self.range = range
        self._level = level
    
    @property
    def health(self):
        return self._health
    
    @property
    def level(self):
        return self._level
    
    @abstractmethod
    def attack(self):
        pass
    

class Warrior(GameCharecter):
    def __init__(self, name, power, health, range,level):
        super().__init__(name, power, health, range,level)
    
    def attack(self):
        return "slicing Attack!"

class Mage(GameCharecter):
    def __init__(self, name, power, health, range,level):
        super().__init__(name, power, health, range,level)
    
    def attack(self):
        return "Magic Attack!"
    

class Archer(GameCharecter):
    def __init__(self, name, power, health, range,level):
        super().__init__(name, power, health, range,level)
    
    def attack(self):
        return "Arrow attack!"
 

playerLIst = [
    Warrior("Thorfinn","strong fist",120,"mid",10),
    Mage("Counte","clever",60,"close",123,),
    Archer("Okotsu","Rika",1000,"long",1000)
]

for player in playerLIst:
    print("\n----Charecter Detial----")
    print(f"\nName: {player.name}")
    print(f"Power: {player.power}")
    print(f"Health: {player.health}")
    print(f"Range: {player.range}")
    print(f"Level: {player.level}")
    print(f"(Attack){player.attack()}\n")


