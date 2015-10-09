'''
Created on Oct 8, 2015

@author: Ethan
'''
from random import randint
class Monster(object):
    name = ""
    monster_names = ["Orc","Goblin","Troll","Jared","Zombie","Gangster rapper","Giant spider","Kobold","direwolf","ghost","mutated rabbit"]
    monster_effects = ["none","armored","magic resistant","dodge","reflective(?)","poison","self obsessed","regeneration","godlike armor","magic immune"]
    level = 1
    stats = {'attack' : 0, 'health' :0}
    currenthp = 1
    armor = 0
    def __init__(self):
        pass
    def create(self,level,monster_names,monster_effects):
        #monster names, and stats, these are pretty simple and straightforward
        # also the level has to scale, probably based on the players level, within 2-3 levels of the player... that shouldn't be too hard.
        self.name = monster_names[randint(0,monster_names.range())]
        self.stats["health"] = randint(level-(level)+3,level+(level*3)-1)
        self.stats["attack"] = randint(level-(level/2)+1,level+(level*2)-1)
        self.currenthp = self.stats["health"]
        if self.level < 5:
            #This helps the monsters scale better into the lategame, as you get stronger, so do they
            self.monster_effects = monster_effects[0]
        elif self.level >= 5 :
            self.armor = self.armor + 1
            self.monster_effects = monster_effects[randint(0,3)]
        elif self.level >=10 :
            self.armor = self.armor + 3
            self.monster_effects = monster_effects[randint(0,6)]
        elif self.level >= 20:
            self.armor = self.armor + 5
            #also it would be interesting to add multiple effects to some monsters... maybe we can save that for the bosses
            self.monster_effects = monster_effects[randint(0,9)]
        else :
            # add another level of scaling here? even write a program that continuously scales up the monsters... I doubt we'd even need up to 20 for 
            #the size of map that we have... maybe you can go to more than one?
            pass
    #here I've put the effects, although it was suggested that they be moved to a separate class, so that they can be used more globally... idk really
    def armored(self,monster):
        
        
        pass
    def magic_resistant(self,monster):
        
        pass
    def dodge(self,monster):
        
        pass
    def reflective(self,monster):
        
        pass
    def poison(self,monster):
        
        pass
    def self_obssessed(self,monster):
        
        pass    
    def regeneration(self,monster):
        
        pass
    def godlike_armor(self,monster):
        
        pass
    def magic_immune(self,monster):
        
        pass