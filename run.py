"""
___BATTLESHIPS___
Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variablies, Methods
How to work:
1. a 14 x 14 grid will have 8 ships of variable lenght randomly placed
2. you will have 50 bullets to take down the ships 
3. you can choose a row and column such as A3 to indicate where to shoot
4. for every shot that hits or misses will be shown in the grid
5. a ship cannot be placed diagonally, so if a shot hits the rest of the 
   ship is in one of 4 directions, left, reight, up, down
6. If all ships are unearthed before using up all bullets, you win else,
   you lose


Legend:
1. "." = water or empty space
2. "O" = part of ship
3. "X" = part of ship which was hit
4. "#" = water shot

"""

grid = [[]]

grid_size = 14

num_of_ships = 8

bullets_left = 50

game_over = False

num_of_ships_sunk = 0

ship_positions = [[]]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """ 
    Will check the row or coloumn to see if it is safe to place a ship there
    Return T or F
    """
    global grid
    global ship_positions

    pass

def try_to_place_ship_on_grid(row, col, direction, lenght):
    """ 
    Based on direction will call helper method to try and place ship 
    on the grid.
    Returns validate_grid_and_place_ship
    """
    global grid_size

    pass

    return validate_grid_and_place_ship(0, 0, 0, 0)

def create_grid():
    """
    Will create a 14x14 grid and randomly place down ships
    of differect size in different directions.
    Has no return but will use try_to_place_ships_on_grid
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    pass

    try_to_place_ship_on_grid(0, 0, 0, 0)
