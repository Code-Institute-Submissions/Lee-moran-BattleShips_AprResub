from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 12 for x in range(12)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 12 for i in range(12)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11  
}

def board():
    pass

def create_ships():
    pass

def get_ship_location():
    pass

def count_hit_ships():
    pass

create_ships()
turns = 10 
while turns > 0: