'''
Created on Oct 8, 2015

@author: Ethan
'''

from random import randint
class Monster(object):
    name = ""
    monster_names = ["Orc","Goblin","Troll","Jared","God","Zombie","Gangster rapper","Toxic goo blob","Samwise the brave","Giant hornet","Giant spider","Kobold","direwolf","ghost","mutated rabbit"]
    monster_effects = ["none","armored","magic resistant","dodge","reflective(?)","poison","self obsessed","regeneration","godlike armor","magic immune"]
    level = 1
    stats = {'attack' : 0, 'health' :0}
    currenthp = 1
    armor = 0
    
    def __init__(self,adv_level):
        #monster names, and stats, these are pretty simple and straightforward
        # also the level has to scale, probably based on the players level, within 2-3 levels of the player... that shouldn't be too hard.
        self.level = randint(adv_level,adv_level+2)
        self.name = self.monster_names[randint(0,len(self.monster_names)-1)]
        self.stats["health"] = randint(self.level-(self.level)+3,self.level+(self.level*3)-1)
        self.stats["attack"] = randint(self.level-(self.level/2)+1,self.level+(self.level*2)-1)
        self.currenthp = self.stats["health"]
        