from tkinter import * #Import Tkinter
from selenium import webdriver #Import WebDriver

Descriptive_Display = Tk(); #Tkinter

ChromeDrive = 'C:\Program Files\chromedrive'
Icon = PhotoImage(file='Message-Py\src\Logo.png')

Descriptive_Display.iconphoto(True, Icon)
WebDriver = webdriver.Chrome()
#------------VERSION 0.0-------------#
#------------------------------------#

#-----------DESCRIPTION-------------------- #
# Send A YouTube Comment With link Provided #
#-------------------------------------------# 

#------------TEXTBOX------------------------#
CommentBox = Entry(
    fg="#ffffff",background="black", width=50, font="consolas"
); CommentBox.pack(pady=5); #Comment Box 
LinkBox = Entry(
     fg="#ffffff",background="black", width=30, font="console"
); LinkBox.pack(); #YouTube Link
#--------------------------------------------#

def SendComment():
    Converted = str(LinkBox.get()); Comment = WebDriver.find_element("id", "contenteditable-root");
    WebDriver.get(Converted)
#-------------- BUTTON---------------------#
PostButton = Button(text="Post Comment"
,command=SendComment); PostButton.pack(pady=5) 
#--------------------------------------------#

#Configuration Method [  # Argument 1: Geomatry, Argument 2: BG, Argument 3: Title ]
#Description: Confirugation Of Tkinter
def Configuration(Content = []):
     #Stores Everything Within List
   for _Index in range(len(Content)): #Iterates Through Content
    if not isinstance(Content[_Index], str): 
        return
    else:
        Descriptive_Display.title(Content[2] ) # [Register-Py]
        Descriptive_Display.geometry(Content[0]) # [800x600]
        Descriptive_Display.config(background=Content[1]) # [Black]

#Main Method [No Arguments ]
#Description: Manager Of Every Method
def Main():
     Configuration(["500x100","black","Message-Py"])
Main()
Descriptive_Display.mainloop()
