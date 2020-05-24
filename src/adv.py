from room import Room
from player import Player
from items import Item 

from random import choice
from textwrap import TextWrapper as tw

# Declare items
item_dict = {
    'stone':'not very valuable, but you could throw it', 
    'coin':'looks like gold!', 
    'cobweb':'not pleasant', 
    'bone':'could make some bone broth with it..', 
    'gem':'ooo, sparkly!', 
    'book':'cannot read. better consult a wizard about the contents', 
    'sword':'pointy'}
# game_items = [Item(k,v) for k,v in item_dict.items()]
game_items = [Item(name, description) for name,description in item_dict.items()]

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [choice(game_items)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [choice(game_items) for i in range(2)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [choice(game_items) for i in range(4)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [choice(game_items) for i in range(4)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [choice(game_items) for i in range(6)]),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player = Player('Sam', room['outside'])
player = Player(input('Please enter your name: '), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# function for player commands
def player_command(cmd):
    if cmd == 'q':
        print('gg')
        exit() # why not exit(0) or exit(1)

    elif cmd in ('n','s','e','w'):
        player.move(cmd)
    
    elif cmd == 'info': #or 'items' 'what' in cmd:
        print(player)

    elif cmd == 'look':
        player.look(cmd)

    elif 'get' in cmd:
        try:
            player.get_item(cmd)
        except:
            pass

    elif 'drop' in cmd:
        try:
            player.drop_item(cmd)
        except:
            pass

    else:
        print('Try another command..')

while True:
    # print(repr(player))
    print(f' Current location: {player.location.name} '.center(100, '-'))
    # print(tw.wrap(f' Location description: {player.location.description} ', 20)) #.center(100, '-'))
    print(f' Location description: {player.location.description} '.center(100, '-'))

    cmd = input('>>> ')
    player_command(cmd)


######### TO DO:
#Add an on_take method to Item.

# Call this method when the Item is picked up by the player.

# on_take should print out "You have picked up [NAME]" when you pick up an item.

# The Item can use this to run additional code when it is picked up.

# Add an on_drop method to Item. Implement it similar to on_take.
