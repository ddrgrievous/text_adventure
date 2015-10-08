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
    def __init__(self):
        pass
    def create(self,level,monster_names,monster_effects):
        #monster names, and stats, these are pretty simple and straightforward
        # also the level has to scale, probably based on the players level, within 2-3 levels of the player... that shouldn't be too hard.
        self.name = monster_names[randint(0,monster_names.range())]
        self.stats["health"] = randint(level-(level/2)+1,level+(level*2)-1)
        self.stats["attack"] = randint(level-(level/2)+1,level+(level*2)-1)
        self.currenthp = self.stats["health"]
        if self.level < 5:
            #This helps the monsters scale better into the lategame, as you get stronger, so do they
            self.monster_effects = monster_effects[0]
        elif self.level >= 5 :
            self.monster_effects = monster_effects[randint(0,3)]
        elif self.level >=10 :
            self.monster_effects = monster_effects[randint(0,6)]
        elif self.level >= 20:
            #also it would be interesting to add multiple effects to some monsters... maybe we can save that for the bosses
            self.monster_effects = monster_effects[randint(0,9)]
    #here I've put the effects, although it was suggested that they be moved to a separate class, so that they can be used more globally... idk really
    #The value will be used to determine the scaling of XP-gold based on monster atributes, IE a value 3 will give a lot more exp than a value 0 or 1
    def armored(self):
        value = 1
        pass
    def magic_resistant(self):
        value = 1
        pass
    def dodge(self):
        value = 1
        pass
    def reflective(self):
        value = 2
        pass
    def poison(self):
        value = 2
        pass
    def self_obssessed(self):
        value = 2
        pass    
    def regeneration(self):
        value = 3
        pass
    def godlike_armor(self):
        value = 3
        pass
    def magic_immune(self):
        value = 3
        pass