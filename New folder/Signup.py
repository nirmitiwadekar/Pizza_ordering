from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

import ast

signup_window=Tk()
signup_window.title('SignUp')
signup_window.geometry('950x650+300+75')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\pizzasignup3.png")
signup_window.resizable(False,False)

bgLabel=Label(signup_window,image=bgImage)
bgLabel.grid()

def signup():
    Your_name=pname.get()
    Mobile_Number=phone.get()
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()

    if password==confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('Signup','Sucessfully Signed Up')
        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close
    else:
        messagebox.showerror('Invalid',"Both Password should match") 

            


signupframe=Frame(signup_window,width=450,height=550,bg='wheat',border=5)
signupframe.place(x=530,y=20)

heading=Label(signupframe,text='Create An Account',fg='white',bg='deeppink',font=('georgia',24,'bold'))
heading.grid(row=0,column=0,padx=10,pady=10)

#---------------------------------------------------------------------------------

#accept name
def on_enter(e):
    pname.delete(0,'end')

def on_leave(e):
    name=pname.get()
    if pname.get()=='':
        pname.insert(0,'Your Name')

pnameLabel=Label(signupframe,width=25,fg='black',border=0,bg='bisque',font=('microsoft YaHei UI Light',11))
pnameLabel.grid(row=1,column=0,sticky='w',padx=25)
#username 
pnameEntry=Entry(signupframe,width=25,font=('arial',14))
pnameEntry.grid(row=1,column=0,sticky='w',padx=25,fg='black',bg='bisque')
pname.insert(0,'Customer Name')
pname.bind('<FocusIn>',on_enter)
pname.bind('<FocusOut>',on_leave)

Frame(signupframe,width=295,height=5,bg='black').place(x=25,y=110)

#---------------------------------------------------------------------------------

#accept Phone Number
def on_enter(e):
    phone.delete(0,'end')

def on_leave(e):
    name=phone.get()
    if phone.get()=='':
        phone.insert(0,'Mobile_Number')
#phone number 
phone=Entry(signupframe,width=25,fg='black',border=0,bg='bisque',font=('microsoft YaHei UI Light',11))
phone.place(x=30,y=130)
phone.insert(0,'Mobile_Number')
phone.bind('<FocusIn>',on_enter)
phone.bind('<FocusOut>',on_leave)

Frame(signupframe,width=295,height=5,bg='black').place(x=25,y=160)
#---------------------------------------------------------------------------------

#set username
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if user.get()=='':
        user.insert(0,'Username')
#username 
user=Entry(signupframe,width=25,fg='black',border=0,bg='bisque',font=('microsoft YaHei UI Light',11))
user.place(x=30,y=180)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(signupframe,width=295,height=5,bg='black').place(x=25,y=210)


#-------------------------------------------------------------------


#set Password
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if user.get()=='':
        code.insert(0,'Password')
#password
code=Entry(signupframe,width=25,fg='black',border=0,bg='bisque',font=('microsoft YaHei UI Light',11))
code.place(x=30,y=230)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(signupframe,width=295,height=5,bg='black').place(x=25,y=260)

#-------------------------------------------------------------------

#confirm password
def on_enter(e):
    confirm_code.delete(0,'end')

def on_leave(e):
    name=confirm_code.get()
    if confirm_code.get()=='':
        confirm_code.insert(0,'Confirm Password')
#password var        
confirm_code=Entry(signupframe,width=25,fg='black',border=0,bg='bisque',font=('microsoft YaHei UI Light',11))
confirm_code.place(x=30,y=280)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind('<FocusIn>',on_enter)
confirm_code.bind('<FocusOut>',on_leave)

Frame(signupframe,width=295,height=5,bg='black').place(x=25,y=310)

#------------------------------------------------------------
Button(signupframe,width=40,pady=5,text='Sign Up',bg='#57a1f8',fg='white',font=('calibri',12,'bold'),border=0,command=signup).place(x=10,y=350)

label=Label(signupframe,text='I Have an Account',fg='black',bg='peachpuff',font=('microsoft YaHei UI Light',10))
label.place(x=80,y=390)

sign_in=Button(signupframe,width=6,text='LogIn',border=0,bg='peachpuff',cursor='hand2',fg='navy')
sign_in.place(x=200,y=390)

#-------------------------------------------------------------





signup_window.mainloop()