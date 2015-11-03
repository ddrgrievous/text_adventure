'''
Created on Oct 8, 2015

@author: Jared, Ethan
'''

from Item import Item
class Potion(Item):
    '''
    classdocs
    '''

    type = 'usable'
    def __init__(self, potency, name, value):
        '''
        Constructor
        '''
        self.potency = potency
        super(Potion,self).__init__(name, value)
    

    def use(self, my_adventurer):
        my_adventurer.current_hp += self.potency
        my_adventurer.Checkhp()