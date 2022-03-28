##----------------------Existing entry stuff


from cProfile import label
from tkinter import ttk ## from https://www.activestate.com/resources/quick-reads/how-to-display-data-in-a-table-using-tkinter/

from tkinter.ttk import Treeview, Scrollbar 

import tkinter as tk

import sqlite3


def View():

    con1 = sqlite3.connect("Journal.db")

    cur1 = con1.cursor() ##uses sql cursor

    cur1.execute("SELECT * FROM Entries")

    rows = cur1.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row) ##inserts values into treeview

    con1.close() ##closes connection


def existing_entry():
    import tkinter as tk ##from https://www.youtube.com/watch?v=D8-snVfekto&list=PLsmaE85R7RwyaAqcLC_XQlKuNbEQSy5Nv&index=1&t=3049s
    from tkinter import scrolledtext


    #First functions
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


    def write_journal():
       
       file1 = open(nice_filepath, "w")
       userWrite=str(journal_text.get("1.0","end"))

       file1.write(userWrite)
       file1.close()

       fileCount = open(nice_filepath, "rt")
       data = fileCount.read()
       words = data.split()

       global wordCount
       wordCount = len(words)
       print("The word count is: "+str(wordCount))   
       fileCount.close()

       #newEntry()

    def updateEntry():

       import sqlite3
       ## tutorial from https://likegeeks.com/python-sqlite3-tutorial/#Create_Connection
       con = sqlite3.connect('Journal.db') ##make sure this is actually the right database
       
       
       def sql_update(con):
           cursorObj = con.cursor()
           sqldata= str(wordCount), primary_key
           ##from https://www.plus2net.com/python/sqlite-update.php
           query =  "UPDATE Entries set WordCount=? where ID =? "
           cursorObj.execute(query, sqldata)
           con.commit()
       
       ##filepath
       import os
       
       
       #entities = (wordCount, primary_key)
       
       sql_update(con)

    root2 = tk.Tk()

    root2.title("Edit an entry")
    canvas = tk.Canvas(root2, height=900, width=900)
    canvas.pack()

    existframe= tk.Frame(root2,bg= "#34568B")
    existframe.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    ##design
    journal_label = tk.Label(existframe,text="Journal", font= ('Helvetica', 20, "bold"))
    journal_label.grid(row=0,column=0, pady = 2, padx= 5)

    ##title
    title_label = tk.Label(existframe,text="Title (Don't use similar titles\n on the same day):",font= ('Helvetica', 11, ))
    title_label.grid(row=1,column=0)

    title_existing_label = tk.Label(existframe, width=40, text= title)
    title_existing_label.grid(row=1, column=1)

    ##mood
    mood_label = tk.Label(existframe,text="Mood (1-10):",font= ('Helvetica', 18, ))
    mood_label.grid(row=2, column=0)

    mood_existing_label = tk.Label(existframe, width=5, text= mood)
    mood_existing_label.grid(row=2, column=1)

    ##label
    label_label = tk.Label(existframe,text="Label:",font= ('Helvetica', 18, ))
    label_label.grid(row=3, column=0)

    label_existing_label = tk.Label(existframe, width=40, text= label)
    label_existing_label.grid(row=3, column=1)

    ##journal write
    journal_label = tk.Label(existframe,text="Write journal\nentry:",font= ('Helvetica', 18, ))
    journal_label.grid(row=4, column=0)


    ##testing reading from textfile
    #example_file= "C:/Users/Ollie/Desktop/journal_text/11.02.2022/no3.txt"
    #with open(example_file) as f:
    #    lines = f.readlines()
    #    print (str(lines))
    #    str_lines= (str(lines))
    ##messed about for too long using readlines instead of just read

    print ("the old filepath is "+filepath)
    replaceslash_filepath= filepath.replace("\\\\", "/") ##from https://www.geeksforgeeks.org/python-string-replace/
    
    replacelist1_filepath= replaceslash_filepath.replace("[('", "")
    
    replacelist2_filepath= replacelist1_filepath.replace("',)]", "")

    nice_filepath= str(replacelist2_filepath)

    print ("\n\n\n\nThe updated nice filepath is this: \n"+nice_filepath)    

    with open(nice_filepath) as f: ##from https://www.pythontutorial.net/python-basics/python-read-text-file/
        contents = f.read()
        print(contents)


    journal_text = scrolledtext.ScrolledText(existframe,width=40,height=30)
    journal_text.insert("end", (contents)) #----- use this for entry editor https://www.codegrepper.com/code-examples/python/python+tkinter+entry+prefilled+field
    journal_text.grid(row=4, column=1)

    ##button to trigger command / submit stuff
    get_button= button = tk.Button(existframe,text="Save entry", font= ('Helvetica', 18, ),command=lambda: [write_journal(), updateEntry()]) ##get from https://www.youtube.com/watch?v=7A_csP9drJw
    get_button.grid(row=2, column=2)



    root2.mainloop()

    ##insert command is up there^
    ##sql get filepath where primary key is "input"
    ##pass filepath into function to read text from txt file
    ##use insert to pass into text box
    ## test writing over it i think it already does
    ##submit button should redo the mood and wordcount and write over db entry



















##----------------Treeview--------------------------------------------------

root = tk.Tk()
root.title("Previous entries")

canvas = tk.Canvas(root, height=700, width=1400)
canvas.pack()

##Frame
tree_frame= tk.Frame(root,bg= "#34568B")
tree_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

##Scrollbar
tree_scroll = Scrollbar(tree_frame)
#tree_scroll.pack()
tree_scroll.grid(row=0,column=1) ##places scrollbar for the treeview

##Treeview
tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, 
column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show='headings')
##sets number of columns to display


tree_scroll.config(command=tree.yview)
##attaches scrollbar to change y coordinate of treeview

tree.column("#1", anchor=tk.CENTER, width=100) ##positions first column
tree.heading("#1", text="ID") ##puts a text heading above data

tree.column("#2", anchor=tk.CENTER, width=150)
tree.heading("#2", text="Title")

tree.column("#3", anchor=tk.CENTER, width=0)
tree.heading("#3", )

tree.column("#4", anchor=tk.CENTER,width=60)
tree.heading("#4", text="Day")

tree.column("#5", anchor=tk.CENTER,width=60)
tree.heading("#5", text="Month")

tree.column("#6", anchor=tk.CENTER,width=60)
tree.heading("#6", text="Year")

tree.column("#7", anchor=tk.CENTER,width=60)
tree.heading("#7", text="Mood")

tree.column("#8", anchor=tk.CENTER,width=80)
tree.heading("#8", text="Label")

tree.column("#9", anchor=tk.CENTER,width=90)
tree.heading("#9", text="WordCount")

tree.grid(row=0, column=0)

display_button = tk.Button(tree_frame, text="Display data", command=View)

display_button.grid(row=2, column=0, pady=10)

key_label = tk.Label(tree_frame, text="Enter ID for entry\nto edit:")

key_label.grid(row=3, column=0)

key_entry=tk.Entry(tree_frame)

key_entry.grid(row=4, column=0)

edit_button = tk.Button(tree_frame, text="Edit",)

edit_button.grid(row=5)



def getfilepath():
    import sqlite3

    primary_key = key_entry.get()
    print (primary_key)

    key_label2 = tk.Label(tree_frame, text=(primary_key))
    key_label2.grid(row=5, column=2)

    filecon = sqlite3.connect("Journal.db")
    cursorObj = filecon.cursor()

    cursorObj.execute("SELECT FilePath FROM Entries WHERE ID = ?", (primary_key,)) ##IMPORTANT COMMA HERE
    ##didnt like "" for fields so change to ''
    ##also didnt like using variables as "search term"
    ## this meant i used the WHERE" + variable method
    ## this randomly only worked with the number ones not the string ones
    ##so i used this from here https://www.kite.com/python/answers/how-to-bind-variables-to-a-sql-query-in-sqlite3-in-python
    ##it STILL DOESNT WORK WHY
    ##this helped how mental is that its literally a comma https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
    ##struggling to call function for select db because input hasnt globalled yet
    #and cant call at end of function because it doesnt like it

    files=cursorObj.fetchall()
    #print (files)

    global filepath
    filepath=str(files)


    #nice_filepath= str(replacelist2_filepath)

    #print ("\n\n\n\nThe updated filepath is this: \n"+nice_filepath) 


    filecon.close()


    ##gets primary key and prints it for now

def gettitle():
    import sqlite3

    primary_key = key_entry.get()
    print (primary_key)


    titlecon = sqlite3.connect("Journal.db")
    cursorObj = titlecon.cursor()

    cursorObj.execute("SELECT Title FROM Entries WHERE ID = ?", (primary_key,)) ##IMPORTANT COMMA HERE

    badtitle=cursorObj.fetchall()

    global title
    badtitlestring=str(badtitle)

    print ("the old title is "+badtitlestring)
    
    replacelist1_title= badtitlestring.replace("[('", "")
    
    replacelist2_title= replacelist1_title.replace("',)]", "")

    title= str(replacelist2_title)

    print ("what a cool title: "+title)



    titlecon.close()


def getlabel():
    import sqlite3

    primary_key = key_entry.get()
    print (primary_key)


    con = sqlite3.connect("Journal.db")
    cursorObj = con.cursor()

    cursorObj.execute("SELECT Label FROM Entries WHERE ID = ?", (primary_key,)) ##IMPORTANT COMMA HERE

    badlabel=cursorObj.fetchall()

    global label
    badlabelstring=str(badlabel)

    print ("the old label is "+badlabelstring)
    
    replacelist1_label= badlabelstring.replace("[('", "")
    
    replacelist2_label= replacelist1_label.replace("',)]", "")

    label= str(replacelist2_label)

    print ("what a cool label: "+label)



    con.close()

def getmood():
    import sqlite3

    global primary_key
    primary_key = key_entry.get()
    print (primary_key)

    con = sqlite3.connect("Journal.db")
    cursorObj = con.cursor()

    cursorObj.execute("SELECT Mood FROM Entries WHERE ID = ?", (primary_key,)) ##IMPORTANT COMMA HERE

    badmood=cursorObj.fetchall()

    global mood
    badmoodstring=str(badmood)

    print ("the old mood is "+badmoodstring)
    
    replacelist1_mood= badmoodstring.replace("[(", "")
    
    replacelist2_mood= replacelist1_mood.replace(",)]", "")

    mood= str(replacelist2_mood)

    print ("new mood: "+mood)



    con.close()


def closewindow():
    root.destroy()
##from https://www.geeksforgeeks.org/how-to-close-a-window-in-tkinter/

close_button = tk.Button(tree_frame, text= "close", command= lambda:[closewindow()])
close_button.grid(row=6, column=6)

edit_button = tk.Button(tree_frame, text="Edit",command=lambda: [getfilepath(), gettitle(), getlabel(), getmood(), closewindow(),existing_entry(), ])

edit_button.grid(row=5)

root.mainloop()

#do the existing entry editor next

##then make main menu where everything links

##switching tkinter frames

##learn how to pass into functions

##ollie

