'''
Created on Oct 2, 2015

@author: Jared
'''

class TravelHandler(object):

    def __init__(self):
        pass
    
    def read_input(self, my_game, player_input):                
        # show available commands
        if player_input.lower() == "help":
            my_game.display_help()           
        # quit the game    
        elif player_input.lower() == "quit":
            my_game.quit()   
        # display the map    
        elif player_input.lower() == "map":
            my_game.map.display(my_game.my_adventurer.location)
        # move adventurer down     
        elif player_input.lower() == "down":
            my_game.my_adventurer.location.move_down(my_game.map)
            my_game.map.display(my_game.my_adventurer.location)
        elif player_input.lower() == "up":
            my_game.my_adventurer.location.move_up(my_game.map)
            my_game.map.display(my_game.my_adventurer.location)
        elif player_input.lower() == "right":
            my_game.my_adventurer.location.move_right(my_game.map)
            my_game.map.display(my_game.my_adventurer.location)
        elif player_input.lower() == "left":
            my_game.my_adventurer.location.move_left(my_game.map)
            my_game.map.display(my_game.my_adventurer.location)                