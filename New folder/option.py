from  tkinter import*
from PIL import ImageTk

def vegmenu_page():
    option_window.destroy()
    import vegmenu
    
def nonvegmenu_page():
    option_window.destroy()
    import nonvegmenu

def sides_page():
    option_window.destroy()
    import sides

option_window=Tk()
option_window.geometry('900x500+300+55')
option_window.title('Option Window')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\optionbg.png")
option_window.resizable(False,False)

bgLabel=Label(option_window,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH,expand=1)

heading=Label(option_window,text='Please Choose Your Order Type From The Below',fg='firebrick4',font=('georgia',25,'bold'),
              bg="white")
heading.place(x=30,y=20)

#Veg Pizzas
veg_btn=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\vegpizza.png")
img_label=Label(image=veg_btn)

veg=Button(option_window,image=veg_btn,borderwidth=5,height=110,width=110,command=vegmenu_page)
veg.place(x=20,y=130)

my_label=Label(option_window,text='Veg Pizzas ',font=('georgia',10,'bold'),fg='black',bd=10,bg='white')
my_label.place(x=30,y=275)


#Non Veg Pizzas
nonveg_btn=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\nonvegpizza.png")
img_label=Label(image=nonveg_btn)

nonveg=Button(option_window,image=nonveg_btn,borderwidth=5,height=110,width=110,command=nonvegmenu_page)
nonveg.place(x=180,y=130)

my_label=Label(option_window,text='Non-Veg Pizzas ',font=('georgia',10,'bold'),fg='black',bd=10,bg='white')
my_label.place(x=175,y=275)


#sides
sides_btn=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\fries.png")
img_label=Label(image=sides_btn)

sides=Button(option_window,image=sides_btn,borderwidth=5,height=110,width=110,command=sides_page)
sides.place(x=340,y=130)

my_label=Label(option_window,text='Sides',font=('georgia',10,'bold'),fg='black',bd=10,bg='white')
my_label.place(x=360,y=275)

option_window.mainloop()