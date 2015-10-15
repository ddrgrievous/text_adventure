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
    def dialog(self):
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
                magic_input = raw_input("Do you want to use magic missile, or heal?")
                valid_input2 =False
                #another valid input loop
                while valid_input2 ==False:
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
    def fight_calcuation(self,hero,monster,player_input):
        #here's where everyone will attack I think... we'll see soon enough
        #we're gonna want to pass stuff like the monster, and the hero, and probably hero input too....
        #This first part will be simple, and will ignore atributes
        #the dialog function above returns a different number based on what you choose to do
        while monster.currenthp > 0:
            if player_input == 1:
                #physical attack
                print "you strike at the " + monster.name
                monster.currenthp = monster.currenthp - (randint(hero.stats("attack")-3,hero.stats("attack")+3) - monster.armor)
            
            
                pass
            elif player_input == 2:
                #magical attack
                print "You fire a bolt of magic at the " + monster.name
            
                monster.currenthp = monster.currenthp - (randint(hero.stats("magic")-3,hero.stats("magic")+3))
            elif player_input == 3:
                #magical Heal
                print "healing light surrounds you"
                hero.current.hp += randint(hero.stats("magic")-2,hero.stats("magic")+2)
                pass
            elif player_input == 4:
                #run away coward
                print "You run away from the " + monster.name + "! What a coward"
                pass
            else:
                #they should never see this
                print "You broke it... shame on you"
            if monster.currenthp <= 0 :
                print " you killed the monster"
                print " you gained " +monster.level + " Experience"
                print " You found " +monster.level*2 + " Gold"
                hero.experience += monster.level
                hero.gold += monster.level*2
            else :
                print "the Monster is angry, it strikes at you!"
                x = randint(monster.stats("attack")+1,monster.stats("attack")*2-2)
                # The hero's armor still needs to be taken into account
                #/\ important, deserves 2 lines
                #or 3
                print "he deals " + x+ " damage to you"
                hero.current_hp -= x 
                if hero.current_hp <= 0:
                    print "You died!"
                    pass
                elif hero.current_hp <= 5:
                    print "you barley survived"
                    pass
                else :
                    print "You survived"
                    pass
    def loot (self,hero,monster):
        #In this the loot (xp and gold) from a battle will be determined
        #Ill make this later, for now It is staticly added right after you kill the monster
        hero.experience = hero.experience + monster.level
        pass
