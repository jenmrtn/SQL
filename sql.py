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

        self.login_button = t.Button(self.frame2,text='Login', command= self.access_database())

        self.login_button.pack()

    def access_database(self):
        print('helllo')

        t.mainloop()
        login = self.email_entry.get()
        password= self.password_entry.get()

        self.main_window.destroy()

        login = 'Jenna_martin1'
        password=''

        prelist= {}
        courselist= []
        cn_str =(
        'Driver=(SQL Server);' # Data source driver,
        'Server=MIS-SQLJB;'    # Server name
        'Database=School;'      #Database name
        'UID='+login+';'        #User name
        'PWD'+password+';'      #User password
            )


        cn= pyodbc.connect(cn_str)

        cursor = cn.cursor()

        cursor.execute('select * from School.dbo.Course')

        data = cursor.fetchall()
        print(data)
        inputcourseid=int(input("What is the course ID"))
        for row in data:
            courseID=row[0]
            title= row[1]
            credit=row[2]
            deptID=row[3]
            prelist = {'CourseID':courseID,'Title': title, 'Credit':credit, 'DeptID':deptID}
            courselist.append(prelist)
        for i in courselist
        if inputcourseid== i[0]:
            print(f'Title:{i["Title"]}')
            print(f'Credits:{i["Credit"]}')
            print(f'Department:{i["DeptID"]}')
myinstance=myGUI()