'''
Created on Oct 1, 2015

@author: Jared
'''

class Adventurer(object):
    
    name = ""
    def __init__(self):
        pass
    
    def create(self):
        self.name = raw_input("What is your Adventurer's Name?:")
        