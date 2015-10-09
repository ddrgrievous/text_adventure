'''
Created on Oct 8, 2015

@author: Jared
'''

from Item import Item
class HealthPotion(Item):
    '''
    classdocs
    '''
    

    def __init__(self, potency, name, value):
        '''
        Constructor
        '''
        self.potency = potency
        super(HealthPotion,self).__init__(name, value)
    

    def use(self, my_adventurer):
        my_adventurer.stats['health'] += self.potency