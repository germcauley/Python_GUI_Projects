# Simple enough, just import everything from tkinter.
from tkinter.filedialog import *
from tkinter import ttk
import datetime
import time
from File_Functions import FileFunctions


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class MainWindow(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)



        # reference to the master widget, which is the tk window
        self.master = master


        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Test Vanity Urls")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # Instantiates a class with all file commands, open, exit etc
        fileActions = FileFunctions()

        # adds a command to the menu option, calling it exit, and the

        # command it runs on event is client_exit
        file.add_command(label="Exit", command=fileActions.client_exit)

        # command it runs on event is client_exit
        file.add_command(label="LoadFile", command=FileFunctions.OpenFile)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

        # creating a button instance
        quitButton = Button(self, text="Exit", command=fileActions.client_exit)

        # placing the button on my window
        quitButton.place(x=125, y=125)

        # creating a button instance

        loadButton = Button(self, text="Load File", command=fileActions.OpenFile)

        # placing the button on my window
        loadButton.place(x=250, y=125)

        #Place env Label
        envLabel = Label(self,text="Select an Environment.")
        envLabel .place(x=10, y=10)
        #place a comboboxbox for environments
        combo = ttk.Combobox(self,values=[ "DEV","STG","PROD"])
        combo.place(x=10,y=50)
        cbox = combo

        # Place domain Label
        domainLabel = Label(self, text="Select a Domain.")
        domainLabel.place(x=250, y=10)
        # place a comboboxbox for domain
        combo2 = ttk.Combobox(self, values=["WWW", "PPG"])
        combo2.place(x=250, y=50)
        cbox2 = combo2

        urlLabel = Label(self, text="")
        urlLabel.place(x=150, y=80)

        # creating a scan button instance, pass env list and domain list in
        testButton = Button(self, text="Test Scan", command=lambda: fileActions.Scanner(cbox.get(),cbox2.get(),urlLabel))
        #testButton = Button(self, text="Test Scan", command=lambda: self.UpdateWidget(urlLabel))

        # placing the scan button on my window
        testButton.place(x=375, y=125)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("600x400")

# creation of an instance
app = MainWindow(root)

# mainloop
root.mainloop()
