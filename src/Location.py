'''
Created on Oct 2, 2015

@author: Jared
'''
from Map import Map 
class Location(object):
    '''
    classdocs
    '''
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.max_x = len(map.spaces[0])
        self.max_y = len(map.spaces)    

    def move_up(self, map):
        new_location = Location(self.x, self.y - 1, map)
        map.update(self, new_location)
        return new_location 
    
    def move_down(self, map):
        new_location = Location(self.x, self.y + 1, map)
        map.update(self, new_location)
        return new_location 
           
    def move_right(self, map):
        new_location = Location(self.x + 1, self.y, map)
        map.update(self, new_location)
        return new_location 

    def move_left(self, map):
        new_location = Location(self.x - 1, self.y, map)
        map.update(self, new_location)
        return new_location             