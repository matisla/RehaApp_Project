'''
Created on 15 avr. 2014

@author: Matthieu
'''

class Article():
    '''
    classdocs
    '''

    def __init__(self, nom, head="None", describe="None", nail="None", txt="write a message here"):
        
        self.name      = nom
        self.heading   = head
        self.shortText = describe
        self.thumbnail = nail
        self.text = txt
        
        
    def Save(self):
        print("Sauvegarde")
       
    
    """
    Getter
    """
    def getName(self):
        return self.name
    
    def getHeading(self):
        return self.heading

    def getShortText(self):
        return self.shortText

    def getThumbnail(self):
        return self.thumbnail

    def getText(self):
        return self.text

    """
    Setter
    """
    def setName(self, value):
        self.name = value
        
    def setHeading(self, value):
        self.heading = value

    def setShortText(self, value):
        self.shortText = value

    def setThumbnail(self, value):
        self.thumbnail = value

    def setText(self, value):
        self.text = value
