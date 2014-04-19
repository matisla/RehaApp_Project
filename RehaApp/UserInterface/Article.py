'''
Created on 15 avr. 2014

@author: Matthieu
'''

class Article():
    '''
    classdocs
    '''

    def __init__(self):
        
        self.heading   = "heading"
        self.shortText = "ShortText"
        self.thumbnail = "Tumbnail"
        self.text      = "Text"


        
    def getList(self):
        return[self.heading, self.shortText, self.thumbnail, self.text]
        
    """
    Getter
    """
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
    def setHeading(self, value):
        self.heading = value

    def setShortText(self, value):
        self.shortText = value

    def setThumbnail(self, value):
        self.thumbnail = value

    def setText(self, value):
        self.text = value
