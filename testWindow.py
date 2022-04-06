
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.config(bg='lightgray')

        self.varFileTransfer = StringVar()
        self.varFileTransfer2 = StringVar()
        
        self.lblsource = Label(self.master, text='File Source:', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblsource.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.txtsource = Entry(self.master, text=self.varFileTransfer, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtsource.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.btnSelect1 = Button(self.master, text='select source', width=10, height=2, command=self.foldersearch1)
        self.btnSelect1.grid(row=1, column=1, padx=(0,0), pady=(30,0))

        self.lbldestination = Label(self.master, text='file destination', font=('Helvetica', 16),fg='black', bg='lightgray')
        self.lbldestination.grid(row=2, column=1, padx=(30,0), pady=(30,0))

        self.txtsource2 = Entry(self.master, text=self.varFileTransfer2, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtsource2.grid(row=3, column=1, padx=(30,0), pady=(30,0))


        self.btnSelect2 = Button(self.master, text='select destination', width=10, height=2, command=self.foldersearch2)
        self.btnSelect2.grid(row=4, column=1, padx=(30,0), pady=(30,0))

        self.btnSend = Button(self.master, text='send files', width=10, height=2, command=self.FileTransfer)
        self.btnSend.grid(row=5, column=1, padx=(30,0), pady=(30,0))

    def foldersearch1(self):
        self.varFileTransfer = filedialog.askdirectory()
        self.txtsource.delete(0, END)
        self.txtsource.insert(0, self.varFileTransfer)
            
        print()

    def foldersearch2(self):
        self.varFileTransfer2 = filedialog.askdirectory()
        self.txtsource2.delete(0, END)
        self.txtsource2.insert(0, self.varFileTransfer2)
        print()

    def FileTransfer(self):
        source = self.txtsource.get()+"/"
        destination = self.txtsource2.get()+"/"
        files = os.listdir(source)
        for i in files:
            filepath = os.path.join(source, i)
            modTime = os.path.getmtime(filepath)
            print(modTime)
            secondsintheday = 24*60*60
            now = time.time()
            before = now - secondsintheday
            if modTime > before:
                destPath = os.path.join(destination, i)
                shutil.move(filepath, destPath)    


if __name__ == "__main__":
         root = tk.Tk()
         App = ParentWindow(root)
         root.mainloop()
