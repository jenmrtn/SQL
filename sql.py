import tkinter as t
import pyodbc
class myGUI:
    
    def __init__(self):
        self.main_window = t.Tk()
        self.main_window.geometry('375x400')
        
        self.main_window.title('SQL Server Login')


        self.frame=t.Frame(self.main_window)
        self.frame1 = t.Frame(self.main_window )
        self.frame2 = t.Frame(self.main_window)
        self.frame.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.prompt_email= t.Label(self.frame, text = 'Login:')
        self.email_entry = t.Entry(self.frame, width=34)

        self.prompt_password= t.Label(self.frame1, text = 'Password:')
        self.password_entry = t.Entry(self.frame1, width=32, show="*")


        self.prompt_email.pack(side='left')
        self.email_entry.pack(side='left')

        self.prompt_password.pack(side='left')
        self.password_entry.pack(side='left')

        self.login_button = t.Button(self.frame2,text='Login')

        self.login_button.pack()

    def access_database(self):
        print('helllo')

        t.mainloop()

myinstance=myGUI()