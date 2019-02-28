# Simple enough, just import everything from tkinter.
from tkinter import *
from tkinter.filedialog import *
import requests, os, sys
from selenium import webdriver
import subprocess

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

        # adds a command to the menu option, calling it exit, and the

        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # command it runs on event is client_exit
        file.add_command(label="LoadFile", command=self.OpenFile)

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
        quitButton = Button(self, text="Exit", command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=125, y=125)

        # creating a button instance
        loadButton = Button(self, text="Load File", command=self.OpenFile)

        # placing the button on my window
        loadButton.place(x=250, y=125)

        # creating a button instance
        scanButton = Button(self, text="Start Scan", command=self.Lighthouse_Scan)

        # placing the button on my window
        scanButton.place(x=375, y=125)

    def client_exit(self):
        exit()

    def OpenFile(self):

        # with open("in.txt") as f:
        #     with open("out.txt", "w") as f1:
        #         for line in f:
        #             if "ROW" in line:
        #                 f1.write(line)



        name = askopenfilename(initialdir="",
                               filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file."
                               )
        # print(name)

        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            with open(name, 'r') as f:
                with open("out.txt", "w") as f1:
                    for line in f:
                         f1.write(line)
                f1.close()
        except:
            print("No file exists")


    def Scan_Urls(self):

        filename = "out.txt"
        # filename = "/Users/gmcauley/Desktop/file.txt"
        file = open(filename, "r")

        # initialize the driver
        driver = webdriver.Chrome()
        # Create a file and write results to it
        #Resultsfile = open("NewTestResultsFile.txt", "w")
        # Get URLS from  x global var
        for line in file:
            print("Requesting: " + line)
            try:
                driver.get(line)
                # url = driver.current_url
                print("Requesting: " + line)
                status = requests.options(line).status_code
                print("Status: " + str(status))
                print("Actual URL: " + driver.current_url)
                url = driver.current_url
                current_status = status = requests.options(url).status_code
                print("Current status: " + str(current_status))
                print(" --------------------------")
                # if "https://www.bankofireland.com/" in url:
                code = requests.options(line).status_code
                #Resultsfile.write(line + str(status) + '/n')

            except:
                print("Encountered an error with: " + driver.current_url)

        print('Script has finished running,all links have been scanned!')
        input("Press Enter to continue...")
        driver.quit()  # end driver
        #Resultsfile.close()  # close file with all results

    def Lighthouse_Scan(self):

        urlFile = open("urls.txt", "r")

        bashCommand = 'lighthouse "$(<urls.txt)" --disable-cpu-throttling --disable-network-throttling --disable-device-emulation --html'
        bashCommand2 = 'lighthouse "https://www.bankofireland.com/" --disable-cpu-throttling --disable-network-throttling --disable-device-emulation --html'

        urls = urlFile.readline().split(",")
        myurl = "https://www.bankofireland.com/"

        for x in urls:
            subprocess.check_call(
                'lighthouse "%s" --disable-cpu-throttling --disable-network-throttling --disable-device-emulation --html ' % x,
                shell=True)


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("600x400")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
