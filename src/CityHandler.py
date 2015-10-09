'''
Created on Oct 6, 2015

@author: Jared
'''
from StoreHandler import StoreHandler
class CityHandler(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        self.store_handler = StoreHandler()
    
    def read_input(self, my_game, player_input):
        # show available commands
        if player_input.lower() == "help":
            self.display_help() 
            return True
        elif player_input.lower() == "shop": 
            self.store_handler.show_items_for_sale(my_game)
            return True        
        # quit the game    
        elif player_input.lower() == "quit":
            my_game.quit()
            return True   
        # display the map    
        elif player_input.lower() == "map":
            my_game.map.display(my_game.my_adventurer.location)
            return True
        elif player_input.lower() == "items":
            my_game.my_adventurer.display_items()
            return True
        # leave the city    
        elif player_input.lower() == "leave":
            return False
        else:
            print ('Invalid Input')
            return True
          
    def display_help(self):
        print 'The following commands are available while in the city:' 
        print 'leave: leave city'  
        print 'map:   View the map.'
        print 'quit:  Quit the game.' 
        print 'shop:  Purchase items'