from tkinter import *


class MyFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master) 
        self.pack(fill="both", expand=True)
        self.config(pady = 30, padx=30, bg= "#E1D7C6")
        

        self.createWidgets()

    def createWidgets(self): 
        self.canvas = Canvas(self, height=450, bg= "#E1D7C6", relief="sunken", highlightthickness=0)
        self.canvas.pack()
        
        self.bspButton = Button(self,text="bspButton", bg="#ffdddd")
        self.bspButton.pack()

        
        

#Fenster erzeugen           
root = Tk()
root.title("Fenstertitel")
root.config(padx=20, pady=20, bg = "#3C6255")
root.geometry("600x600")
  


#MyFrame erzeugen
rahmen = MyFrame(root)       
root.mainloop()

