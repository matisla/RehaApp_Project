'''
Created on 15 avr. 2014

@author: Matthieu
'''
import os

from UserInterface.GUI import GUI
from UserInterface.XMLManager import XMLManager

if __name__ == '__main__':
    
    myManager = XMLManager()
    myInterface = GUI(myManager, Debug=True)
    

    #os.system("pause")