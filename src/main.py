'''
Created on Oct 1, 2015
# jared is white
@author: Jared, Ethan
'''   
from Game import Game 
import time
if __name__ == '__main__':       
    my_game = Game() 
    my_game.start()
    while my_game.in_play == True:
        my_game.travel()
        if my_game.map.current_space.lower() == 'c':
            my_game.city()
        
        if my_game.map.current_space.lower() == 'd':
            my_game.dungeon()
            
        if my_game.map.current_space.lower() =='m':
            my_game.fight()
            my_game.map.monsterdeath()
            
        if my_game.map.current_space.lower() == 'x':
            my_game.exit_dungeon()
        
        if my_game.map.current_space.lower() == 't':
            my_game.found_treasure()