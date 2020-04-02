import sys                      ##usesd so that i can shoe the version of python i am using
import tkinter
import os
from tkinter.filedialog import *   ## so that i can show a new dialog box when clicking a open or save button
from tkinter import messagebox   # to show a message box
from tkinter import scrolledtext
win=tkinter.Tk()                # main window
win.title('File menu')         # used to give a title
win.geometry('250x100')        # setting size       
menuBar=tkinter.Menu(win)   
win.config(menu=menuBar)       # configuring menu bar in window
thisTextArea = Text(win)
scroll_bar = Scrollbar(thisTextArea)
file = None
thisTextArea.grid(sticky=N + S + E + W)
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)
thisTextArea = Text(win)
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width = scrolW, height =scrolH, wrap = tkinter.WORD)
file = None
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=thisTextArea.yview)
thisTextArea.config(yscrollcommand=scroll_bar.set)   

def openFile():
    global thisTextArea
    global file
    global win
    file = askopenfilename(defaultextension=".txt")
    if file == " ":  
       file = None
    else:
        win.title(os.path.basename(file)) 
        thisTextArea.delete(1.0,END) 
        file = open(file,"r")
        thisTextArea.insert(1.0,file.read()) 
        file.close() 
     
    

def saveFile(self):

    if file == None: 
            file = asksaveasfilename(initialfile='Untitled.txt') 
  
            if file == "": 
                file = None
            else:   
                file = open(file,"w") 
                file.write(self._thisTextArea.get(1.0,END)) 
                file.close() 
                win.root.title(os.path.basename(self.file) + " - Notepad")
                

def closeWindow():
    win.destroy()   # for closing the window

def message():
    messagebox.showinfo('Python version', sys.version )        # for showing the python version in a message box
    
    
filemenu=tkinter.Menu(menuBar, tearoff=0)# create file menu in menu bar
helpmenu=tkinter.Menu(menuBar, tearoff=0)# create help menu in menu bar

filemenu.add_command(label='New', command='')# adding a label of New in file menu
filemenu.add_separator() #adding a separtor like a line after new label
filemenu.add_command(label='Open', command=openFile)# adding a label of Open in file menu
filemenu.add_separator()  #adding a separtor like a line after open label
filemenu.add_command(label='Save', command=saveFile)# adding a label of Save in file menu
filemenu.add_separator()  #adding a separtor like a line after save label
filemenu.add_command(label='Exit', command=closeWindow) # adding a label of Exit in file menu
                                                
menuBar.add_cascade(label='File', menu=filemenu) # adding all the labels in filemenu i.e new, open, save, exit in a File menu

helpmenu.add_command(label='About', command =message) # adding a label of About in helpmenu
menuBar.add_cascade(label='Help', menu=helpmenu) #adding the labels in helpmenu i.e about to Help menu

win.mainloop()# wait for interactions

