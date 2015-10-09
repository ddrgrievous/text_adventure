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
        for i in range(0,randint(1,4)):
            key = random.choice(my_game.game_items.keys())
            self.store_items.append(my_game.game_items[key])
            
        
    def show_items_for_sale(self, my_game):
        if self.need_to_setup == True:
            self.setup_shop(my_game)
            self.need_to_setup = False
        player_input = ''
        while player_input.lower() != 'leave':
            for i in range(0, len(self.store_items)):
                print str(i + 1) +'. ' + self.store_items[i].name.title() + ' ' + str(self.store_items[i].value)+ ' Gold'
            player_input = str(raw_input("Enter the item number you would like to buy!: "))
            self.handle_input(player_input,my_game)
                
    def handle_input(self,player_input, my_game):   
        for i in range(0, len(self.store_items)):
            if player_input == str(i + 1):
                my_game.my_adventurer.items.append(self.store_items[i])
                self.store_items.pop(i)
        
        if player_input == 'help':
            print 'noob'         
            
        if player_input == 'items':
            my_game.my_adventurer.display_items()                