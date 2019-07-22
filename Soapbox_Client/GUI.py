from tkinter.filedialog import *
from tkinter import ttk
from selenium import webdriver
from base_page import BasePage
from Actions import Actions


class MainWindow(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window and button widgets
    def init_window(self):

        # changing the title of our master widget
        self.master.title("SoapBox")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # creating a close button instance
        closeButton = Button(self, text="Close Page",command=self.client_exit)
        # placing the button on my window
        closeButton.place(x=250, y=125)
        # creating a scan button instance
        # scanButton = Button(self, text="Run!",command=lambda: Actions.SoapBox)
        scanButton = Button(self, text="Run!", command=lambda: Actions.SoapBox(self,var1,var2,var3))
        # , command = lambda: Actions.SoapBox(.get()
        # placing the button on my window
        scanButton.place(x=500, y=425)

        #place some checkboxes
        # option =["https://old.reddit.com/","b","c","d"]
        # x = 350
        # y = 225
        # for item in option:
        #     item = Checkbutton(self, text=str(item), fg="red")
        #     item.place(x=x,y=y)
        #     y+=20

        #reddit button
        var1 = IntVar()
        chk1 = Checkbutton(self, text=str("Reddit"), fg="red", variable=var1)
        chk1.place(x =350, y=225)
        #twitter button
        var2 = IntVar()
        chk2 = Checkbutton(self, text=str("Twitter"), fg="red", variable=var2)
        chk2.place(x=350, y=245)
        #LinkedIn button
        var3 = IntVar()
        chk3 = Checkbutton(self, text=str("LinkedIn"), fg="red", variable=var3)
        chk3.place(x=350, y=265)
        #get value of checkboxes


    def client_exit(self):
        exit()




# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("800x600")

# creation of an instance
app = MainWindow(root)

# mainloop
root.mainloop()