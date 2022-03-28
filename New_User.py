##----Functions need to be above
def newuser():
    ##direct from https://www.makeuseof.com/encrypt-password-in-python-bcrypt/
    import bcrypt

    # Encode the stored password:
    password = str(password_entry.get())

    password = password.encode('utf-8')
    
    # Encrypt the stored password:
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 

    import sqlite3
    ## tutorial from https://likegeeks.com/python-sqlite3-tutorial/#Create_Connection
    con = sqlite3.connect('Journal.db') ##make sure this is actually the right database
    
    def sql_insert(con, entities):
    
        cursorObj = con.cursor()
        
        cursorObj.execute('INSERT INTO Login2(Username, Password) VALUES(?,?)', entities,)
        ##inserts login info into database
        con.commit()
    
    
    entities = (username, hashed,)

    sql_insert(con, entities)


def lengthcheck():
    global username
    username =user_entry.get()

    global password
    password = str(password_entry.get())
    usernamelength = len(username)
    passwordlength = len(password)
    #gets credential input lengths

    if passwordlength>=4 and usernamelength>=4:
        #sets minimum credential length 
        generate_new_user_folders()
        newDB()
        logintable()
        newuser()
        closewindow()
        mainmenu()
    else :
        length_label = tk.Label(frame,text="Credentials too short", font="20")
        length_label.grid(row=3,column=3, pady = 2, padx= 5)
        #prints if too short



import tkinter as tk ##from https://www.youtube.com/watch?v=D8-snVfekto&list=PLsmaE85R7RwyaAqcLC_XQlKuNbEQSy5Nv&index=1&t=3049s


def date():
    from datetime import date
    
    today = date.today() ##from https://www.programiz.com/python-programming/datetime/current-datetime

    global day
    global month
    global year
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    global today_correct
    today_correct=today.strftime("%d.%m.%Y")

    print("The date=", today_correct+"\n\n")
date()

def mainmenu():
    import os
    os.system('python mainmenu.py')
    #opens main menu

def closewindow():
    root.destroy() #closes window

root = tk.Tk()


root.title("Journal Login")
canvas = tk.Canvas(root, height=600, width=600)
canvas.pack()

#creates frame and entry fields
frame= tk.Frame(root,bg= "light blue")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

journal_label = tk.Label(frame,text="Journal", font="20")
journal_label.grid(row=0,column=0, pady = 2, padx= 5)

user_label = tk.Label(frame,text="User", font="15")
user_label.grid(row=1, column=0, pady = 2, padx= 5)

user_entry = tk.Entry(frame)
user_entry.grid(row=1, column=1)

password_label = tk.Label(frame,text="Password \n(4 characters minimum)", font="15")
password_label.grid(row=2, column=0, pady = 2, padx= 5)

password_entry = tk.Entry(frame,show="*",) 
##from https://stackoverflow.com/questions/2416486/how-to-create-a-password-entry-field-using-tkinter
password_entry.grid(row=2, column=1)

def generate_new_user_folders(): ##creates new journal folder for a new user
    import tkinter as tk
    import os.path
    user_profile = os.environ['USERPROFILE'] ##gets windows username, found from stackoverflow
    user_desktop = user_profile + "\Desktop/journal_text" ##makes path from user directory
    print (user_desktop)

    print ("The first folder i will create is "+ user_desktop)

    try:
        os.mkdir(user_desktop) ##makes a new folder
    except OSError:
        print ("Creation of the directory %s failed" % user_desktop) ##error if task fails or if folder exists
        journalfilefail_label = tk.Label(frame,text=("Creation of the directory\n %s failed"% user_desktop))
        journalfilefail_label.grid(row=4,column=1)

    else:
        print ("Successfully created the directory %s " % user_desktop + "\n\n") ##this is console printing not label
        journalfile_success_label = tk.Label(frame,text=("Successfully created your journal folder\n%s " % user_desktop))
        journalfile_success_label.grid(row=4,column=1)
        print("I'll now try to make a date folder in the newly created journal folder")
        save_path_date = user_desktop+"/%s" %today_correct #this one is for the date folder in the journal file
        
        try:
            os.mkdir(save_path_date)
        except OSError:
            print ("Creation of the directory %s failed" % save_path_date)
            datefolder_fail_label = tk.Label(frame,text=("Creation of the directory %s failed" % save_path_date))
            datefolder_fail_label.grid(row=5,column=1)

        else:
            datefolder_success_label = tk.Label(frame,text=("Successfully your date folder at\n %s " % save_path_date))
            datefolder_success_label.grid(row=5,column=1)
            print ("Successfully created the directory %s " % save_path_date)

def newDB():
    import sqlite3
    ##https://likegeeks.com/python-sqlite3-tutorial/#Create_Connection
    from sqlite3 import Error

    def sql_connection():
        try:
            con = sqlite3.connect('Journal.db') ##makes a new database connection
            return con

        except Error:
            print(Error)

    def sql_table(con):

        cursorObj = con.cursor()
        ##creates columns
        cursorObj.execute("CREATE TABLE Entries(ID text PRIMARY KEY, Title text, FilePath text, Day integer, Month integer, Year integer, Hour integer, Minute integer, Mood integer, Label text, WordCount integer)") 
        ##creates table with columns for use in the journal database

        con.commit() ##writes to db

    con = sql_connection()

    sql_table(con) ##calls the create table function with the connection function as an argument

def logintable():
  ## tutorial from https://likegeeks.com/python-sqlite3-tutorial
  
  import sqlite3
  from sqlite3 import Error
  def sql_connection():
      try:
          con = sqlite3.connect('Journal.db') ##makes a new database connection
          return con
      except Error:
          print(Error) ##prints error if necessary
  def sql_table(con):
      cursorObj = con.cursor()
      ##creates columns
      cursorObj.execute("CREATE TABLE Login2(Username text, Password text)") 
      con.commit() ##creates login table in database
  con = sql_connection()
  sql_table(con) ##calls the create table function with the connection function as an argument



new_button = tk.Button(frame,text="Register as new user", command=lambda: [lengthcheck()])
#calls length checker which calls the rest of the functions if conditions are met
new_button.grid(row=3,column=0)

root.mainloop() ##runs tkinter