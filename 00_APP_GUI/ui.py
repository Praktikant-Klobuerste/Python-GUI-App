from tkinter import *


class MyFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master) 
        self.grid()

        self.createWidgets()

    def createWidgets(self): 
        

        #Beispiel Button
        self.bspButton = Button(self,text="bspButton",command=self.eventHandlerButton,bg="#ffdddd")
        self.bspButton.grid(row=0,column=0,sticky=EW)
        # alle Optionen für Button ausgeben
        print(self.bspButton.config())
        
        #Beispiel Label
        self.bspLabel = Label(self,text="Beispiel Label")
        self.bspLabel.grid(row=1,column=0,sticky=EW)
        # alle Optionen für Label ausgeben
        print(self.bspLabel.config())
        
        #Beispiel Entry
        #Tkinter String Objekt erzeugen
        self.bspEntryVar = StringVar()
        # Das Textfeld mit der Textvariablen verknüpfen
        self.bspEntry = Entry(self,width=20,textvariable=self.bspEntryVar)
        self.bspEntry.grid(row=2,column=0)
        
        # Das 2. Textfeld mit der gleichen  Textvariablen verknüpfen
        self.bspEntry2 = Entry(self,width=20,textvariable=self.bspEntryVar)
        self.bspEntry2.grid(row=3,column=0)
        
        #Beispiel Canvas
        self.bspCanvas = Canvas(self, width=500,height=500, borderwidth= 2, relief="sunken", bg="#ddddff")
        self.bspCanvas.grid(column= 0,row=4)
        self.bspCanvas.create_oval(20,20,100,100,fill="#ff0000")

    
    # Alle Eventhandler 
    def eventHandlerButton(self):
        print("eventHandlerButton")


#Fenster erzeugen           
root = Tk()
root.title("Fenstertitel")
  


#MyFrame erzeugen
rahmen = MyFrame(root)       
root.mainloop()

