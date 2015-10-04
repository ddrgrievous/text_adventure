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
            self.display_help()           
        # quit the game    
        elif player_input.lower() == "quit":
            my_game.quit()   
        # display the map    
        elif player_input.lower() == "map":
            my_game.map.display(my_game.my_adventurer.location)
        # move adventurer down     
        elif player_input.lower() == "down":
            # check to see if the move is going to put adventurer off the map
            if my_game.my_adventurer.location.y + 1 < len(my_game.map.spaces):
                # update the map and the adventurer's location
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_down(my_game.map)
                # display the map for the user
                my_game.map.display(my_game.my_adventurer.location)
            else:
                print "Invalid Move"
        # move adventurer up        
        elif player_input.lower() == "up":
            # check to see if the move is going to put adventurer off the map            
            if my_game.my_adventurer.location.y - 1 >= 0:           
                # update the map and the adventurer's location
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_up(my_game.map)
                # display the map for the user                
                my_game.map.display(my_game.my_adventurer.location)
            else:
                print "Invalid Move"
        # move adventurer right        
        elif player_input.lower() == "right":
            # check to see if the move is going to put adventurer off the map            
            if my_game.my_adventurer.location.x + 1 < len(my_game.map.spaces[my_game.my_adventurer.location.y]):
                # update the map and the adventurer's location                
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_right(my_game.map)
                # display the map for the user
                my_game.map.display(my_game.my_adventurer.location)
            else:
                print "Invalid Move"
        # move adventurer left        
        elif player_input.lower() == "left":
            # check to see if the move is going to put adventurer off the map            
            if my_game.my_adventurer.location.x - 1 >= 0:
                # update the map and the adventurer's location                   
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_left(my_game.map)
                # display the map for the user                
                my_game.map.display(my_game.my_adventurer.location)
            else:
                print "Invalid Move"
        else:
            print 'Invalid command'   
        
    def display_help(self):
        print 'The following commands are available while traveling:'
        print 'up: Move adventurer up.'    
        print 'right: Move adventurer right.'
        print 'down: Move adventurer down.'
        print 'left: Move adventurer left.'  
        print 'map: View the map.'
        print 'quit: Quit the game.'       