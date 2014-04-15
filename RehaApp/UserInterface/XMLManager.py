'''
Created on 11 avr. 2014

@author: Matthieu
'''

from xml.dom import *
from Article import Article

class XMLManager():
    '''
    classdocs
    '''


    def __init__(self, documents=None):
        '''
        Constructor
        '''
        
        self.ArticleList = {}
        
        for x in ["titre 1", "titre 2", "titre 3"]:
            element = Article(x, "head "+x, "short "+x, "thumbnail "+x, "text "+x)
            self.ArticleList[x] = element
        
        
        """self.file = minidom.parse(documents)
        self.article = self.file.getElementsByTagName("Article")
        
        self.title = []
        for tit in self.article:
            self.title.append(tit.childNodes())"""
        
        
    def getArticleName(self):
        listName = []
        for x in self.ArticleList.values():
            listName.append(x.getName())
        listName.sort()
        return listName
    
    def getInfo(self, article):
        listInfo = []
        listInfo.append(self.ArticleList[article].getHeading())
        listInfo.append(self.ArticleList[article].getThumbnail())
        listInfo.append(self.ArticleList[article].getShortText())
        listInfo.append(self.ArticleList[article].getText())
        return listInfo
    
    def newArticle(self, articleName):
        element = Article(articleName)
        self.ArticleList[articleName] = element
        
    def removeArticle(self, article):
        del self.ArticleList[article]
        
    def Save(self, article, listInfo):
        self.ArticleList[article].setName(listInfo[0])
        self.ArticleList[article].setHeading(listInfo[1])
        self.ArticleList[article].setThumbnail(listInfo[2])
        self.ArticleList[article].setShortText(listInfo[3])
        self.ArticleList[article].setText(listInfo[3])
        
        self.SaveXML()
        
    def Read(self):
        print("reading")
        
    def SaveXML(self):
        print("save XML")
        
    def getText(self, article, title):
        print("hello")