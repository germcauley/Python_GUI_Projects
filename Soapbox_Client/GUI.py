from tkinter.filedialog import *
from tkinter import ttk


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




# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("600x400")

# creation of an instance
app = MainWindow(root)

# mainloop
root.mainloop()