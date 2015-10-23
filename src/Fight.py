'''
Created on Oct 8, 2015

@author: Ethan
'''
from random import randint


class Fight(object):
    #This is where the fighting logic will take place I guess haha I have no idea how this is gonna work 
    #I guess it'll be kinda turn based or something asking what you wanna do at first'
    #then the monster will attack, and stuff... we'll see what I do'
    def __init__(self):
        pass
    def dialog(self,monster):
        #I think that we should check that the player still has HP before we call this function, not as a while loop here... 
        # also I don't want to add more indents here, so there's that too.
        
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
    def fight_calcuation(self,hero,monster):
        #here's where everyone will attack I think... we'll see soon enough
        #we're gonna want to pass stuff like the monster, and the hero, and probably hero input too....
        #This first part will be simple, and will ignore atributes
        #the dialog function above returns a different number based on what you choose to do
        survived = True
        print "you are minding your own business when you stumble across a " + str(monster.level) + monster.name
        print "you have " + str(hero.current_hp) + "/" + str(hero.stats["health"]) + " Health," + str(hero.stats["attack"]) + " Attack, " + str(hero.stats["magic"]) + " Magic, " + str(hero.stats["luck"]) + " Luck!"
        print "The monster has " + str(monster.currenthp) + " Health, and " + str(monster.stats["attack"]) + " attack"
        while monster.currenthp > 0 and survived == True :
            player_input = self.dialog(monster)
            
            if player_input == 1:
                #physical attack
                y_attack =   (randint(hero.stats["attack"],hero.stats["attack"]+3) - monster.armor)
            
                print "you strike at the " + monster.name + " dealing " + str(y_attack) + " damage"
                monster.currenthp -=y_attack
            
                pass
            elif player_input == 2:
                #magical attack
                y_magic =(randint(hero.stats["magic"],hero.stats["magic"]+3))
                print "You fire a bolt of magic at the " + monster.name + " dealing " + str(y_magic) + " damage!"
                monster.currenthp -= y_magic
                
            elif player_input == 3:
                #magical Heal
                y_heal = hero.current_hp + randint(hero.stats["magic"],hero.stats["magic"]+2)
                print "healing light surrounds you, healing you for " + str(y_heal)
                hero.current_hp += y_heal
                if hero.current_hp > hero.stats["health"] :
                    hero.current_hp = hero.stats["health"]
                print " your HP is now" + str(hero.current_hp)
                pass
            elif player_input == 4:
                #run away coward
                print "You run away from the " + monster.name + "! What a coward"
                return True
            else:
                #they should never see this
                print "You broke it... shame on you"
            if monster.currenthp <= 0 :
                print " you killed the " + monster.name
                # this is kinda ghetto, but It makes XP scale of HP, and gold scale off luck
                a  =hero.experience + monster.level + (hero.stats["health"]/2)
                b =hero.gold + monster.level*2 + (hero.stats["luck"])
                hero.experience += a
                hero.gold += b
                print " you gained " + str(monster.level ) + " Experience"
                print " You found " + str(monster.level*2) + " Gold"
                if hero.experience >= hero.level * 10 :
                    hero.level_up()
                return True
            else :
                print "the "+monster.name+" is angry, it strikes at you!"
                x = randint(monster.stats["attack"]-1,monster.stats["attack"]+1)-hero.armor
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
                    
    