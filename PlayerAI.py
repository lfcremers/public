import numpy as np
import random
import time
import sys
import os 
from BaseAI import BaseAI
from Grid import Grid

# TO BE IMPLEMENTED
# 
class Node():

    def __init__(self,util,grid,parent=None):

        self.util=util
        self.grid=grid
        self.children=[]
        self.parent=parent
        self.depth=0
        if parent==None:
            self.depth=1
        else:
            self.depth=parent.depth+1


class PlayerAI(BaseAI):

    def __init__(self) -> None:
        # You may choose to add attributes to your player - up to you!
        super().__init__()
        self.pos = None
        self.player_num = None
        
        
    
    def getPosition(self):
        return self.pos

    def setPosition(self, new_position):
        self.pos = new_position 
        self.root=self.pos
        #should initiate the tree here?

    def getPlayerNum(self):
        return self.player_num

    def setPlayerNum(self, num):
        self.player_num = num

    def ish(self,current_options, grid):
        best_option=None
        num_options=0
        for option in current_options:
            if len(grid.get_neighbors(option,only_available=True))>num_options:
                best_option=option
                num_options=len(grid.get_neighbors(option,only_available=True))

        return best_option

    def getMove(self, grid: Grid) -> tuple:
        """ 
        YOUR CODE GOES HERE

        The function should return a tuple of (x,y) coordinates to which the player moves.

        It should be the result of the ExpectiMinimax algorithm, maximizing over the Opponent's *Trap* actions, 
        taking into account the probabilities of them landing in the positions you believe they'd throw to.

        Note that you are not required to account for the probabilities of it landing in a different cell.

        You may adjust the input variables as you wish (though it is not necessary). Output has to be (x,y) coordinates.
        
        """
        #implement improved score heuristic: ish
        current_options=grid.get_neighbors(self.pos, only_available = True)
        adv_options=grid.get_neighbors(grid.find(2), only_available=True)
            
        best_option=self.ish(current_options,grid)
        return best_option

    def getTrap(self, grid : Grid) -> tuple:
        """ 
        YOUR CODE GOES HERE

        The function should return a tuple of (x,y) coordinates to which the player *WANTS* to throw the trap.
        
        It should be the result of the ExpectiMinimax algorithm, maximizing over the Opponent's *Move* actions, 
        taking into account the probabilities of it landing in the positions you want. 
        
        Note that you are not required to account for the probabilities of it landing in a different cell.

        You may adjust the input variables as you wish (though it is not necessary). Output has to be (x,y) coordinates.
        
        """
        #simplest return

        #return coordinates next to opponent
        return grid.get_neighbors(grid.find(2),only_available=True)[0]
        

    