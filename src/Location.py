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
        if self.y - 1 < 0:
            return False
        else:
            self.y -= 1
            return True
    
    def move_down(self, map):
        new_location = Location(self.x, self.y + 1, map)
        map.update(self, new_location)
        if self.y + 1 > self.max_y:
            return False
        else:
            self.y += 1
            return True 
           
    def move_right(self, map):
        new_location = Location(self.x + 1, self.y, map)
        map.update(self, new_location)
        if self.x + 1 > self.max_x:
            return False
        else:
            self.x += 1
            return True

    def move_left(self, map):
        new_location = Location(self.x - 1, self.y, map)
        map.update(self, new_location)
        if self.x - 1 < 0:
            return False
        else:
            self.x -= 1
            return True              