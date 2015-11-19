'''
Created on Oct 8, 2015

@author: Ethan
'''
from random import randint


class Fight(object):
    dmgtype = ""
    #This isn't being used currently ... awkward.... maybe when monsters get more than one attack type
    def __init__(self):
        pass
    def dialog(self,monster,hero):
        #dialog returns a number based on players input, which is used by the fight calculator down below
        valid_input = False
        
        while valid_input == False :
            
            print  str(hero.current_hp) + "/" + str(hero.true_hp) + " HP," +str(hero.current_mana)+"/"+ str(hero.true_mana) + " Mana, "
            print monster.name+" " + str(monster.currenthp) + " Hp, " + str(monster.true_attack) + " atk"
            player_input = raw_input("Enter a number to indicate which action you will perform? : ")
            if player_input == str(1) or player_input == str(3):
                valid_input = True
                return int(player_input)
            elif player_input == str(2) :
                if hero.current_mana >= 5 :
                    hero.current_mana -= 5
                    valid_input = True
                    return int(player_input)
                else :
                    print "You don't have enough mana!"
                    valid_input = False
            else :
                print " Invalid option, your options are :"
                print "(1) Normal attack"
                print "(2) Magic attack (costs 5 mana)"
                print "(3) Run away"
                print "********************************************"
        
        
    def fight_calcuation(self,hero,monster):
        
        
        # I think that I'm going to rewrite the damage section of this when I get home, so that 
        survived = True
        # Here I've added some more interesting elements to the story telling
        
        events = ["you are minding your own business when you stumble across a level ","As you travel, you notice a level ", "Suddenly you are ambushed by a level ","You feel a little foolish when you walk right into a level ","You are thinking about awesome stuff, and walk right into a level ","Your journeying is sudden interrupted by a level "]
        current_event = events[randint(0,len(events)-1)]
        print current_event + str(monster.level) +" "+ monster.name
        
        
        
        print "you have " + str(hero.current_hp) + "/" + str(hero.true_hp) + " Health," + str(hero.true_attack) + " Attack, " +str(hero.current_mana)+"/"+ str(hero.true_mana) + " Mana, " + str(hero.stats["luck"]) + " Luck!"
        print "The "+monster.name+" has " + str(monster.currenthp) + " Health, and " + str(monster.true_attack) + " attack"
        print "(1) Normal attack"
        print "(2) Magic attack (costs 5 mana)"
        print "(3) Run away"
        print "********************************************"
        while monster.currenthp > 0 and survived == True :
            player_input = self.dialog(monster,hero)
            
            if player_input == 3:
                #run away coward
                print "You run away from the " + monster.name + "! You coward"
                return True
            else :
                #magical attack
                hero.attacking = True
                dmg = self.damage_calc(player_input, hero, monster)
                monster.currenthp -= dmg
           
            if monster.currenthp <= 0 :
                print " you killed the " + monster.name
                print "********************************************"
                self.looting(hero,monster)
                return True
            else :
                print "the "+monster.name+" is angry, it strikes at you!"
                x = randint(monster.true_attack-1,monster.true_attack+1)-hero.armor
                if (hero.stats["luck"] - randint(monster.level,monster.level + 10)) > 0 :
                    print " You quickly dodge out of the way"
                else :
                    print "he deals " + str(x)+ " damage to you"
                    hero.current_hp -= x 
                if hero.current_hp <= 0:
                    print "You died!"
                    return False
                    
                elif hero.current_hp <= 5:
                    print "you barley survived"
                    
                else :
                    print "You survived"
    def damage_calc (self,p_input,hero,monster):
        # This would be better if it could be called by monster too, but I aint that good lol
        if hero.attacking == True:
            if p_input == 1 :
                #here's physical damage
                
                y_atk =   (randint(hero.true_attack-1,hero.true_attack+2) - monster.armor)
                if y_atk < 0 :
                    y_atk = 0
                print "you strike at the " + monster.name + " dealing " + str(y_atk) + " damage"
                return y_atk
            elif p_input == 2:
                #here's magic
                
                y_mgk =(randint(hero.true_magic-1,hero.true_magic+2)-monster.mresist)
                if y_mgk < 0 :
                    y_mgk = 0;
                print "You fire a bolt of magic at the " + monster.name + " dealing " + str(y_mgk) + " damage!"
                return y_mgk
           
            hero.attacking = False
        else:
            #This is where the monster attack can be calculated
            pass
        
        pass
    def looting (self,hero,monster):
        #Here the XP and loot are determined, it also checks if you leveled up
        a  = randint(monster.level/2,monster.level * 2)
        b = randint((monster.level + hero.stats["luck"]/2) + 1,(monster.level + hero.stats["luck"] * 2))
        hero.experience += a
        hero.gold += b
        print " you gained " + str(a) + " Experience"
        print " You found " + str(b) + " Gold"
        if hero.experience >= hero.level * 15 :
            hero.level_up()
        
        