from tkinter import *


class MyFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master) 
        self.pack(fill="both", expand=True)
        self.config(pady = 30, padx=30,bg= "#E1D7C6")
        

        self.createWidgets()

    def createWidgets(self): 
        
        
        #Beispiel Label
        self.bspLabel = Label(self,text="Beispiel Label")
        self.bspLabel.grid(row=0,column=0)
        # alle Optionen für Label ausgeben

        #Beispiel Button
        self.bspButton = Button(self,text="bspButton",command=self.eventHandlerButton,bg="#ffdddd")
        self.bspButton.grid(row=1,column=0)
        # alle Optionen für Button ausgeben

    
    # Alle Eventhandler 
    def eventHandlerButton(self):
        pass


#Fenster erzeugen           
root = Tk()
root.title("Fenstertitel")
root.config(padx=20, pady=20, bg = "#3C6255")
root.geometry("600x600")
  


#MyFrame erzeugen
rahmen = MyFrame(root)       
root.mainloop()

