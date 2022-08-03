import random
from collections import namedtuple
from enum import Enum

class Directions(object):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

context = Enum("Context",[
    "navigate",
    "fight"
])

class Enemy(object):
    def __init__(self, hp=100, attacks:list=None):
        self.hp = hp
        self.attacks = attacks
    
    def get_attack(self):
        return random.choice(self.attacks)

class Room(object):
    "Holds information about a room"
    def __init__(self, name, items=None, enemy=None):
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items
        self.enemy = enemy
        self.connections = {} 
    
    def add_connection(self, room: "Room", direction, reverse_direction=None):
        # connect to other room
        self.connections[direction] = room
        # connect other room to this room in oposite direction
        if reverse_direction:
            room.connections[reverse_direction] = self
    
def navigate(room:Room):
    print("*"*60)
    print(f"You are in {room.name}")
    if room.enemy:
        combat(room.enemy)
    
    if room.items:
        print("You see:")
        for item in room.items:
            print(f"  -{item.name}")

    print("You may go:")
    for direction in room.connections.keys():
        print(direction)

    return input("What would you like to do? (enter 'o' for options)").strip()
    

def play_game(starting_room:Room):
    current_room = starting_room
    while True:
        user_input = navigate(current_room)
        if user_input in current_room.connections:
            current_room = current_room.connections[user_input]
        else:
            print("Invalid entry")

def combat(enemies):
    pass

def main():
    entry = Room("Entryway")
    dungeon = Room("Dungeon")
    cellar = Room("Cellar")
    dining_room = Room("Dining Room")
    tower = Room("Tower")

    entry.add_connection(dining_room, Directions.EAST, Directions.WEST)
    dining_room.add_connection(cellar, Directions.SOUTH, Directions.NORTH)
    dining_room.add_connection(tower, Directions.EAST, Directions.WEST)
    cellar.add_connection(dungeon, Directions.SOUTH, Directions.NORTH)

    play_game(entry)

if __name__ == "__main__":
    main()
    