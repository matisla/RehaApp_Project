import threading
from tkinter import *
from tkinter.tix import *

from XMLManager import XMLManager

class GUI(threading.Thread):
    
    def __init__(self, manag, Debug=False):
        
        self.debug = Debug
        self.Manager = manag
        
        self.ArticleList = self.Manager.getAllArticle()
        
        threading.Thread.__init__(self)
        self.setName("GUI")
        
        self.fenetre = Tk()
        self.fenetre.title("RehaApp")
        self.fenetre.geometry("600x400")
        self.fenetre.minsize(450,400)
        
        self.initLog()
        self.initArticle()
        self.initCategorie()
        self.initText()
        self.initCommand()
        
        
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
        
        self.Article = ComboBox(self.articlebox, editable=False)
        self.Article.configure(command=lambda x: self.Selection())
        self.Article.pack(anchor="w", expand=True, fill="x")
        
        if self.ArticleList != []:
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
        self.shortTextbox.pack(side="top", expand=True, fill="x", padx=10, pady=5)
        self.thumbnailbox.pack(side="top", expand=True, fill="x", padx=10, pady=5)
        
        
        self.initHeading(self.headingbox)
        self.initShortText(self.shortTextbox)
        self.initThumbnail(self.thumbnailbox)
        
      
    def initHeading(self, box):
        
        """
        Heading
        """
        self.labHeading = Label(box, anchor="w", text="Heading", width=10)
        self.labHeading.pack(side="left", expand=False, anchor="w")
        
        self.varHeading = StringVar()
        self.heading = Entry(box, textvariable=self.varHeading)
        self.heading.pack(side="right", expand=True, fill="x")
        
    def initThumbnail(self, box):
        
        """
        #Thumbnail
        """
        self.labThumbnail = Label(box, anchor="w", text="Thumbnail", width=10)
        self.labThumbnail.pack(side="left", expand=False, anchor="w")
        
        self.varThumbnail = StringVar()
        self.thumbnail = Entry(box, textvariable=self.varThumbnail)
        self.thumbnail.pack(side="right", expand=True, fill="x")
        
    def initShortText(self, box):
        
        """
        ShortText
        """
        self.labShortText = Label(box, anchor="w", text="ShortText", width=10)
        self.labShortText.pack(side="left", expand=False, anchor="w")
        
        self.varShortText = StringVar()
        self.shortText = Entry(box, textvariable=self.varShortText)
        self.shortText.pack(side="right", expand=True, fill="x")
            
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
        self.cmdbox.pack(side="bottom", expand=True, fill="x", padx=20, pady=20)
        
        self.labEmpty = Label(self.cmdbox, text="", width=10)
        self.labEmpty.pack(side="left")
        
        self.btNew = Button(self.cmdbox, text="New", width=10)
        self.btNew.config(command=lambda: self.New())
        self.btNew.pack(side="left")
        
        self.labEmpty2 = Label(self.cmdbox, text="", width=5)
        self.labEmpty2.pack(side="left")
        
        self.btRemove  = Button(self.cmdbox, text="Remove", width=10)
        self.btRemove.config(command=lambda: self.Remove())
        self.btRemove.pack(side="left")
        
        self.labEmpty3 = Label(self.cmdbox, text="", width=5)
        self.labEmpty3.pack(side="left")
        
        self.btSave = Button(self.cmdbox, text="Save", width=10)
        self.btSave.config(command=lambda: self.Save())
        self.btSave.pack(side="right")
        
    
    def Selection(self):
        
        if self.Article.cget("value") != "":
            
            element = self.Manager.getArticle(self.Article.cget("value"))
            
            self.Clear()
            
            self.heading.insert(  INSERT, element[0])
            self.shortText.insert(INSERT, element[1])
            self.thumbnail.insert(INSERT, element[2])
            self.text.insert(     INSERT, element[3])
        
        else:
            pass
                
    def New(self):
        self.ClearAll()
        
    def Remove(self):
        if self.Article.cget("value") != "":
            self.Manager.rmArticle(self.Article.cget("value"))
            
            self.Refresh()
            self.ClearAll()
            
    def Save(self):
        if self.heading.get() != "":
            listInfo = []
            
            listInfo.append(self.heading.get())
            listInfo.append(self.thumbnail.get())
            listInfo.append(self.shortText.get())
            listInfo.append(self.text.get("1.0", END))
            
            self.Manager.saveArticle(self.Article.cget("value"), listInfo)
            self.Refresh()
        else:
            pass
        
    def Refresh(self):
        listName = self.Manager.getAllArticle()
        self.Article.subwidget("listbox").delete(0,END)
        
        if listName != "":
            for x in listName:
                self.Article.insert(END, x)
        
    def ClearAll(self):
        self.Article.configure(value="", selection="")
        self.heading.delete(0, END)
        self.shortText.delete(0,END)
        self.thumbnail.delete(0, END)
        self.text.delete("1.0", END)
        
    def Clear(self):
        self.heading.delete(0, END)
        self.shortText.delete(0,END)
        self.thumbnail.delete(0, END)
        self.text.delete("1.0", END)
            
if __name__ == '__main__':
    test = GUI(Debug=True, manag=None)