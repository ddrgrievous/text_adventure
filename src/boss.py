from random import randint
from Monster import Monster

class boss (Monster):
    
    boss_names = ["Dragon","Demon","Golem","Demigod","Wyvern"]
    def __init__(self,level):
    # lel this boss is stupid strong
        self.true_hp = level * 1000
        self.true_attack = self.stats["attack"] * 2
        self.name = self.boss_names[randint(0,len(self.boss_names)-1)]
        
        # Bosses will have special effects like regeneration that will make them stronger to kill, I just have to figure 
        # out how to call those atributes in fight so that they apply effects... I think I can do it pretty easily, by 
        #calling an effect function or something
        
        

    