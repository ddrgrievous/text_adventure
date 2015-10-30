'''
Created on Oct 8, 2015

@author: Ethan
'''

from random import randint
class Monster(object):
    name = ""
    monster_names = ["Orc","Goblin","Troll","Jared","Bandit","Zombie","Gangster rapper","Toxic goo blob","Samwise the brave","Giant hornet","Giant spider","Kobold","direwolf","ghost","mutated rabbit","siren","dark mage","chimera"]
    monster_effects = ["none","armored","magic resistant","agile","regeneration","godlike armor","magic immune"]
    # --------------------------monster_effects_explained----------------------------------------------------------
    #$$$ armored = bonus armor based on level    $$$   magic resistant = magic armor based on level (unimplimented)
    #$$$ agile = dodge chance                    $$$   regeneration = regenerates hp after every hit
    #$$$ godlike armor = tons of +armor like +50 $$$   magic immune = tons of magic armor ( like +50)
    #
    # At least part of this should probably be Boss exclusive (IE normal monsters can have the first 3-4 bosses get the last 3)
    #
    level = 1
    stats = {'attack' : 0, 'health' :0}
    true_hp = 0
    true_attack = 0
    currenthp = 1
    armor = 0
    
    def __init__(self,adv_level):
        # Here the monsters' stats are declared
        # true_hp and true_attack are modifiers that make the monsters scale correctly THEY ARE IMPORTANT
        self.level = randint(adv_level,adv_level+2)
        self.name = self.monster_names[randint(0,len(self.monster_names)-1)]
        self.stats["health"] = randint(self.level+2,self.level*3)
        #This makes the monster scale harder for balance
        self.true_hp = self.stats["health"] * 12
        self.stats["attack"] = randint(self.level-(self.level/2)+1,self.level+2)
        #As does this... These variables will be replacing the old HP and Attack vars...
        self.true_attack = self.stats["attack"] * 4
        self.currenthp = self.true_hp
        