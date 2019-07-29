from selenium import webdriver



filename1 = '/Users/gmcauley/PycharmProjects/GUI_TEST_LIST_URLS/Misc_Scripts/new_urls.txt'
filename2 = '/Users/gmcauley/PycharmProjects/GUI_TEST_LIST_URLS/Misc_Scripts/postfix.txt'

term = open(filename1, "r")
urls = open(filename2, "r")
num =1
# for line in urls:
#     print(term[num] + "     "+ urls[num])
#     num +=1

term = open(filename1, "r")
urls = open(filename2, "r")
for i,j in zip(term,urls):
    print(i+j)

