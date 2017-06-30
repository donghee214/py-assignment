"""Assignment 1 - TreasureHunt 

This module contains the TreasureHunt class.

Your only task here is to implement the methods
where indicated, according to their docstring. 
Also complete the missing doctests.
"""
from grid import Grid

class TreasureHunt:
    """
    Represents an instance of the treasure hunt game.
    
    === Attributes: ===
    @type grid_path: str 
        pathname to a text file that contains the grid map
        see Grid and Node classes for the format
	@type grid: Grid
	    a representation of the game world
    @type sonars: int
       the number of sonars the boat can drop
    @type so_range: int
       the range of sonars
    @type state: str
       the state of the game:
          STARTED, OVER, WON 
    """

    def __init__(self, grid_path, sonars, so_range):
        """
        Initialize a new game with map data stored in the file grid_path
        and commands to be used to play the game in game_path file.
        
        @type grid_path: str
           pathname to a text file that contains the grid map
           see Grid and Node classes for the format
        @type sonars: int
        @type so_range: int      
        """
        # TODO
        pass

    def process_command(self, command):
        """
        Process a command, set and return the state of the game 
        after processing this command
        @type command: str
           a command that can be used to play, as follows:
           GO direction, where direction=N,S,E,W,NW,NE,SW,SE
           SONAR, drops a sonar
           PLOT, plots the shortest path from the boat to the treasure
           (on condition the SONAR has discovered the treasure and
           the optimal oath has already been determined)
           QUIT, quit the game
        @rtype: str 
           the state of the game  
        """
        # TODO
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='pylintrc.txt')
