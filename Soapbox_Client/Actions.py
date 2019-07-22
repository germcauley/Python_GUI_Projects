from tkinter.filedialog import *
import requests, os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from base_page import BasePage
from Reddit import Reddit
from LinkedIn import LinkedIN
import time
import datetime


class Actions(Frame):

    def client_exit(self):
        exit()


    # def SoapBox(self,sites,credentials):
    #     #Take in message/link
    #     #use credentials for each selected site(s)
    #     #post to selected site(s)
    #
    #     # initialize the driver
    #     chrome_options = Options()
    #     chrome_options.add_argument("--headless")
    #     driver = webdriver.Chrome(chrome_options=chrome_options)
    #     # Create a file and write results to it
    #     #Resultsfile = open("NewTestResultsFile.txt", "w")
    #     # Get URLS from  x global var
    #     for line in file:
    #         print("Requesting: " + line)
    #         try:
    #             driver.get(line)
    #             # url = driver.current_url
    #             status = requests.options(line).status_code
    #             print("Status: " + str(status))
    #             print("Actual URL: " + driver.current_url)
    #             url = driver.current_url
    #             current_status = requests.options(url).status_code
    #             print("Current status: " + str(current_status))
    #             print(" --------------------------")
    #             # if "https://www.bankofireland.com/" in url:
    #             # code = requests.options(line).status_code
    #             #Resultsfile.write(line + str(status) + '/n')
    #         except:
    #             print("Encountered an error with: " + driver.current_url)
    #
    #     print('Script has finished running,all links have been scanned!')
    #     input("Press Enter to continue...")
    #     driver.quit()  # end driver
    #     exit()
    #     #Resultsfile.close()  # close file with all results

    def SoapBox(self,v1,v2,v3):
        var1val = Actions.checkbox_value(self,v1)
        var2val = Actions.checkbox_value(self,v2)
        var3val = Actions.checkbox_value(self, v3)

        if var1val > 0:
            print("Login to reddit!")
            driver = webdriver.Chrome()
            driver.get("https://old.reddit.com/")
            driver.quit()
        else:
            print("no reddit!")

        if var2val > 0:
            print("Login to Twitter!")
            driver = webdriver.Chrome()
            driver.get("https://www.twitter.com/")
            driver.quit()
        else:
            print("no twitter!")

        if var3val > 0:
            print("Login to LinkedIn!")
            driver = webdriver.Chrome()
            LinkedIN.LI_post()
            driver.quit()
        else:
            print("no LinkedIn!")

    # Will need to create a separate login function for every site added

    def checkbox_value(self, var):
        return (var.get())
