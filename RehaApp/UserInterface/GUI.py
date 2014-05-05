import threading
from tkinter import *
from tkinter.tix import *

from XMLManager import XMLManager
from getpass import getpass

class GUI(threading.Thread):
    
    def __init__(self, manag, password="rehaapp", Debug=False):
        
        self.Manager = manag
        
        self.tryIncrement = 1
        self.password = password
        self.login = False
        
        self.ArticleList = self.Manager.getAllArticle()
        
        threading.Thread.__init__(self)
        self.setName("GUI")
        
        self.start()
        
    def run(self):
        
        while self.login is False:

            self.initLogin()
            if self.login is False:
                break
            else:
                self.login = True
             
            if self.login:
                self.initApp()
            
            
    
    def initLogin(self):
            
        self.fenetre = Tk()
        self.fenetre.title("RehaApp Login")
        self.fenetre.minsize(500,200)
    
        self.initLogo()
        self.initLog()
        
        self.log.configure(text="Es bleiben Ihnen noch %s Versuche" %(4-self.tryIncrement))
        
        self.pwbox = Frame(self.fenetre)
        self.pwbox.pack(side="bottom", expand=True, fill="x", padx=20)
        
        self.pwLab = Label(self.pwbox, anchor="e", text="Password: ", width=8)
        self.pwLab.pack(side="left", pady=20)
        
        self.pwEntry = Entry(self.pwbox,  show="*")
        self.pwEntry.bind("<Return>", self.testPW)
        self.pwEntry.pack(side="right", expand=True, fill="x")
        self.pwEntry.focus()
        
        self.fenetre.mainloop()
        
    def testPW(self, event):
        
        if self.pwEntry.get() == self.password:
            self.login = True
            self.fenetre.destroy()
        
        elif self.tryIncrement < 3:
            self.login = False
            self.tryIncrement += 1
            self.pwEntry.delete(0, END)
            self.pwEntry.focus()
            
            if self.tryIncrement == 3:
                self.log.configure(text="Es bleibt Ihnen noch %s Versuch" %(4-self.tryIncrement))
            else:
                self.log.configure(text="Es bleiben Ihnen noch %s Versuche" %(4-self.tryIncrement))
                
        else:
            self.login = False
            self.fenetre.destroy()
    
    
    def initApp(self):
        self.fenetre = Tk()
        self.fenetre.title("RehaApp")
        self.fenetre.geometry("600x550")
        self.fenetre.minsize(600,550)
        
        self.initLogo()
        self.initLog()
        self.initArticle()
        self.initCategorie()
        self.initText()
        self.initCommand()
        
        self.fenetre.mainloop()
               
    def initLogo(self):
        
        logobox = Frame(self.fenetre, bg="white")
        logobox.pack(side="top", expand=True, fill="x", padx=20, pady=10)
        
        self.rehaAppLogo = PhotoImage(file="./RehaApp.gif")
        logo1 = Label(logobox, image=self.rehaAppLogo, bg="white")
        logo1.pack(side="left")
        
        self.titleLab = Label(logobox, text="RehaApp XML Editor", bg="white")
        self.titleLab.pack(side="left", expand=True, fill="x")
        
        self.dhbwLogo = PhotoImage(file="./DHBW.gif")
        logo2 = Label(logobox, image=self.dhbwLogo, bg="white")
        logo2.pack(side="right")
            
    def initLog(self):
        
        """
        Log
        """
        self.logbox = Frame(self.fenetre)
        self.logbox.pack(side="top", expand=True, fill="x", padx=20, pady=10)
        
        empty = Label(self.logbox, width=12)
        empty.pack(side="left")
        
        self.log = Label(self.logbox, text = "Willkommen im RehaApp Editor", justify="left")
        self.log.pack(side="left")
    
    def initArticle(self):
        
        """
        Article
        """
        self.articlebox = Frame(self.fenetre)
        self.articlebox.pack(side="top", expand=True, fill="x", padx=19, pady=10)
        
        self.Article = ComboBox(self.articlebox, editable=False)
        self.Article.configure(command=lambda x: self.Selection())
        self.Article.pack(anchor="w", expand=True, fill="x")
        
        self.Article.subwidget("label").configure(text="Menu", width=12, anchor="w")
        
        self.Refresh()
        
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
        self.labHeading = Label(box, anchor="w", text="Titel", width=12)
        self.labHeading.pack(side="left", expand=False, anchor="w")
        
        self.heading = Entry(box)
        self.heading.pack(side="right", expand=True, fill="x")
        
    def initThumbnail(self, box):
        
        """
        #Thumbnail
        """
        self.labThumbnail = Label(box, anchor="w", text="Bild", width=12)
        self.labThumbnail.pack(side="left", expand=False, anchor="w")
        
        self.thumbnail = Entry(box)
        self.thumbnail.pack(side="right", expand=True, fill="x")
        
    def initShortText(self, box):
        
        """
        ShortText
        """
        self.labShortText = Label(box, anchor="w", text="Beschreibung", width=12)
        self.labShortText.pack(side="left", expand=False, anchor="w")
        
        self.shortText = Entry(box)
        self.shortText.pack(side="right", expand=True, fill="x")
            
    def initText(self):
        
        """
        Text
        """
        self.textbox = Frame(self.fenetre)
        self.textbox.pack(expand=True, fill="both", padx=20, pady=10)
        
        self.labMessage = Label(self.textbox, anchor="w", text="Text", width=12)
        self.labMessage.pack(side="left")
        
        self.scrollbar = Scrollbar(self.textbox, jump=1)
        self.scrollbar.pack(side="right", fill="y")
        
        self.text = Text(self.textbox, wrap="word", width=60, height=10)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        self.text.pack(side="left", expand=True, fill="both")
    
    def initCommand(self):
        
        """
        Save
        """
        self.cmdbox = Frame(self.fenetre)
        self.cmdbox.pack(side="bottom", expand=True, fill="x", padx=20, pady=20)
        
        self.labEmpty = Label(self.cmdbox, text="", width=12)
        self.labEmpty.pack(side="left")
        
        self.btNew = Button(self.cmdbox, text="Neuer Artikel", width=10)
        self.btNew.config(command=lambda: self.New())
        self.btNew.pack(side="left")
        
        self.labEmpty2 = Label(self.cmdbox, text="", width=5)
        self.labEmpty2.pack(side="left")
        
        self.btRemove  = Button(self.cmdbox, text="Loeschen", width=10)
        self.btRemove.config(command=lambda: self.Remove())
        self.btRemove.pack(side="left")
        
        self.labEmpty3 = Label(self.cmdbox, text="", width=5)
        self.labEmpty3.pack(side="left")
        
        self.btSave = Button(self.cmdbox, text="Bestaetigen", width=10)
        self.btSave.config(command=lambda: self.Save())
        self.btSave.pack(side="right")
        
        self.labEmpty4 = Label(self.cmdbox, text="", width=5)
        self.labEmpty4.pack(side="right")
        
        self.btSave = Button(self.cmdbox, text="Logout", width=10)
        self.btSave.config(command=lambda: self.logout())
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
        self.log.configure(text = "Benutzen Sie nicht ein schon existierenden Titel")
        self.heading.focus()
        
    def Remove(self):
        if self.Article.cget("value") != "":
            article = self.Article.cget("value")
            self.Manager.rmArticle(article)
            
            self.log.configure(text = 'Der Artikel "%s" wurde geloescht' %(article))
            self.Refresh()
            self.ClearAll()
            
    def Save(self):
        if self.heading.get() != "":
            listInfo = []
            
            listInfo.append(self.heading.get())
            listInfo.append(self.shortText.get())
            listInfo.append(self.thumbnail.get())
            listInfo.append(self.text.get("1.0", END))
            
            article = self.Article.cget("value")
            
            if self.Manager.saveArticle(article, listInfo):
                self.Refresh()
                self.Article.configure(value=self.heading.get())
                self.log.configure(text = 'Der Artikel "%s" wurde gespeichert' %(listInfo[0]))
                
            else:
                self.heading.focus()
                self.log.configure(text = '[Error] Der Artikel "%s" wurde nicht gespeichert' %(listInfo[0]))
            
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
        
    def logout(self):
        self.fenetre.destroy()
        self.login = False
        
if __name__ == '__main__':
    test = GUI(Debug=True, manag=None)