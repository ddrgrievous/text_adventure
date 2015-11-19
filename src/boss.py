from random import randint
from Monster import Monster

        # Bosses will have special effects like regeneration that will make them stronger to kill, I just have to figure 
        # out how to call those atributes in fight so that they apply effects... I think I can do it pretty easily, by 
        #calling an effect function or something
        
        
class boss(object):
    name = ""
    effect = ""
    isboss = True
    boss_names = ["Dragon","Demon","Golem","Demigod","Wyvern"]
    #boss_names = ["Orc","Goblin","Troll","Jared","Bandit","Zombie","Gangster rapper","Toxic goo blob","Samwise the brave","Giant hornet","Giant spider","Kobold","Direwolf","Ghost","Mutated rabbit","Siren","Dark mage","Chimera"]
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
        self.name = self.boss_names[randint(0,len(self.boss_names)-1)]
        self.effect = self.monster_effects[randint(0,2)]
        self.effects()
        self.stats["health"] = randint(self.level+2,self.level*3)
        #This makes the monster scale harder for balance
        self.true_hp = self.stats["health"] * 100
        self.stats["attack"] = randint(self.level-(self.level/2)+1,self.level+2)
        #As does this... These variables will be replacing the old HP and Attack vars...
        self.true_attack = self.stats["attack"] * 2
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
        
    