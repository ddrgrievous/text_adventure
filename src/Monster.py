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
    
    def __init__(self,level):
        #monster names, and stats, these are pretty simple and straightforward
        # also the level has to scale, probably based on the players level, within 2-3 levels of the player... that shouldn't be too hard.
        self.name = self.monster_names[randint(0,len(self.monster_names))]
        self.stats["health"] = randint(level-(level)+3,level+(level*3)-1)
        self.stats["attack"] = randint(level-(level/2)+1,level+(level*2)-1)
        self.currenthp = self.stats["health"]
        