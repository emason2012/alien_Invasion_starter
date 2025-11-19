"""
Volatile game stats
Ethan Mason
11/18
This will store all of the data for the game and all stats it tracks
"""
class GameStats():

    def __init__(self, ship_limit):
        self.ships_left = ship_limit
