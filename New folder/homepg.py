from  tkinter import*
from PIL import ImageTk

def login_page():
    home_window.destroy()
    import loginnew

def signup_page():
    home_window.destroy()
    import signupnew

def about_us_page():
    home_window.destroy()
    import aboutus

def marqueuee_fun(widget,widget_w,widget_h,total_w,total_h,direction,speed,position=0):
    if direction=='right':
        if position>=total_w-widget_w:
            position=0
        position=position+speed
        widget.place(x=position)
        
#now we call this function after 0.01 sec 
    widget.after(10,lambda:marqueuee_fun(widget,widget_w,widget_h,total_w,total_h,direction,speed,position))

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

#Marqueue Label
marqueueelabel=Label(home_window,text='WELCOME TO THE WORLD OF PIZZAZZZ.....',fg='black',bg='yellowgreen',font=('georgia',15,'bold'))
marqueueelabel.place(x=50,y=100,width=580,height=50)

#Marqueue Function
marqueueelabel.after(100,lambda:marqueuee_fun(marqueueelabel,0,0,650,100,'right',2))

sloganLabel=Label(home_window,text='Top Your Crust With Kindness And Trust..!',fg='white',bg='black',font=('comic sans sm',13,'bold'))
sloganLabel.place(x=25,y=365)


clickButton=Button(home_window,text= "About Us",cursor="hand2", bd=2,font=("comic sans",12),
                   activebackground='orange',bg="white",fg="black",command=about_us_page)
clickButton.place(x=5,y=10)


clickButton=Button(home_window,text= "Login",cursor="hand2", bd=2,font=("comic sans",18, 'bold'),
                   activebackground='orange',bg="black",fg="white",command=login_page)
clickButton.place(x=45,y=550)

clickButton=Button(home_window,text= "SignUp",cursor="hand2", bd=2,font=("comic sans",18, 'bold'),
                   activebackground='orange',command=signup_page)
clickButton.place(x=145,y=550)

home_window.mainloop()