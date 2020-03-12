# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
    
    def move(self, cmd):
        location = eval(f'self.location.{cmd}_to')
        if location:
            self.location = location
        else:
            print("You can't go there. Try another direction/command.")

    def look(self, cmd):
        location_items = '\n'.join([item.name for item in self.location.items])
        if len(location_items)==0:
            print('there are no items in this area.')
        else:
            print(f'you see these items: \n{location_items}')

    def get_item(self, cmd):
        #### TO DO: 
        ## SEE BOTTOM OF ADV FILE
        # sep of concerns: move this to items..
        requested_item = next(i for i in self.location.items if i.name in cmd)
        self.items.append(requested_item)
        self.location.items.remove(requested_item)
        print(f'you added 1 {requested_item.name} to your inventory!')
    
    def drop_item(self, cmd):
        dropped_item = next(i for i in self.items if i.name in cmd)
        self.items.remove(dropped_item)
        self.location.items.append(dropped_item)
        print(f'you dropped 1 {dropped_item.name}!')

    def __str__(self):
        # '''Prints all the class attribute names and values.'''
        # d = self.__dict__ 
        # player_info = '\n'.join([f'{key} = {d.get(key)}' for key in d])
        # if player_info:
            # return f"Here are {self.name}'s stats.\n" + player_info 
        # else:
            # return f"No stats for {self.name}."
        return 'Here are your items:\n' + '\n'.join([item.name for item in self.items])
    
    # def __str__(self):
    #     d = self.__dict__
    #     return '\n'.join([f'{key} = {d.get(key)}' for key in d if type(d.get(key))==str])


        
    # def eat(self, food_itme):
        