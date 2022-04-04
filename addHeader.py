
import tkinter as Tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)

        
        # building conainer for our button and text window
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Add Header')
        self.master.config(bg='lightgray')

        # function that holds input data as string value
        self.varAddHeader = StringVar()

        # label for text window
        self.lblAddHeader = Label(self.master, text='Add header here: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblAddHeader.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        # text window for user input
        self.txtAddHeader = Entry(self.master, text=self.varAddHeader, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtAddHeader.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        # submit button
        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)

    # function for adding user input into html h1 tag
    def submit(self):
        head = self.varAddHeader.get()
        file = open('1.html', 'w')
        message = """

        <html>
            <head>
                <title>
                    Gotcha!
                </title>
            </head>
            <body>
                <h1>
                    {}
                </h1>
            </body>    
        </html>
        """.format(head)
        file.write(message)
        file.close()
        webbrowser.open_new_tab('1.html')
        

    
        


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
