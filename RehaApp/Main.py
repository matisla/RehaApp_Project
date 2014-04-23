'''
Created on 15 avr. 2014

@author: Matthieu
'''
import os

from UserInterface.GUI import GUI
from UserInterface.XMLManager import XMLManager

from getpass import getpass

if __name__ == '__main__':
    
    debug = False
        
    myManager = XMLManager()
    myInterface = GUI(myManager)
    
    if debug == True:
        os.system("pause")