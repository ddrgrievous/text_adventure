'''
Created on Oct 8, 2015

@author: Ethan
'''
from random import randint


class Fight(object):
    
    def __init__(self):
        pass
    def dialog(self,monster,hero):
        valid_input = False
        
        while valid_input == False :
            
        
            player_input = raw_input("Enter a number to indicate which action you will perform")
            if player_input == str(1) or player_input == str(4):
                valid_input = True
                return int(player_input)
            elif player_input == str(2) or player_input == str(3):
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
                print "(3) Magic Heal(costs 5 mana)"
                print "(4) Run away"
                
        
        """    
        valid_input = False
        while valid_input == False:
            #/\ this loops so that you have to give good input
            player_input = raw_input("What attack would you like to perform?")
            if player_input.lower() == "attack":
                valid_input = True
                # here the damage will be dealt , as physical/normal damage
                return 1
            elif player_input.lower() =="magic":
                valid_input = True
                # this determines if you are going to be attacking with magic, or healing
                
                valid_input2 =False
                #another valid input loop
                while valid_input2 ==False:
                    magic_input = raw_input("Do you want to use magic missile, or heal?")
                    if magic_input.lower() == "missile":
                        valid_input2 = True
                        #Here the damage will be dealt, as magical damage, probably we shouldn't go more complex than that (IE FIRE DAMAGE/ ICE DAMAGE)
                        return 2
                    elif magic_input.lower() == "heal":
                        valid_input2 = True
                        #Here the hero will be healed for whatever he rolls (a random number of HP)
                        return 3
                    else :
                        print "invalid input, put (missile) or (heal)"
                        # telling the valid options when the text is invalid will be good so we don't have to write a help bit here for two options
                        valid_input2 = False
            elif player_input.lower() =="run":
                print "whimp"
                valid_input = True
                #This will end the combat early, and let you run away... no XP or gold earned for this option, you coward
                return 4
            else :
                print "Invalid input"
                print "Your options are : attack, magic, run"
                print "please choose one"
                valid_input = False
    """
    def fight_calcuation(self,hero,monster):
        #here's where everyone will attack I think... we'll see soon enough
        #we're going to want to pass stuff like the monster, and the hero, and probably hero input too....
        #This first part will be simple, and will ignore atributes
        #the dialog function above returns a different number based on what you choose to do
        
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
        print "(3) Magic Heal(costs 5 mana)"
        print "(4) Run away"
        while monster.currenthp > 0 and survived == True :
            player_input = self.dialog(monster,hero)
            
            if player_input == 1:
                #physical attack
                y_attack =   (randint(hero.true_attack-1,hero.true_attack+2) - monster.armor)
                if y_attack < 0 :
                    y_attack = 0
                print "you strike at the " + monster.name + " dealing " + str(y_attack) + " damage"
                monster.currenthp -=y_attack
            
                pass
            elif player_input == 2:
                
                #magical attack
                y_magic =(randint(hero.true_magic-1,hero.true_magic+2))
                if y_magic < 0 :
                    y_magic = 0;
                print "You fire a bolt of magic at the " + monster.name + " dealing " + str(y_magic) + " damage!"
                monster.currenthp -= y_magic
                
            elif player_input == 3:
                #magical Heal
                y_heal = hero.current_hp + randint(hero.true_magic,hero.true_magic+2)
                print "healing light surrounds you, healing you for " + str(y_heal)
                hero.current_hp += y_heal
                hero.Checkhp()
                print " your HP is now" + str(hero.current_hp)
                pass
            elif player_input == 4:
                #run away coward
                print "You run away from the " + monster.name + "! You coward"
                return True
            else:
                #they should never see this
                print "You should never see this, so here's a story... once upon a time I was writing this game and got bored, and wrote this, the end"
            if monster.currenthp <= 0 :
                print " you killed the " + monster.name
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
    def damage_calc (self,dmgtaken,dmgtype,monster):
        # I'm unfocused, so I can't write this right now
        
        
        
        pass
    def looting (self,hero,monster):
        #Here the XP and loot are determined, it also checks if you leveled up
        a  = monster.level + (hero.stats["health"]/2)
        b = monster.level*2 + (hero.stats["luck"])
        hero.experience += a
        hero.gold += b
        print " you gained " + str(a) + " Experience"
        print " You found " + str(b) + " Gold"
        if hero.experience >= hero.level * 15 :
            hero.level_up()
        
        