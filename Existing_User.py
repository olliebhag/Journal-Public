##----Functions need to be above
global attempts
attempts = 0
attempts = int(attempts) 

def attempts():
    global attempts
    attempts = attempts + 1
    if attempts== 5:
        closewindow()
    else:
        existingUser()

def existingUser():

    

    username = str(user_entry.get())
    passwordinput = str(password_entry.get()) 
    import bcrypt
    import sqlite3

    # Encode the inputted password:
    passwordinput = passwordinput.encode('utf-8')

    # Encrypt the stored pasword:
    #hashedinput = bcrypt.hashpw(passwordinput, bcrypt.gensalt(10)) 

    filecon = sqlite3.connect("Journal.db")
    cursorObj = filecon.cursor()

    cursorObj.execute("SELECT Password FROM Login2 WHERE Username = ?", (username,)) ##IMPORTANT COMMA HERE
    gethashdb=cursorObj.fetchall()
    print (gethashdb)
    gethashdb=str(gethashdb)
    
    replacelist1_hash= gethashdb.replace("[(", "")
    replacelist2_hash= replacelist1_hash.replace(",)]", "")

    print("The list stripped hash is "+replacelist2_hash)

    replacelist3_hash=replacelist2_hash.replace("b'", "")
    replacelist4_hash=replacelist3_hash.replace("'", "")

    hasheddb= replacelist4_hash
    hasheddb= hasheddb.encode('utf-8')
    
    print ("The stripped hash is "+str(hasheddb))

    # Use conditions to compare the authenticating password with the stored one:
    if bcrypt.checkpw(passwordinput, hasheddb):
        print("login success")
        existingzip()
        generate_existing_user_date()
        
        closewindow()
        mainmenu()
        
    else:
        wrongpass_label = tk.Label(frame,text= "Incorrect login")
        wrongpass_label.grid(row=6, column=1)

def existingzip():
    import os.path
    user_profile = os.environ['USERPROFILE']

    password= str(password_entry.get()) 

    import py7zr
    with py7zr.SevenZipFile(user_profile+"/Desktop/journalzip.7z", 'r', password=password) as archive:
        archive.extractall(path=user_profile+"/Desktop/")



import tkinter as tk ##from https://www.youtube.com/watch?v=D8-snVfekto&list=PLsmaE85R7RwyaAqcLC_XQlKuNbEQSy5Nv&index=1&t=3049s
import random


def date():
    from datetime import date
    
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

    print("The date=", today_correct+"\n\n")
date()

def mainmenu():
    import os
    os.system('python mainmenu.py')

def closewindow():
    root.destroy() #closes window

root = tk.Tk()

root.title("Journal Login")
canvas = tk.Canvas(root, height=600, width=600)
canvas.pack()

frame= tk.Frame(root,bg= "light blue")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

journal_label = tk.Label(frame,text="Journal", font="20")
journal_label.grid(row=0,column=0, pady = 2, padx= 5)

user_label = tk.Label(frame,text="User", font="15")
user_label.grid(row=1, column=0, pady = 2, padx= 5)

user_entry = tk.Entry(frame)
user_entry.grid(row=1, column=1)


password_label = tk.Label(frame,text="Password", font="15")
password_label.grid(row=2, column=0, pady = 2, padx= 5)

password_entry = tk.Entry(frame,show="*",) 
##from https://stackoverflow.com/questions/2416486/how-to-create-a-password-entry-field-using-tkinter
password_entry.grid(row=2, column=1)



def generate_existing_user_date():
    import os.path
    user_profile = os.environ['USERPROFILE'] ##gets username from windows
    user_current_date = user_profile + "\Desktop/journal_text/"+today_correct ##makes a path to current date folder
    print ("The file path is "+user_current_date)

    if os.path.isdir(user_current_date): ##this means if its true then continue
        print ("The folder for todays date already exists")
        dateexists_label = tk.Label(frame,text= "The folder for todays date already exists")
        dateexists_label.grid(row=4, column=1)
        

    else:
        print ("The folder for todays date doesnt exist. Lets create one.") ##if date folder for today doesnt exist
        
        
        try:
            os.mkdir(user_current_date) ##makes current date_folder
        except OSError:
            print ("Creation of the directory %s failed" % user_current_date) ##in case of error, unrelated to if folder exists
            datefail_label = tk.Button(frame,text= "Creation of the directory %s failed" % user_current_date)
            datefail_label.grid(row=5, column=1)
        print ("The folder for todays date has been created")
        datesuccess_label = tk.Label(frame,text= "The folder for todays date has been created")
        datesuccess_label.grid(row=5, column=1)

existing_button = tk.Button(frame,text="Log in as existing user", command=lambda: [attempts()])
existing_button.grid(row=3,column=1)

#enter_button = tk.Button(frame,text= "Enter program (fake)")
#enter_button.grid(row=5, column=2) 
root.mainloop() ##runs tkinter

