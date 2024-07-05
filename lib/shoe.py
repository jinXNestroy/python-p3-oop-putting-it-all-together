#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition ="old") -> None:
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size 
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size= size
            return self._size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "Your shoe is as good as new!"
        if self.condition == "Your shoe is as good as new!":
            self.condition = "New"
        print("Your shoe is as good as new!")


    