from abc import ABC, abstractmethod
class RestaurantService(ABC):
    def __init__(self,food,qty,table):
        self._food = food
        self._qty = qty
        self._table = table
    
    @property
    def food(self):
        return self._food
    @property
    def qty(self):
        return self._qty
    @property
    def table(self):
        return self._table
    
    @abstractmethod
    def prepare_food(self):
        pass
    
class VegRestaurant(RestaurantService):
    def __init__(self,food,qty,table):
        super().__init__(food,qty,table)
    
    def prepare_food(self):
        return f"Preparing Veg food {self.food}"
    
class NonVegRestaurant(RestaurantService):
    def __init__(self,food,qty,table):
        super().__init__(food,qty,table)
    
    def prepare_food(self):
        return f"Preparing Non Veg food {self.food}"
    
    
c1 = VegRestaurant("Paneer Tikka",2,4)
print(f"{c1.prepare_food()}")
c2 = NonVegRestaurant("Chicken Biriyani",2,6)
print(f"{c2.prepare_food()}")