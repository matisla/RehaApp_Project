'''
Created on 15 avr. 2014

@author: Matthieu
'''

from UserInterface.UserInterface import UserInterface
from UserInterface.XMLManager import XMLManager

if __name__ == '__main__':
    
    myManager = XMLManager()
    myInterface = UserInterface(myManager)