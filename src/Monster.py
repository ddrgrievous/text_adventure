'''
Created on Oct 8, 2015

@author: Ethan
'''
from random import randint
class Monster(object):
    name = ""
    monster_names = ["Orc","Goblin","Troll","Jared"]
    monster_effects = ["none","armored","magic resistant","dodge","reflective(?)","poison","self obsessed","regeneration","godlike armor","magic immune"]
    level = 1
    stats = {'attack' : 0, 'health' :0}
    def __init__(self):
        pass
    def create(self,level,monster_names,monster_effects):
        self.name = monster_names[randint(0,4)]
        self.stats["health"] = randint(level-(level/2)+1,level+(level*2)-1)
        self.stats["attack"] = randint(level-(level/2)+1,level+(level*2)-1)
        if self.level < 5:
            self.monster_effects = monster_effects[0]
        elif self.level >= 5 :
            self.monster_effects = monster_effects[randint(0,3)]
        elif self.level >=10 :
            self.monster_effects = monster_effects[randint(0,6)]
        elif self.level >= 20:
            self.monster_effects = monster_effects[randint(0,9)]
    def armored(self):
        pass
    def magic_resistant(self):
        pass
    def dodge(self):
        pass
    def reflective(self):
        pass
    def poison(self):
        pass
    def self_obssessed(self):
        pass    
    def regeneration(self):
        pass
    def godlike_armor(self):
        pass
    def magic_immune(self):
        pass