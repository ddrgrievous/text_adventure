'''
Created on Oct 6, 2015

@author: Jared
'''

class CityHandler(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    def read_input(self, my_game, player_input):
         # show available commands
        if player_input.lower() == "help":
            self.display_help() 
            return True          
        # quit the game    
        elif player_input.lower() == "quit":
            my_game.quit()
            return True   
        # display the map    
        elif player_input.lower() == "map":
            my_game.map.display(my_game.my_adventurer.location)
            return True
        # leave the city    
        elif player_input.lower() == "leave":
            return False
        else:
            print ('Invalid Input')
            return True
            
    def display_help(self):
        print 'The following commands are available while in the city:'
        print 'up: Move adventurer up.'    
        print 'leave: leave city'  
        print 'map: View the map.'
        print 'quit: Quit the game.' 