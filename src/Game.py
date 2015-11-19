'''
Created on Oct 1, 2015

@author: Jared, Ethan
'''
from Weapon import Weapon
from Adventurer import Adventurer
from Map  import Map
from Dungeon_map import Dungeon_map
from TravelHandler import TravelHandler
from CityHandler import CityHandler
from HealthPotion import Potion
from Fight import Fight
from Monster import Monster
from boss import boss
from Location import Location
import time
from random import randint
class Game(object):
    
    game_items = {'health potion' : Potion(5,'health potion', 20), "Mana potion" : Potion(5,"Manapotion",20)}
    game_weapons = {'dull sword' : Weapon(10, 'dull sword', 200)}
    map_storage = []
    location_storage = []
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
            elif player_input.lower() == "load" :
                filename = raw_input("What file would you like to load?")
                open (filename.lower(),"w")
                
                valid_input = True
        print "Good Luck " + self.my_adventurer.name + "!"
        
        
    def quit(self):
        self.in_play = False
        print "Come back soon!"
        time.sleep(5)
        
        
        
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
        
        if player_input.lower() == 'y' or player_input.lower() == 'yes':
            self.map_storage.append(self.map)
            self.location_storage.append(self.my_adventurer.location)
            self.map = Dungeon_map(randint(3,7),randint(3,7))
            self.my_adventurer.location = Location(0,0, self.map)
            self.map.display(self.my_adventurer.location)
            
    def exit_dungeon(self):
        player_input = raw_input("Do you want to leave this dungeon?  You can never come back: ")
        
        if player_input.lower() == 'y' or player_input.lower() == 'yes':
            self.map = self.map_storage[len(self.map_storage) - 1]
            self.my_adventurer.location = self.location_storage[len(self.location_storage) - 1]
            del self.map_storage[-1]
            del self.location_storage[-1]
            self.map.current_space = ' '
            
    def found_treasure(self):
        amount = randint(5,300) * (len(self.map_storage) + 1)
        print "********************************************"
        print "********** YOU FOUND " + str(amount) + " Gold!" + "**********"
        print "********************************************" 
        print " "
        self.map.display(self.my_adventurer.location)
        self.my_adventurer.gold += amount
        self.map.current_space = ' '
            
    def fight (self,isboss):
        fight_handler = Fight()
        a = True
        #This is the natural regeneration... it only happens when you go into combat, so you can't abuse it by walking between already/cleared areas
        self.my_adventurer.regenerate()
        
        if isboss == False :
            monster = Monster(self.my_adventurer.level)
        elif isboss == True:
            monster = boss(self.my_adventurer.level)
        
        if self.my_adventurer.current_hp > 0 :
            
            a =  fight_handler.fight_calcuation(self.my_adventurer, monster)
            if a ==False :
                quit() 
        else :
            print "You shouldn't see this ever..."
            
        
        
        