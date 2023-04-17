from  tkinter import*
from PIL import ImageTk
from tkinter import messagebox


#-----------Home Page-----------
def login_page():
    home_window.destroy()
    import loginnew

def signup_page():
    home_window.destroy()
    import signupnew

def about_us_page():
    home_window.destroy()
    import aboutus

home_window=Tk()
home_window.geometry('950x650+300+55')
home_window.title('Home Window')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\homepg.png")
home_window.resizable(False,False)

bgLabel=Label(home_window,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH,expand=1)

heading=Label(home_window,text='Delicious',fg='white',font=('georgia',18),bg="black")
heading.place(x=305,y=280)

heading=Label(home_window,text='The Crispy Crust Pizzeria',fg='black',font=('georgia',27),bg="whitesmoke")
heading.place(x=5,y=315)

sloganLabel=Label(home_window,text='Top Your Crust With Kindness And Trust..!',fg='navajowhite',bg='black',font=('comic sans sm',14,'bold'))
sloganLabel.place(x=10,y=365)

clickButton=Button(home_window,text= "About Us",cursor="hand2", bd=2,font=("comic sans",12),
                   activebackground='orange',bg="blanchedalmond",fg="black",command=about_us_page)
clickButton.place(x=5,y=10)


clickButton=Button(home_window,text= "Login",cursor="hand2", bd=2,font=("comic sans",18, 'bold'),
                   activebackground='orange',bg="black",fg="white",command=login_page)
clickButton.place(x=45,y=550)

clickButton=Button(home_window,text= "SignUp",cursor="hand2", bd=2,font=("comic sans",18, 'bold'),
                   activebackground='orange',command=signup_page)
clickButton.place(x=145,y=550)

home_window.mainloop()

#----------Login--------------

from  tkinter import*
from tkinter import messagebox
from PIL import ImageTk

def signup_page():
    login_window.destroy()
    import signupnew



def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUI Part
login_window=Tk()
login_window.geometry('925x700+300+55')
login_window.title('Login')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\loginbg.png")
login_window.resizable(False,False)

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH,expand=1)

heading=Label(login_window,text='The Crispy Crust Pizzeria',fg='black',font=('Georgia',26),bg='white')
heading.place(x=20,y=20)

heading=Label(login_window,text='USER LOGIN',fg='white',font=('Georgia',22),bg='darkred')
heading.place(x=100,y=120)

#------------Username-------------
usernameEntry=Entry(login_window,width=25,fg='black',border=1,bg='bisque',font=('arial',14),bd=0)
usernameEntry.place(x=80,y=178)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window,width=290,height=4,bg='orange')
frame1.place(x=80,y=200)

#-----------password--------------
passwordEntry=Entry(login_window,width=25,fg='black',border=1,bg='bisque',font=('arial',14),bd=0)
passwordEntry.place(x=80,y=240)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=290,height=4,bg='orange')
frame2.place(x=80,y=264)

#-------------Forgot Password---------
forgotButton=Button(login_window,text='Forgot Password??',bd=0,fg='black',bg='palegoldenrod',font=('microsoft YaHei UI Light',11,'bold'),cursor='hand2',activeforeground='darkorange',activebackground='deeppink')
forgotButton.place(x=215,y=280)

#-------------Login Button-------------
loginButton=Button(login_window,width=18,pady=5,bd=2,text='Login',bg='maroon',fg='white',font=('Georgia',16,'bold'),border=0,activeforeground='white',activebackground='orange',cursor='hand2')
loginButton.place(x=90,y=330)

#--------------------OR----------------
orLabel=Label(login_window,text='------------------------OR----------------------',font=('Georgia',11),fg='black',bg='sandybrown')
orLabel.place(x=50,y=400)

signupLabel=Label(login_window,text='Dont have an account?',font=('Georgia',12,'bold'),fg='black',bg='palegoldenrod')
signupLabel.place(x=20,y=450)

newaccountButton=Button(login_window,bd=2,text='create new account',bg='olivedrab',fg='black',font=('Georgia',9,'bold','underline'),
                        border=0,activeforeground='white',activebackground='yellow',cursor='hand2',command=signup_page)
newaccountButton.place(x=220,y=445)
#---------------Social Media--------------
joinusLabel=Label(login_window,text='Join is on..',font=('Georgia',12,'bold'),fg='black',bg='tomato')
joinusLabel.place(x=20,y=570)

facebook_logo=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\socialmediaicons.png")
fbLabel=Label(login_window,image=facebook_logo)
fbLabel.place(x=25,y=600)



login_window.mainloop()

#------------Signup---------------

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import ast

def connect_database():
    if pnameEntry.get()=='' or phoneEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Rquired')
    
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch!!!')
    
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions.')
    
    #else:
        
#in else we have to connect database ... by importing  


def login_page():
    signup_window.destroy()
    import loginnew

    
signup_window=Tk()
signup_window.title('SignUp')
signup_window.geometry('950x650+300+55')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\pizzasignup.png")
signup_window.resizable(False,False)

bgLabel=Label(signup_window,image=bgImage)
bgLabel.grid()
bgLabel.pack(fill=BOTH,expand=1)

signupframe=Frame(signup_window,width=450,height=550,bg='wheat',border=5)
signupframe.place(x=530,y=20)

heading=Label(signupframe,text='Create An Account',fg='white',bg='tomato',font=('georgia',24,'bold'))
heading.grid(row=0,column=0,padx=10,pady=10)

#Name
pnameLabel=Label(signupframe,text='Customer Name',fg='black',bg='wheat',font=('georgia',11,'bold'))
pnameLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,2))

pnameEntry=Entry(signupframe,width=25,font=('arial',14),fg='black',bg='bisque')
pnameEntry.grid(row=2,column=0,sticky='w',padx=25)

#phone Number
phoneLabel=Label(signupframe,text='Phone Number',fg='black',bg='wheat',font=('georgia',11,'bold'))
phoneLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,2))

phoneEntry=Entry(signupframe,width=25,font=('arial',14),fg='black',bg='bisque')
phoneEntry.grid(row=4,column=0,sticky='w',padx=25)

#Username
usernameLabel=Label(signupframe,text='Username',fg='black',bg='wheat',font=('georgia',11,'bold'))
usernameLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,2))

usernameEntry=Entry(signupframe,width=25,font=('arial',14),fg='black',bg='bisque')
usernameEntry.grid(row=6,column=0,sticky='w',padx=25)

#Password
passwordLabel=Label(signupframe,text='Password',fg='black',bg='wheat',font=('georgia',11,'bold'))
passwordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,2))

passwordEntry=Entry(signupframe,width=25,font=('arial',14),fg='black',bg='bisque')
passwordEntry.grid(row=8,column=0,sticky='w',padx=25)

#Confirm Password
confirmLabel=Label(signupframe,text='Confirm Password',fg='black',bg='wheat',font=('georgia',11,'bold'))
confirmLabel.grid(row=9,column=0,sticky='w',padx=25,pady=(10,2))

confirmEntry=Entry(signupframe,width=25,font=('arial',14),fg='black',bg='bisque')
confirmEntry.grid(row=10,column=0,sticky='w',padx=25)


#Check button
check=IntVar()
termsandconditions=Checkbutton(signupframe,text='I agree to the Terms and Conditions',font=('georgia',11,'bold'),fg='black',bg='wheat',
                               activebackground='wheat',activeforeground='black',cursor='hand2',variable=check)
termsandconditions.grid(row=11,column=0,pady=15,padx=20)

#Sign Up Button

signupButton=Button(signupframe,width=30,text='Sign Up',border=5,bg='tomato',cursor='hand2',fg='white',
                    font=('open sans',12,'bold'),activebackground='wheat',activeforeground='white',command=connect_database)
signupButton.grid(row=12,column=0,sticky='w',padx=25,pady=15)


#already account 

alreadyaccountLabel=Label(signupframe,text='Have an account..?',fg='black',bg='wheat',font=('georgia',12,'bold'))
alreadyaccountLabel.grid(row=13,column=0,sticky='w',padx=25,pady=(10,2))

loginButton=Button(signupframe,text='Login',bd=0,bg='wheat',cursor='hand2',fg='navy',
                    font=('open sans',11,'bold','underline'),activebackground='wheat',activeforeground='navy',command=login_page)
loginButton.place(x=190,y=510)


signup_window.mainloop()