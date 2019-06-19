# Simple enough, just import everything from tkinter.
from tkinter.filedialog import *
from File_Functions import FileFunctions


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
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

        #Instantiates a class with all file commands, open, exit etc
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

        # creating a button instance
        scanButton = Button(self, text="Start Scan", command=self.Scan_Urls)

        # placing the button on my window
        scanButton.place(x=375, y=125)


        #place a listbox
        Lb1 = Listbox(self)
        Lb1.insert(1, "DEV")
        Lb1.insert(2, "STG")
        Lb1.insert(3, "PROD")
        Lb1.place(x=350, y=225)

        #create Text Widget
        T = Text(root, height=2, width=30)
        T.pack()
        T.insert('1.0', 'here is my text to insert')


    def Scan_Urls(self,x="www.google.com"):

        print(str(x))


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("600x400")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
