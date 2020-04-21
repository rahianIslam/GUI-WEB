# Author: Rahian Islam
import tkinter as tk
from sklearn.utils import shuffle
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox






class TextAnal(ttk.Frame):

    def __init__(self, parent= None):

        super().__init__(parent)
        self.grid(sticky = tk.N+tk.S+tk.W+tk.E)
        self.makewidgets()
        self.file=()


    def makewidgets(self):

        # buttons
        but = ttk.Button(self, text = 'Start Analysis', command = lambda:[self.count_words(),self.count_sentences()])
        but.grid(row=2, column=0)

        #labels 
        ttk.Label(self,text = 'Essay to be Analysed').grid(row=0, column= 0)
        self.input = tk.Text(self, width = 80, height= 20)
        self.input.grid(row=1, column= 0, padx = 5, pady = 5)


        ttk.Label(self,text = 'Result').grid(row=3, column= 0)
        self.result = tk.Text(self, width = 30, height= 5)
        self.result.grid(row=4, column= 0, padx = 5, pady = 5)

 
    def count_words(self):
        file = self.input.get('1.0',tk.END+'-1c').split() 
        # i ahd to open files seperately for all the functions because after going through one of the rfunctions it would stop and my values wopuld be zero. 

        c2 = 0
        for line in file:
            c2 += 1
        a = 'Number of words:'
        self.result.insert('1.0',a)  
        self.result.insert('2.0',c2)  
    
            

    def count_sentences(self):
        file = self.input.get('1.0',tk.END+'-1c').split()
        c1 = 0 
        for line in file:
            for char in line:
                if char == '.' or char == '?' or char == '!':
                    c1 += 1
        b = '          Number of sentences:'
        self.result.insert('3.0',b) 
        self.result.insert('3.1',c1) 







root = tk.Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
TextAnal(root)
root.geometry('1000x700')
root.title('GUI for testing Sneetches')
root.mainloop()