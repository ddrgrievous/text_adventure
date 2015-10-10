'''
Created on Oct 9, 2015

@author: Jared
'''
from Item import Item
class Weapon(Item):
    '''
    classdocs
    '''

    type = 'weapon'
    def __init__(self, attk_mod, name, value):
        '''
        Constructor
        '''
        self.attk_mod = attk_mod
        super(Weapon,self).__init__(name, value)
        