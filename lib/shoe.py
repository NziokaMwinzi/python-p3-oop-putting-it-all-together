class Shoe:
    def __init__(self, brand, size):
        self.brand = brand  
        self.size = size   
        self._condition = "Used"  
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and 1 <= len(brand) <= 50:  
            self._brand = brand
        else:
            print("brand must be a string")
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    @property
    def condition(self):
        return self._condition
    
    def cobble(self): 
        self._condition = "New"  
        print("Your shoe is as good as new!")  

