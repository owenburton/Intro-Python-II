'''Add items to the game that the user can carry around'''
from room import Room

### rename this file to just 'item.py'

class Item(): 
    def __init__(self, name, description):
        self.name = name 
        self.description = description
        self.with_player = False
        self.edible = False


# class Food(Item):
#     def __init__(self, name, description, calories):
#         super().__init__() 
#         self.calories = calories
#         self.edible = True
