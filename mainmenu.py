
import tkinter as tk
import os

root = tk.Tk()


root.title("Main Menu")
canvas = tk.Canvas(root, height=800, width=800)
canvas.pack()

frame= tk.Frame(root,bg= "light blue")
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7) ##rel=relative to screen size

#frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1) #from https://www.tutorialspoint.com/how-to-horizontally-center-a-widget-using-a-grid-in-tkinter

journal_label = tk.Label(frame,text="Journal",pady=20,font= ('Helvetica', 40, "bold"))
journal_label.grid(row=0, column=0,)

question = tk.Label(frame, font= ('Helvetica', 20, ),pady=20,text= "What would you like to do?")
question.grid(row=1, column=0)

def newrun():
    os.system('python New_Entry.py')

def closewindow():
    root.destroy()

newbutton = tk.Button(frame, pady=20,text="Create New Entry",font= ('Helvetica', 20, ), command=lambda: [closewindow(), newrun(), ])
newbutton.grid(row=2, column=0)

def existrun():
    os.system('python Existing_Entry.py')

existingbutton = tk.Button(frame, pady=20,text="Edit Existing Entry", font= ('Helvetica', 20, ),command=lambda: [closewindow(), existrun(), ])
existingbutton.grid(row=3, column=0)

def getpassword():
    global password
    password= password.get()

def logoutzip():
    import os.path
    user_profile = os.environ['USERPROFILE']
    user_desktop = user_profile + "/Desktop/journal_text"

    
    

    #writes archive of journal text folder
    import py7zr #https://py7zr.readthedocs.io/en/latest/user_guide.html?highlight=password#
    with py7zr.SevenZipFile(user_profile+"/Desktop/journalzip.7z", 'w', password=password) as archive:
        archive.writeall(user_profile+"/Desktop/journal_text", arcname="journal_text")
    print("Archived to desktop\nNow attempting to delete unencrypted folders ")

    

    #deletes unencrypted folder
    #from https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/
    import shutil
    import os
    
    # location
    location = user_profile+"/Desktop/journal_text"
    
    # removing directory
    shutil.rmtree(location)
    print ("Journal text folder deleted")



exitbutton = tk.Button(frame, pady=20,text="Log Out\n(Type password first)",font= ('Helvetica', 20, ), command=lambda: [getpassword(),logoutzip(),closewindow(),])
#exitbutton = tk.Button(frame, pady=20,text="Log Out\nType password first", command=logoutzip())

exitbutton.grid(row=4, column=0)

password = tk.Entry(frame,)
password.grid(row=5, column=0, padx=10,pady=10,ipady=30)

root.mainloop()