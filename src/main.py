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
        player_input = raw_input("Make a choice: ")
        
        if player_input == "help":
            my_game.display_help()
            
        # quit the game    
        if player_input == "quit":
            my_game.quit()   
            
                # quit the game    
        if player_input == "map":
            my_game.map.display(my_game.my_adventurer.location)  
        
        if player_input == "down":
            my_game.my_adventurer.location.move_down()
            my_game.map.display(my_game.my_adventurer.location)    
        
