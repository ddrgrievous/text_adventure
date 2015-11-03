'''
Created on Oct 1, 2015

@author: Jared, Ethan
'''
from Weapon import Weapon
from Adventurer import Adventurer
from Map  import Map
from TravelHandler import TravelHandler
from CityHandler import CityHandler
import Potion.Potion
from Fight import Fight
from Monster import Monster
class Game(object):
    
    game_items = {'health potion' : Potion(5,'health potion', 20), "Mana potion" : Potion(5,"Manapotion",20)}
    game_weapons = {'dull sword' : Weapon(10, 'dull sword', 200)}
    map = Map(10,20)
    my_adventurer = Adventurer(map)
    in_play = False
    travel_handler = TravelHandler()
    
    def __init__(self):
        pass
        
    def start(self):
        self.in_play = True
        print "Welcome to text_adventure!"
        print 'To start a new game enter  "start"'
        print 'Or to a game enter "load" [character name]'
        valid_input = False
        
        # Keep looping through responses until they choose a correct response
        while valid_input == False:
            player_input = raw_input("Start or Load?: ")
            if player_input.lower() == "start":
                self.my_adventurer.create()
                valid_input = True
                
        print "Good Luck " + self.my_adventurer.name + "!"
        
        
    def quit(self):
        self.in_play = False
        print "Come back soon!"
        
    def travel(self):
        traveling = True
        # while they are still on a empty space keep traveling
        while traveling == True:
            player_input = raw_input("Which direction will you travel?: ")
            traveling = self.travel_handler.read_input(self, player_input)
            
    def city(self):
        city_handler = CityHandler()
        in_city = True
        while in_city:
            player_input = raw_input("What is your business in the city?: ")
            in_city = city_handler.read_input(self, player_input)
    
    def dungeon(self):
        player_input = raw_input("You See an ominous cave, will you enter it?: ")#placeholder
        
    def fight (self):
        fight_handler = Fight()
        a = True
        #This is the natural regeneration... it only happens when you go into combat, so you can't abuse it by walking between already/cleared areas
        self.my_adventurer.regenerate()
        monster = Monster(self.my_adventurer.level)
        if self.my_adventurer.current_hp > 0 :
            
            a =  fight_handler.fight_calcuation(self.my_adventurer, monster)
            if a ==False :
                quit() 
        else :
            print "You shouldn't see this ever..."
            
        
        
        