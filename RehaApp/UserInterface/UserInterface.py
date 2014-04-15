import threading
from tkinter import *
from tkinter.tix import *

from Article import Article
from XMLManager import XMLManager

class UserInterface(threading.Thread):
    
    def __init__(self, manag, Debug=False):
        
        self.debug = Debug
        self.xmlManager = manag
        
        self.ArticleList = self.xmlManager.getArticleName()
        
        self.info = []
        
        threading.Thread.__init__(self)
        self.setName("GUI")
        
        self.fenetre = Tk()
        self.fenetre.title("RehaApp")
        
        self.initLog()
        self.initArticle()
        self.initCategorie()
        self.initCommand()
        self.initText()
        
        self.start()
        
    def run(self):
        
        self.fenetre.mainloop()
        
    def initLog(self):
        """
        Log
        """
        
        self.logbox = Frame(self.fenetre)
        self.logbox.pack(side="top", expand=True, fill="x", padx=10)
        
        self.log = Label(self.logbox, text="Welcome to RehaApp", anchor="w")
        self.log.pack()
    
    def initArticle(self):
        
        """
        Article
        """
        self.articlebox = Frame(self.fenetre)
        self.articlebox.pack(side="top", expand=True, fill="x", padx=19, pady=10)
        
        self.Article = ComboBox(self.articlebox, editable=True)
        self.Article.configure(command=lambda x: self.Selection())
        self.Article.pack(anchor="w", expand=True, fill="x")
        
        for x in self.ArticleList:
            self.Article.insert(END, x)
        
        self.Article.subwidget("label").configure(text="Article", width=10, anchor="w")
        
        
    def initCategorie(self):
        
        self.categoriebox = Frame(self.fenetre)
        self.headingbox   = Frame(self.categoriebox)
        self.shortTextbox = Frame(self.categoriebox)
        self.thumbnailbox = Frame(self.categoriebox)
        
        self.categoriebox.pack(side="top", expand=True, fill="x", padx=10)
        self.headingbox.pack(  side="top", expand=True, fill="x", padx=10, pady=5)
        self.thumbnailbox.pack(side="top", expand=True, fill="x", padx=10, pady=5)
        self.shortTextbox.pack(side="top", expand=True, fill="x", padx=10, pady=5)
        
        self.initHeading(self.headingbox)
        self.initThumbnail(self.thumbnailbox)
        self.initShortText(self.shortTextbox)
      
    def initHeading(self, box):
        
        """
        Heading
        """
        self.labHeading = Label(box, anchor="w", text="Heading", width=10)
        self.labHeading.pack(side="left", expand=False, anchor="w")
        
        self.varHeading = StringVar()
        self.heading = Entry(box, textvariable=self.varHeading)
        self.heading.pack(side="right", expand=True, fill="x")
        
        self.info.append(self.heading)
        
    def initThumbnail(self, box):
        
        """
        #Thumbnail
        """
        self.labThumbnail = Label(box, anchor="w", text="Thumbnail", width=10)
        self.labThumbnail.pack(side="left", expand=False, anchor="w")
        
        self.varThumbnail = StringVar()
        self.thumbnail = Entry(box, textvariable=self.varThumbnail)
        self.thumbnail.pack(side="right", expand=True, fill="x")
        
        self.info.append(self.thumbnail)
    
    def initShortText(self, box):
        
        """
        ShortText
        """
        self.labShortText = Label(box, anchor="w", text="ShortText", width=10)
        self.labShortText.pack(side="left", expand=False, anchor="w")
        
        self.varShortText = StringVar()
        self.shortText = Entry(box, textvariable=self.varShortText)
        self.shortText.pack(side="right", expand=True, fill="x")
        
        self.info.append(self.shortText)
            
    def initText(self):
        
        """
        Text
        """
        self.textbox = Frame(self.fenetre)
        self.textbox.pack(expand=True, fill="both", padx=20, pady=10)
        
        self.labMessage = Label(self.textbox, anchor="w", text="Message", width=10)
        self.labMessage.pack(side="left")
        
        self.scrollbar = Scrollbar(self.textbox)
        self.scrollbar.pack(side="right", fill="y")
        
        self.varText = StringVar()
        self.text = Text(self.textbox, wrap="word", width=60, height=10)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.text.pack(side="left", expand=True, fill="both")
    
    def initCommand(self):
        
        """
        Save
        """
        self.cmdbox = Frame(self.fenetre)
        self.cmdbox.pack(side="bottom", expand=True, fill="x", padx=10, pady=20)
        
        self.labEmpty = Label(self.cmdbox, text="", width=11)
        self.labEmpty.pack(side="left")
        
        self.btSave = Button(self.cmdbox, text="Save", width=10)
        self.btSave.config(command=lambda: self.Save())
        self.btSave.pack(side="left")
        
        self.btNew = Button(self.cmdbox, text="New", width=10)
        self.btNew.config(command=lambda: self.New())
        self.btNew.pack(side="left")
        
        self.btRemove  = Button(self.cmdbox, text="Remove", width=10)
        self.btRemove.config(command=lambda: self.Remove())
        self.btRemove.pack(side="left")
        
    
    def Selection(self):
        
        listInfo = self.xmlManager.getInfo(self.Article.cget("value"))
        
        for element, info in zip(self.info, listInfo):
            element.delete(0,END)
            element.insert(INSERT, info)
        
        if self.text.get("1.0", END) != "":
            self.text.delete("1.0", END)
        self.text.insert(INSERT, listInfo[3])
            
    def New(self):
        self.xmlManager.newArticle(self.Article.cget("selection"))
        self.Refresh()
        
    def Remove(self):
        if self.Article.cget("selection") != "":
            article = self.Article.cget("value")
            self.xmlManager.removeArticle(article)
            
            self.Refresh()
            self.Article.configure(selection="")
            for x in self.info:
                x.delete(0,END)
            self.text.delete("1.0", END)
            
    def Save(self):
        if self.Article.cget("selection") != "":
            listInfo = []
            listInfo.append(self.Article.cget("selection"))
            listInfo.append(self.heading.get())
            listInfo.append(self.thumbnail.get())
            listInfo.append(self.shortText.get())
            listInfo.append(self.text.get("1.0", END))
            
            self.xmlManager.Save(self.Article.cget("value"), listInfo)        
        
        
    def Refresh(self):
        listName = self.xmlManager.getArticleName()
        self.Article.subwidget("listbox").delete(0,END)
        for x in listName:
            self.Article.insert(END, x)
        
if __name__ == '__main__':
    test = UserInterface(Debug=True)