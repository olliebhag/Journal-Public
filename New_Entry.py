
import tkinter as tk ##from https://www.youtube.com/watch?v=D8-snVfekto&list=PLsmaE85R7RwyaAqcLC_XQlKuNbEQSy5Nv&index=1&t
from tkinter import scrolledtext
from tkinter.ttk import OptionMenu

##First functions
def date():
    from datetime import date
    from datetime import datetime

    today = date.today() ##from https://www.programiz.com/python-programming/datetime/current-datetime

    global day
    global month
    global year
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    print("The year is "+ year+" and the month is "+month+" and the day is "+day)

    global today_correct
    today_correct=today.strftime("%d.%m.%Y")

    print("The date=", today_correct+"\n")

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    global hour
    global minute

    hour=now.strftime("%H")
    minute=now.strftime("%M")
    print("Current Time =", current_time)
date()


def get_title(): ##pass into DB later
    
    print (title_entry)
    output= tk.Label(frame,text=title_entry.get())
    output.grid(row=3, column=3)

def get_mood():

    output= tk.Label(frame,text=options.get()) 
    output.grid(row=3, column=4)


def title_check():
    ##checks if title is above 2 characters
    title = title_entry.get()
    titlelength = len(title)
    if titlelength>=2:
        write_journal()
    
    else:
        smalltitle = tk.Label(frame,text="Two characters \nneeded for title",font= ('Calibri', 12,))
        smalltitle.grid(row=5,column=2, pady = 2, padx= 5) ##leaves pixel space between adjacent objects
    

def write_journal():
    import os
    
    user_profile = os.environ['USERPROFILE']
    user_current_date = user_profile + "\Desktop/journal_text/"+today_correct ##makes a path to current date folder
    
    file_name = title_entry.get()+".txt" 
    
    global completePath
    completePath = os.path.join(user_current_date, file_name) ##makes a path to the file
    print(completePath)
    
    
    file1 = open(completePath, "w")
    userWrite=str(journal_text.get("1.0","end")) #gets all text box content in variable

    file1.write(userWrite) #writes all text box content to file
    file1.close()


    fileCount = open(completePath, "rt") #opens created file
    data = fileCount.read() ##gets data from file
    words = data.split() ##counts words in file by splitting
    global wordCount
    wordCount = len(words)
    fileCount.close()

    newEntry()

def mainmenu():
    import os
    os.system('python mainmenu.py')

def closewindow():
    root.destroy()

def newEntry():
    import sqlite3
    ## tutorial from https://likegeeks.com/python-sqlite3-tutorial/#Create_Connection
    con = sqlite3.connect('Journal.db') 
    
    def sql_insert(con, entities):
    
        cursorObj = con.cursor()
        
        cursorObj.execute('INSERT INTO Entries(ID, Title , FilePath , Day , Month , Year, Hour, Minute, Mood , Label, WordCount) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
        
        con.commit()
    
    #title and primary key
    short_userTitle= title_entry.get()[0:4] ##shortens title for primary key usage
    print (short_userTitle)
    userID = short_userTitle+today_correct #makes primary key
    print (userID)
    
    
    entities = (userID, title_entry.get(), completePath, day, month, year, hour, minute, options.get(), label_entry.get(), wordCount)
    #gets entry properties and creates new db record
    
    sql_insert(con, entities)

    root.destroy()
    mainmenu()


root = tk.Tk()

root.title("Text maker")
canvas = tk.Canvas(root, height=970, width=900)
canvas.pack() ##creates canvas in root and defines size

frame= tk.Frame(root,bg= "#34568B")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)  
##places frame with position and size relative to the window

##design
journal_label = tk.Label(frame,text="Journal", font= ('Calibri', 20, "bold"))
journal_label.grid(row=0,column=0, pady = 2, padx= 5) ##leaves pixel space between adjacent objects

back_button= button = tk.Button(frame,text="Exit without\nsaving", font= ('Calibri', 16, ),command=lambda: [closewindow(),mainmenu()]) ##get from https://www.youtube.com/watch?v=7A_csP9drJw
back_button.grid(row=2, column=2, pady = 10)


##title
title_label = tk.Label(frame,text="Title (Don't use similar titles\n on the same day):",font= ('Calibri', 11, ) )
title_label.grid(row=1,column=0)

title_entry = tk.Entry(frame, width=40)
title_entry.grid(row=1, column=1)

##mood
mood_label = tk.Label(frame,text="Mood (1-10):",font= ('Calibri', 18, ))
mood_label.grid(row=2, column=0)

##from https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter
from tkinter import *
mood_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]
options = StringVar(root)
options.set(mood_options[0]) #default value
mood_entry = OptionMenu(frame, options, *mood_options) 
##mood dropdown menu with options 1-10
mood_entry.grid(row=2, column=1)

##label
label_label = tk.Label(frame,text="Enter a label:",font= ('Calibri', 18, ))
label_label.grid(row=3, column=0)

label_entry = tk.Entry(frame, width=10)
label_entry.grid(row=3, column=1)

##journal write
journal_label = tk.Label(frame,text="Write journal\nentry:",font= ('Calibri', 18, ))
journal_label.grid(row=4, column=0)

journal_text = scrolledtext.ScrolledText(frame,width=40,height=28,font= ('Calibri', 11, ))
#use this for entry editor https://www.codegrepper.com/code-examples/python/python+tkinter+entry+prefilled+field
journal_text.grid(row=4, column=1)

##button to trigger command / submit stuff
get_button= button = tk.Button(frame,text="Save Entry",font= ('Calibri', 18, ), command=lambda: [get_title(), get_mood(), title_check()]) ##get from https://www.youtube.com/watch?v=7A_csP9drJw
get_button.grid(row=5, column=1, pady = 6, padx= 5)

def trends():
    import tweepy

    bearer = "AAAAAAAAAAAAAAAAAAAAAAJdaQEAAAAAaQlq6cYO6N%2F6oMX%2F0qJnHw6U99E%3DrHWrBHsUVJLZwzrqPN85dU3i8m8wvquRzIOhs9fFxoU9dPyQj7"

    auth = tweepy.OAuth2BearerHandler(bearer)
    API = tweepy.API(auth)

    trends1 = API.get_place_trends(23424975)

    #from https://stackoverflow.com/questions/21203260/python-get-twitter-trends-in-tweepy-and-parse-json
    # trends1 is a list with only one element in it, which is a dict which we'll put in data
    data = trends1[0] 
    # grab the trends
    trends = data['trends']
    # grab the name from each trend
    names = [trend['name'] for trend in trends]


    twitterlabel = tk.Label(frame, text="Trends", font= ('Calibri', 19, 'bold')) ##from #https://stackoverflow.com/questions/46495160/make-a-label-bold-tkinter
    twitterlabel.grid(row=3, column=2)
    newlinenames= ('\n'.join(names[0:29])) #https://blog.finxter.com/python-list-to-string/#:~:text=What%20is%20this%3F,-Report%20Ad&text=python%20fast'''-,Solution%3A%20to%20convert%20a%20list%20of%20strings%20to%20a%20string,and%20returns%20a%20new%20string.
    trendslinelabel = tk.Label(frame, text=newlinenames)
    trendslinelabel.grid(row=4, column=2, padx=10)

    ##important https://stackoverflow.com/questions/21203260/python-get-twitter-trends-in-tweepy-and-parse-json


trends()
root.mainloop()


