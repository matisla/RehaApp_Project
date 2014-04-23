'''
Created on 11 avr. 2014

@author: Matthieu
'''

from xml.dom.minidom import Document, parse
from Article import Article

class XMLManager():
    '''
    classdocs
    '''


    def __init__(self, documents=None, Debug=False):
        
        self.debug = Debug
        
        self.ArticleList = {}

        self.Read()

    def getAllArticle(self):
        ArticleList = []
        
        if self.ArticleList != {}:
            for x in self.ArticleList.values():
                ArticleList.append(x.getHeading())
            
            try: 
                ArticleList.sort()
            except:
                pass
        
        return ArticleList
    
    def getArticle(self, article):
        return self.ArticleList[article].getList()
        
    def rmArticle(self, article):
        del self.ArticleList[article]
        self.refreshHome()
        
    def saveArticle(self, article, listInfo):
            
        # New
        if listInfo[0] != article and article == "":
            if listInfo[0] not in self.ArticleList:
                self.ArticleList[listInfo[0]] = Article()
                
                self.ArticleList[listInfo[0]].setHeading(listInfo[0])
                self.ArticleList[listInfo[0]].setShortText(listInfo[1])
                self.ArticleList[listInfo[0]].setThumbnail(listInfo[2])
                self.ArticleList[listInfo[0]].setText(listInfo[3])
                
                self.refreshHome()
                return True
            
            else:
                return False
        
        # Heading change
        elif listInfo[0] != article and article != "":
            
            self.ArticleList[listInfo[0]] = self.ArticleList[article]
            del self.ArticleList[article]
            
            self.ArticleList[listInfo[0]].setHeading(listInfo[0])
            self.ArticleList[listInfo[0]].setShortText(listInfo[1])
            self.ArticleList[listInfo[0]].setThumbnail(listInfo[2])
            self.ArticleList[listInfo[0]].setText(listInfo[3])
            
            self.refreshHome()
            return True
        
        # Simple Modification
        elif article != "":
            self.ArticleList[article].setShortText(listInfo[1])
            self.ArticleList[article].setThumbnail(listInfo[2])
            self.ArticleList[article].setText(listInfo[3])
            
            self.refreshHome()
            return True
        
        else:
            return True
            
    def refreshHome(self):
        
        xml = self.generateXML()
       
        if self.debug:
            print(xml.decode())
        
        try:
            f = open("Home.xml", "w", encoding="utf-8")
            f.write(xml.decode())
            
        except:
            print("[Error] in XMLManager, file couldn't be opened !")
        
        finally:
            f.close()
            
    def generateXML(self):
        
        """
        Create the XML File
        """
        document = Document()
        
        home = document.createElement("SmartCruizerData")
        document.appendChild(home)
        
        for element in self.ArticleList.values():
            
            Article = document.createElement("Article")
            home.appendChild(Article)
            
            """
            Heading
            """
            heading = document.createElement("Heading")
            Article.appendChild(heading)
            
            headingValue = document.createTextNode(element.getHeading())
            heading.appendChild(headingValue)
            
            """
            ShortText
            """
            shortText = document.createElement("ShortText")
            Article.appendChild(shortText)
            
            shortTextValue = document.createTextNode(element.getShortText())
            shortText.appendChild(shortTextValue)
            
            """
            Thumbnail
            """
            Thumbnail = document.createElement("Thumbnail")
            Article.appendChild(Thumbnail)
            
            ThumbnailValue = document.createTextNode(element.getThumbnail())
            Thumbnail.appendChild(ThumbnailValue)
            
            """
            Text
            """
            text = document.createElement("Text")
            Article.appendChild(text)
            
            textValue = document.createTextNode(element.getText())
            text.appendChild(textValue)
            
        return document.toprettyxml(indent="", encoding="utf-8")
    
    
    def Read(self):
        try:
            document = parse("Home.xml")
            
            for element in document.getElementsByTagName("Article"):
                listElement = []
                
                for i in range(1,8,2):
                    try:
                        listElement.append(element.childNodes[i].firstChild.nodeValue)
                    except:
                        listElement.append("")
                
                self.ArticleList[listElement[0]] = Article()
                
                self.ArticleList[listElement[0]].setHeading(listElement[0])
                self.ArticleList[listElement[0]].setShortText(listElement[1])
                self.ArticleList[listElement[0]].setThumbnail(listElement[2])
                self.ArticleList[listElement[0]].setText(listElement[3])
            
        except:
            pass
        