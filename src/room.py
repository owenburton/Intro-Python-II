# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items=[]):
        self.name = name 
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        print(self.name)
        print('')
        print(self.description)
    
    def get_exits_string(self):
        directions = ('n','s','e','w')
        exits = [d for d in directions if eval(f'self.{d}_to')]
        print(exits)