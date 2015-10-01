'''
Created on Oct 1, 2015
# jared is white
@author: Jared, Ethan
'''   
from Game import Game 

if __name__ == '__main__':
    game_in_play = True    
    
    #start the game
    my_game = Game()
    
    my_game.start()
    while my_game.in_play == True:
        player_input = raw_input("Make a choice: ")
        
        if player_input == "help":
            my_game.display_help()
            
        # quit the game    
        if player_input == "quit":
            my_game.quit()        
        
