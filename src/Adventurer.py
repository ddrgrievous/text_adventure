'''
Created on Oct 1, 2015

@author: Jared
'''

class Adventurer(object):
    
    name = ""
    type = ""
    experience = 0
    stats = {'attack' : 0, 'health' : 0, 'magic' : 0, 'luck' : 0}
    level = 0
    items = []
    equipment = []
    spells = []
    def __init__(self):
        pass
    
    def create(self):
        self.name = raw_input("What is your Adventurer's Name?: ")
        print 'Warrior  (6 health, 6 attack, 1 magic, luck 2)'
        print 'Mage     (5 health, 1 attack, 5 magic, luck 4)'
        print 'Beserker (6 health, 9 attack, 0 magic, luck 0)'
        print 'Custom   (? health, ? attack, ? magic, luck ?)'
        self.type = raw_input("Choose a class: ")
        
        if self.type.lower() == 'custom':
            print 'You get a total of 15 points to assign.'
            total_points = 15
            choosing_character = True
            while choosing_character == True:
                for key in sorted(self.stats):
                    print "You have " + str(total_points) + " left"
                    self.stats[key] = int(raw_input( key +"?: "))
                    total_points -= self.stats[key]
                    if total_points <= 0:
                        break
                print "You have Chosen:"    
                for key in sorted(self.stats):
                    print key + ": " + str(self.stats[key])
                
                if raw_input( "Is this correct? (y/n): ").lower() == 'y':
                    choosing_character = False 
                else:
                    total_points = 15
                    
            
        
        
        