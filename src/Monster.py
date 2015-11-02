'''
Created on Oct 8, 2015

@author: Ethan
'''

from random import randint
class Monster(object):
    name = ""
    effect = ""
    monster_names = ["Orc","Goblin","Troll","Jared","Bandit","Zombie","Gangster rapper","Toxic goo blob","Samwise the brave","Giant hornet","Giant spider","Kobold","Direwolf","Ghost","Mutated rabbit","Siren","Dark mage","Chimera"]
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
    mresist = 0
    #magic resistance
    
    def __init__(self,adv_level):
        # Here the monsters' stats are declared
        # true_hp and true_attack are modifiers that make the monsters scale correctly THEY ARE IMPORTANT
        self.level = randint(adv_level,adv_level+2)
        self.name = self.monster_names[randint(0,len(self.monster_names)-1)]
        self.effect = self.monster_effects[randint(0,2)]
        self.effects()
        self.stats["health"] = randint(self.level+2,self.level*3)
        #This makes the monster scale harder for balance
        self.true_hp = self.stats["health"] * 12
        self.stats["attack"] = randint(self.level-(self.level/2)+1,self.level+2)
        #As does this... These variables will be replacing the old HP and Attack vars...
        self.true_attack = self.stats["attack"] * 3
        #/\-- I'm not sure how hard monsters should scale... a single monster probably shouldn't be able to kill you, but not healing in between fights might
        self.currenthp = self.true_hp
    def effects (self):
        
        if self.effect == "none" :
            return 0
        elif self.effect == "armored":
            self.armor += 5
            return 1
        elif self.effect == "magic resistant":
            self.mresist += 5
            return 2
        
    def dmgtype (self):
        #["Orc","Goblin","Troll","Jared","Bandit","Zombie","Gangster rapper","Toxic goo blob","Samwise the brave",
        #"Giant hornet","Giant spider","Kobold","Direwolf","ghost","Mutated rabbit","siren","dark mage","Chimera"]
   
        if self.name == "Orc" or self.name == "Goblin" or self.name == "Troll" or self.name == "Bandit" or self.name == "Zombie" or self.name == "Samwise the brave" or self.name == "Giant hornet" or self.name == "Kobold" or self.name == "Direwolf" or self.name == "Mutated rabbit" or self.name == "Chimera" :
            return "1"
        #physical damage type
        elif self.name =="Toxic goo blob" or self.name == "Giant spider" or self.name == "Ghost" or self.name == "Siren" or self.name == "Dark mage":
            return "2"
        # Magical damage type
        else :
            return "0"
        #special damage type... unreducable bwahahaha or something haha I dunno
    






        