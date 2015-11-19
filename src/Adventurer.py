'''
Created on Oct 1, 2015

@author: Jared, Ethan
'''
from Location import Location
from Weapon import Weapon

class Adventurer(object):
    
    name = ""
    type = ""
    experience = 0
    stats = {'attack' : 0, 'health' : 0, 'magic' : 0, 'luck' : 0}
    true_hp = 0
    true_magic = 0
    true_mana = 0
    true_attack = 0
    current_hp = 0
    current_mana = 0
    level = 1
    gold = 1000
    items = []
    weapon = Weapon(0,'wooden stick', 0)
    spells = []
    armor = 1
    attacking = False
    
   
    
    def __init__(self, map):
        self.location = Location(0,0,map)
        
    def full_heal(self):
        # lol I just wrote a fullheal somewhere else... This code is a bit better but I don't care
        self.current_hp = self.stats['health'];
    
    def create(self):
        finished_creation = False
        
        # adventures name
        self.name = raw_input("What is your Adventurer's Name?: ")
        
        while finished_creation == False:          
            # print the choices of classes
            print 'Warrior  (6 health, 6 attack, 1 magic, luck 2)'
            print 'Mage     (5 health, 1 attack, 5 magic, luck 4)'
            print 'Beserker (6 health, 9 attack, 0 magic, luck 0)'
            print 'Custom   (? health, ? attack, ? magic, luck ?)'
            self.type = raw_input("Choose a class: ")
            
            if self.type.lower() == 'beserker':
                self.stats['health'] = 6
                self.stats['attack'] = 9
                finished_creation = True        
            elif self.type.lower() == 'mage':
                self.stats['health'] = 5
                self.stats['attack'] = 1
                self.stats['magic']  = 5
                self.stats['luck']   = 4
                finished_creation = True
            elif self.type.lower() == 'warrior':
                self.stats['health'] = 6
                self.stats['attack'] = 6
                self.stats['magic']  = 1
                self.stats['luck']   = 2
                finished_creation = True 
            elif self.type.lower() == 'demon_lord':
                # This is a test class, that will for sure make it to the city to buy stuff
                # if you level up, put your points into luck, so that you can for sure see the effects of items
                self.stats['health'] = 100
                self.stats['attack'] = 100
                self.stats['magic']  = 100
                self.stats['luck']   = -100
                finished_creation = True
            elif self.type.lower() == 'Jared':
                #This is a profile that I change based on what I want to test
                self.stats['health'] = 1
                self.stats['attack'] = 1
                self.stats['magic']  = 2
                self.stats['luck']   = 1 
                finished_creation = True   
            elif self.type.lower() == "Ethan":
                self.stats['health'] = 4
                self.stats["attack"] = 5
                self.stats["magic"] = 2
                self.stats["luck"] = 10000   
            # custom type means that they are able to choose their own stats 
            elif self.type.lower() == 'custom':
                print 'You get a total of 15 points to assign between attack, health, luck, and magic.'
                total_points = 15
                choosing_character = True
                while choosing_character == True:
                    # loop through each stats
                    for key in sorted(self.stats):
                        print "You have " + str(total_points) + " left"
                        self.stats[key] = int(raw_input( key +"?: "))
                        total_points -= self.stats[key]
                        
                        # if you run out of points you are done
                        if total_points <= 0:
                            break
                    print "You have Chosen:"    
                    for key in sorted(self.stats):
                        print key + ": " + str(self.stats[key])
                    
                    if raw_input( "Is this correct? (y/n): ").lower() == 'y':
                        choosing_character = False
                        finished_creation = True
                    else:
                        # reset the stats to 0 because they will choose again
                        for key in sorted(self.stats):
                            self.stats[key] = 0
                        total_points = 15
            else:
                print "Invalid Command"
        
       
        # Here Im calling the stat modifiers, so that heros have more health and stuff
        self.realstats()
    def realstats(self):
        self.true_hp = self.stats["health"] * 12
        self.true_attack = self.stats["attack"] * 4
        self.true_magic = self.stats["magic"] * 4
        self.true_mana = self.stats["magic"] * 5
        self.current_hp = self.true_hp
        self.current_mana = self.true_mana
       
        
    
    def display_items(self):
        print "Gold: " + str(self.gold)   
        print "Weapon: " +  self.weapon.name.title() + " " + str(self.weapon.value)
        for i in range(0, len(self.items)):
            print self.items[i].name.title() + " " + str(self.items[i].value)   
    
       
    def level_up(self):
            self.experience = 0
            print " you leveled up!"
            self.level += 1
            print "You are now level" + str(self.level)
            print "You get 3 points to put into stats!"
            lvl_points = 3
            print "press 1 to add a point to health"
            print "press 2 to add a point to attack"
            print "press 3 to add a point to magic"
            print "press 4 to add a point to luck"
            while lvl_points > 0 :
                
                inp = raw_input("press a number to add a point to that stat")
                if inp == "1" :
                    self.stats["health"] += 1
                    
                    print "You added a point to health"
                    lvl_points -= 1
                elif inp == "2" :
                    self.stats["attack"] += 1
                    
                    print "You added a point to attack"
                    lvl_points -= 1
                elif inp == "3" :
                    self.stats["magic"] += 1
                    
                    print "You added a point to magic"
                    lvl_points -= 1
                elif inp == "4" :
                    self.stats["luck"] += 1
                    
                    print "You added a point to luck"
                    lvl_points -= 1
                else :
                    print" invalid input, enter a number from 1 to 4"
                    
            self.fullheal()
            self.Checkhp()
            self.realstats()
    def regenerate(self):
        # This function will be used for natural regeneration of Health and mana
        
        
        #Here is the Health portion
        if self.stats["health"] <= 10 :
            self.current_hp += 10
        elif self.stats["health"] <= 20:
            self.current_hp += 20
        elif self.stats["health"] <= 30:
            self.current_hp += 30
        else :
            self.current_hp += 45
        self.Checkhp()   
        # Here is the mana portion
        if self.stats["magic"] <= 5 :
            self.current_mana += 1
        elif self.stats["magic"] <= 10 :
            self.current_mana += 2
        elif self.stats["magic"] <= 15 :
            self.current_mana += 4
        elif self.stats["magic"] <= 20 :
            self.current_mana += 8
        elif self.stats["magic"] <= 25 :
            self.current_mana += 12
        elif self.stats["magic"] <= 30 :
            self.current_mana += 16
        else :
            self.current_mana += 20
        self.Checkhp()
    def fullheal(self):
        #full heal... yay
        self.current_hp += 100000000
        self.current_mana += 100000000
        self.Checkhp()        
    def Checkhp(self):
        # This function will check to make sure your mana and HP never go over what they are supposed to be
        if self.current_hp > self.true_hp :
                self.current_hp = self.true_hp
                
        if self.current_mana > self.true_mana :
                self.current_mana = self.true_mana
        
        
        
        
        
        
        
        
        
        
        