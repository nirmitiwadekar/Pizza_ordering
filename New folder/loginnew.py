from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import psycopg2
import psycopg2.extras

def signup_page():
    login_window.destroy()
    import signupnew

def home_page():
    login_window.destroy()
    import homepg

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


hostname = 'localhost'
database = 'project'
username = 'postgres'
pwd = '250201'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                    id      int PRIMARY KEY,
                                    name    varchar(40) NOT NULL,
                                    salary  int,
                                    dept_id varchar(30)) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D2')]
            for record in insert_values:
                cur.execute(insert_script, record)

            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            #delete_script = 'DELETE FROM employee WHERE name = %s'
            #delete_record = ('James',)
            #cur.execute(delete_script, delete_record)

            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'], record['salary'])
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


#GUI Part
login_window=Tk()
login_window.geometry('925x700+300+55')
login_window.title('Login')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\loginbg.png")
login_window.resizable(False,False)

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH,expand=1)


heading=Label(login_window,text='The Crispy Crust Pizzeria',fg='maroon',font=('Georgia',26),bg='white',bd=7)
heading.place(x=20,y=20)

heading=Label(login_window,text='USER LOGIN',fg='black',font=('Georgia',20),bg='white',bd=5)
heading.place(x=100,y=120)

#------------Username-------------
usernameEntry=Entry(login_window,width=25,fg='black',border=2,bg='mistyrose',font=('arial',14),bd=0)
usernameEntry.place(x=80,y=178)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=290,height=4,bg='coral')
frame1.place(x=80,y=200)

#-----------password--------------
passwordEntry=Entry(login_window,width=25,fg='black',border=2,bg='mistyrose',font=('arial',14),bd=0)
passwordEntry.place(x=80,y=240)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=290,height=4,bg='coral')
frame2.place(x=80,y=264)

#-------------Forgot Password---------
forgotButton=Button(login_window,text='Forgot Password??',bd=0,fg='black',bg='bisque',font=('microsoft YaHei UI Light',11,'bold'),cursor='hand2',activeforeground='darkorange',activebackground='deeppink')
forgotButton.place(x=215,y=280)

#-------------Login Button-------------
loginButton=Button(login_window,width=18,pady=5,bd=2,text='Login',bg='orangered',fg='white',font=('Georgia',16,'bold'),border=0,activeforeground='white',activebackground='orange',cursor='hand2')
loginButton.place(x=90,y=330)

#--------------------OR----------------
orLabel=Label(login_window,text='------------------------OR----------------------',font=('Georgia',11),fg='black',bg='sandybrown')
orLabel.place(x=50,y=400)

signupLabel=Label(login_window,text='Dont have an account?',font=('Georgia',12,'bold'),fg='black',bg='bisque')
signupLabel.place(x=20,y=450)

newaccountButton=Button(login_window,bd=2,text='create new account',bg='pink',fg='black',font=('Georgia',9,'bold','underline'),
                        border=0,activeforeground='white',activebackground='yellow',cursor='hand2',command=signup_page)
newaccountButton.place(x=220,y=445)
#---------------Social Media--------------
joinusLabel=Label(login_window,text='Join is on..',font=('Georgia',12,'bold'),fg='black',bg='tomato')
joinusLabel.place(x=20,y=570)

facebook_logo=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\socialmediaicons.png")
fbLabel=Label(login_window,image=facebook_logo)
fbLabel.place(x=25,y=600)

backButton=Button(login_window,text= "Back",cursor="hand2", bd=2,font=("comic sans",13, 'bold'),
                   activebackground='orange',bg="bisque",fg="black",command=home_page)
backButton.place(x=20,y=500)

login_window.mainloop()