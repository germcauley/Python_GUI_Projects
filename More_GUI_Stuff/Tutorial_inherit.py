from tkinter.filedialog import *
import requests, os, sys
from selenium import webdriver
from Tutorial import App

import datetime


class FileFunctions(App):

    def OpenFile(self):
        name = askopenfilename(initialdir="",
                               filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                               title="Choose a file."
                               )
        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            with open(name, 'r') as f:
                with open("out.txt", "w") as f1:
                    for line in f:
                        f1.write(line)
                f1.close()
        except:
            print("No file exists")

    def client_exit(self):
        quit()

    def Scanner(self,env,dom):
        filename = (env+dom) + ".txt"
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
                status = requests.options(line).status_code

                print("Status: " + str(status))
                print("Actual URL: " + driver.current_url)
                url = driver.current_url
                current_status = status = requests.options(url).status_code
                print("Current status: " + str(current_status))
                print(" --------------------------")

                # if "https://www.bankofireland.com/" in url:
                # code = requests.options(line).status_code
                #Resultsfile.write(line + str(status) + '/n')
            except:
                print("Encountered an error with: " + driver.current_url)
        print('Script has finished running,all links have been scanned!')
        input("Press Enter to continue...")
        driver.quit()  # end driver
        exit()
        #Resultsfile.close()  # close file with all results