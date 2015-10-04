'''
Created on Oct 1, 2015
# jared is white
@author: Jared, Ethan
'''   
from Game import Game 

if __name__ == '__main__':       
    my_game = Game() 
    my_game.start()
    while my_game.in_play == True:
        my_game.travel()

