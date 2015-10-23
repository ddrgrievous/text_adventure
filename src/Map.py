'''
Created on Oct 1, 2015

@author: Jared
'''
from sysconfig import sys
from random import randint
class Map(object):

    current_space = ' '
    spaces = []
    
    def __init__(self, rows, cols):
        
        # create board based on parameters
        for i in range(0,rows):
            self.spaces.append([])  
             
        for i in range(0, rows):
            for j in range(0, cols):
                self.spaces[i].append('?')
    
        # start the adventurer in a blank space
        self.spaces[0][0] = ' '            
        
    def display(self, advent_loc):
        self.spaces[advent_loc.y][advent_loc.x] = '*'
        for y in range(0,len(self.spaces)):                
            for x in range(0, len(self.spaces[y])):
                if x == 0:
                    print "\n|" + self.spaces[y][x] + "|",
                else:                
                    sys.stdout.write(self.spaces[y][x] + "|")
        print'\n'
    
    def update(self, old_location, new_location):

        # set the location from * back to what it used to be
        self.spaces[old_location.y][old_location.x] = self.current_space
            
        # if the location hasn't be discovered we need to assign it
        if self.spaces[new_location.y][new_location.x] == '?':            
            self.current_space = self.discover_location()
        else:
            self.current_space = self.spaces[new_location.y][new_location.x]
            
        # the new space is now occupied by the adventurer    
        self.spaces[new_location.y][new_location.x] = '*'
        
    def monsterdeath(self):
        self.current_space = " "
    def discover_location(self):
        random_num = randint(1, 100)
        
        if random_num % 15 == 0:
            return 'D'
        elif random_num % 10 == 0:
            return 'C'
        elif random_num % 2 == 0:
            return 'M'
        else:
            return ' '                 