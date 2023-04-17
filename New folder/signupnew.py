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

#Back Button
backButton=Button(signup_window,text= "Back",cursor="hand2", bd=2,font=("comic sans",13, 'bold'),
                   activebackground='orange',bg="bisque",fg="black",command=login_page)
backButton.place(x=820,y=530)

signup_window.mainloop()