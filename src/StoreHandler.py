'''
Created on Oct 8, 2015

@author: Jared
'''

import random
from Crypto.Random.random import randint

class StoreHandler(object):
    '''
    classdocs
    '''
    store_items = []
    need_to_setup = True

    def __init__(self):
        pass
            
    def setup_shop(self, my_game):
        # a store will have 1-4 items
        for i in range(0,randint(1,4)):
            
            # randomly select the items for sale
            key = random.choice(my_game.game_items.keys())
            
            # add the item to the store items
            self.store_items.append(my_game.game_items[key])
            
        
    def show_items_for_sale(self, my_game):
        
        # this occurs only if it is their first visit to the store
        if self.need_to_setup == True:
            self.setup_shop(my_game)
            self.need_to_setup = False
        
        # initialize input    
        player_input = ''
        
        # loop through the prompting until they choose to leave
        while player_input.lower() != 'leave':
            
            # loop through store items
            for i in range(0, len(self.store_items)):
                
                # print items
                print str(i + 1) +'. ' + self.store_items[i].name.title() + ' ' + str(self.store_items[i].value)+ ' Gold'
            
            # prompt
            player_input = str(raw_input("Enter the item number you would like to buy!: "))
            
            # handle the input
            self.handle_input(player_input,my_game)
                
    def handle_input(self,player_input, my_game):   
        
        # check to see if they have chosen an item
        for i in range(0, len(self.store_items)):
            
            # check for which item
            if player_input == str(i + 1):
                
                # check if they have enough gold
                if my_game.my_adventurer.gold >= self.store_items[i].value:
                    
                    # add to the adventurer's inventory
                    my_game.my_adventurer.items.append(self.store_items[i])
                    print "Item purchased"
                    my_game.my_adventurer.gold -= self.store_items[i].value
                    print "Gold remaining: " + str(my_game.my_adventurer.gold)
                    
                    # get rid of it from the store inventory
                    self.store_items.pop(i)
                else:
                    print "You don't have enough gold!"
                    
        
        if player_input == 'help':
            self.display_help()         
            
        if player_input == 'items':
            my_game.my_adventurer.display_items() 
        
        if player_input == 'map':
            my_game.map.display(my_game.my_adventurer.location)
    
    def display_help(self):
        print 'Enter an item number to purchase it' 
        print 'items: shows your adventures current items'
        print 'map: display the map'
        print 'leave: exit the shop'   
                    