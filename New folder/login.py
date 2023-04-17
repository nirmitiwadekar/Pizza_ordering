from tkinter import *
from tkinter import messagebox
import os

login_window=Tk()
login_window.title('Login')
login_window.geometry('600x650+100+20')
login_window.resizable(False,False)


bg=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\loginbg.png")

my_label=Label (login_window,image=bg)

my_label.place(x=0,y=0,relwidth=1,relheight=1)



def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(login_window)
        screen.title("App")
        screen.geometry('1545x785+0+0')
        screen.config(bg='white')

        Label(screen,text='Welcome',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        
        screen.mainloop()
    
    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid!!","Invalid username and password.")
    
    elif password!='1234':
        messagebox.showerror("Invalid!!","Invalid Password")

    elif username!='admin':
        messagebox.showerror("Invalid!!","Invalid Username")



loginframe=Frame(login_window,width=500,height=500)
loginframe.place(x=130,y=20)

heading=Label(loginframe,text='SIGN IN',fg='red',font=('microsoft YaHei UI Light',24,'bold'))
heading.place(x=100,y=0)

#----------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(loginframe,width=25,fg='black',border=1,bg='white',font=('microsoft YaHei UI Light',11))
user.place(x=30,y=70)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(loginframe,width=295,height=5,bg='black').place(x=25,y=100)

#-----------------------------------------------------------------------

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(loginframe,width=25,fg='black',border=1,bg='white',font=('microsoft YaHei UI Light',11))
code.place(x=30,y=130)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(loginframe,width=295,height=5,bg='black').place(x=25,y=160)

#-----------------------------------------------------------------------
Button(loginframe,width=35,pady=5,text='Login',bg='deepSkyblue',fg='white',font=('calibri',12,'bold'),border=0,command=signin).place(x=25,y=200)

label=Label(loginframe,text='Dont Have an Account??',fg='black',bg='white',font=('microsoft YaHei UI Light',11,'italic'))
label.place(x=80,y=285)

sign_up=Button(loginframe,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='navy')
sign_up.place(x=245,y=285)

fplabel=Label(loginframe,text='Forgot Password?',fg='black',bg='white',font=('microsoft YaHei UI Light',11,'italic'))
fplabel.place(x=175,y=248)
#------------------------------------------------------------------

orLabel=Label(loginframe,text='-----------------OR-------------------',font=('Open Sans',12),fg='black',bg='white')
orLabel.place(x=70,y=315)

socialmedia_logo=PhotoImage(file='socialmediaicons.png')
smLabel=Label(loginframe,image=socialmedia_logo,bg='white')
smLabel.place(x=15,y=360)




login_window.mainloop()