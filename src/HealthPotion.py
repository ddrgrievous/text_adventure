'''
Created on Oct 8, 2015

@author: Jared
'''

from Item import Item
class HealthPotion(Item):
    '''
    classdocs
    '''

    type = 'usable'
    def __init__(self, potency, name, value):
        '''
        Constructor
        '''
        self.potency = potency
        super(HealthPotion,self).__init__(name, value)
    

    def use(self, my_adventurer):
        my_adventurer.current_hp += self.potency
        if my_adventurer.current_hp >= my_adventurer.real_hp :
            my_adventurer.current_hp = my_adventurer.real_hp