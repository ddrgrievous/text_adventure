'''
Created on Oct 2, 2015

@author: Jared
'''

# Hey i took this out because you don't seem to have to import it, and importing it causes a circular dependency...
# from main import my_game

class TravelHandler(object):

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
            return False   
        # display the map
       
        elif player_input.lower() == "map":
            my_game.map.display(my_game.my_adventurer.location)
            return True
        
        elif player_input.lower() == "stats":
            print str(my_game.my_adventurer.current_hp) + "/" +  str(my_game.my_adventurer.stats["health"]) + "Health, " + str(my_game.my_adventurer.stats["attack"]) + " Attack, " + str(my_game.my_adventurer.stats["magic"]) + " magic, " + str(my_game.my_adventurer.stats["luck"]) + " luck"    
            print "you are level " + str(my_game.my_adventurer.level) + " and you have " + str(my_game.my_adventurer.gold) + " Gold"
            return True
            
        elif player_input.lower() =="heal":
            my_game.my_adventurer.current_hp = my_game.my_adventurer.stats["health"]
            print "you heal yourself back to full health"
        
        
        # move adventurer down     
        elif player_input.lower() == "down" or player_input.lower() == "south" or player_input.lower() == "d" or player_input.lower() == "s":
            # check to see if the move is going to put adventurer off the map
            if my_game.my_adventurer.location.y + 1 < len(my_game.map.spaces):
                # update the map and the adventurer's location
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_down(my_game.map)
                # display the map for the user
                my_game.map.display(my_game.my_adventurer.location)
                return self.is_traveling(my_game)                
            else:
                print "Invalid Move"
        # move adventurer up        
        elif player_input.lower() == "up" or player_input.lower() == "north" or player_input.lower() == "u" or player_input.lower() == "n":
            # check to see if the move is going to put adventurer off the map            
            if my_game.my_adventurer.location.y - 1 >= 0:           
                # update the map and the adventurer's location
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_up(my_game.map)
                # display the map for the user                
                my_game.map.display(my_game.my_adventurer.location)
                return self.is_traveling(my_game)                
            else:
                print "Invalid Move"
        # move adventurer right        
        elif player_input.lower() == "right" or player_input.lower() == "east" or player_input.lower() == "r" or player_input.lower() == "e":
            # check to see if the move is going to put adventurer off the map            
            if my_game.my_adventurer.location.x + 1 < len(my_game.map.spaces[my_game.my_adventurer.location.y]):
                # update the map and the adventurer's location                
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_right(my_game.map)
                # display the map for the user
                my_game.map.display(my_game.my_adventurer.location)
                return self.is_traveling(my_game)                
            else:
                print "Invalid Move"
                return True
        # move adventurer left        
        elif player_input.lower() == "left" or player_input.lower() == "west" or player_input.lower() == "l" or player_input.lower() == "w":
            # check to see if the move is going to put adventurer off the map            
            if my_game.my_adventurer.location.x - 1 >= 0:
                # update the map and the adventurer's location                   
                my_game.my_adventurer.location = my_game.my_adventurer.location.move_left(my_game.map)
                # display the map for the user                
                my_game.map.display(my_game.my_adventurer.location)
                return self.is_traveling(my_game)
            else:
                print "Invalid Move"
        else:
            print 'Invalid command'
               
    def is_traveling(self, my_game):
        if my_game.map.current_space.lower() == 'c':
            return False
        elif my_game.map.current_space.lower() =='m':
            return False
        else:
            return True
            
    def display_help(self):
        print 'The following commands are available while traveling:'
        print 'up: Move adventurer up.'    
        print 'right: Move adventurer right.'
        print 'down: Move adventurer down.'
        print 'left: Move adventurer left.'  
        print 'map: View the map.'
        print "stats: Veiw your stats"
        print "heal: heal yourself back to full"
        print 'quit: Quit the game.'       