from tkinter import *
from tkinter import filedialog, Text
import os

WINDOW_COLOR = "#3C6255"
FRAME_COLOR = "#E1D7C6"


class MyFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master) 
        self.pack(fill="both", expand=True)
        self.config(bg=FRAME_COLOR)
        self.apps = []
        

        self.createWidgets()



    def createWidgets(self): 
        self.canvas = Canvas(self, bg = FRAME_COLOR, relief="sunken", highlightthickness=0)
        self.canvas.pack(fill="both")
        
        self.btn_run_apps = Button(self,text="Run Apps", bg=WINDOW_COLOR, fg="white", command=self.runApp)
        self.btn_run_apps.pack(side = BOTTOM)
        
        self.btn_open_file = Button(self,text="Open File", bg=WINDOW_COLOR, fg="white", command=self.addApp)
        self.btn_open_file.pack(side = BOTTOM)



    def addApp(self):

        for widget in self.canvas.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/", 
                                            title="Select File",                                        
                                            filetypes=(("executables", "exe"), ("all files", "*.*"))
                                            )
        if filename:
            self.apps.append(filename)
            print(self.apps)

        for app in self.apps:
            Label(self.canvas, text = app).pack()



    def runApp(self):
        for app in self.apps:
            os.startfile(app)
            
        

#Fenster erzeugen           
root = Tk()
root.title("Start PC")
root.config(padx=30, pady=30, bg = WINDOW_COLOR)
root.geometry("600x600")
  


#MyFrame erzeugen
rahmen = MyFrame(root)       
root.mainloop()

