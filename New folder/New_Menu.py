from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk
import random
import time
import requests
#---------------------------------OPTION-----------------------------------
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

sides=Button(option_window,image=sides_btn,borderwidth=5,height=110,width=110,command=nonvegmenu_page)
sides.place(x=340,y=130)

my_label=Label(option_window,text='Sides',font=('georgia',10,'bold'),fg='black',bd=10,bg='white')
my_label.place(x=360,y=275)

option_window.mainloop()

#---------------------------------VEG MENU---------------------------------
def home_page():
    vegmenu.destroy()
    import homepg

def option_page():
    vegmenu.destroy()
    import option

# radio  button to order 
def clicked(value):
    radioLabel=Label(vegmenu,text=value)
    radioLabel.pack()


#Functions

def margherita():
    if var1.get()==1:
        textmargherita.config(state=NORMAL)
        textmargherita.focus()
        textmargherita.delete(0,END)
    elif var1.get() == 0:
        textmargherita.config(state=DISABLED)
        e_margherita.set('0')

def goldencorn():
    if var2.get()==1:
        textgoldencorn.config(state=NORMAL)
        textgoldencorn.focus()
        textgoldencorn.delete(0,END)
    elif var2.get() == 0:
        textgoldencorn.config(state=DISABLED)
        e_goldencorn.set('0')

def mixveg():
    if var3.get()==1:
        textmixveg.config(state=NORMAL)
        textmixveg.focus()
        textmixveg.delete(0,END)
    elif var3.get() == 0:
        textmixveg.config(state=DISABLED)
        e_mixveg.set('0')

def farmhouse():
    if var4.get() == 1:
        textfarmhouse.config(state=NORMAL)
        textfarmhouse.focus()
        textfarmhouse.delete(0, END)
    elif var4.get() == 0:
        textfarmhouse.config(state=DISABLED)
        e_farmhouse.set('0')


def peppy_paneer():
    if var5.get() == 1:
        textpeppy_paneer.config(state=NORMAL)
        textpeppy_paneer.focus()
        textpeppy_paneer.delete(0, END)
    elif var5.get() == 0:
        textpeppy_paneer.config(state=DISABLED)
        e_peppy_paneer.set('0')


def smokey_paneer():
    if var6.get() == 1:
        textsmokey_paneer.config(state=NORMAL)
        textsmokey_paneer.focus()
        textsmokey_paneer.delete(0, END)
    elif var6.get() == 0:
        textsmokey_paneer.config(state=DISABLED)
        e_smokey_paneer.set('0')


def mexican():
    if var7.get() == 1:
        textmexican.config(state=NORMAL)
        textmexican.focus()
        textmexican.delete(0, END)
    elif var7.get() == 0:
        textmexican.config(state=DISABLED)
        e_mexican.set('0')


def pizza_paratha():
    if var8.get() == 1:
        textpizzaparatha.config(state=NORMAL)
        textpizzaparatha.focus()
        textpizzaparatha.delete(0, END)
    elif var8.get() == 0:
        textpizzaparatha.config(state=DISABLED)
        e_pizza_paratha.set('0')

def veg_momo():
    if var9.get()==1:
        textveg_momo.config(state=NORMAL)
        textveg_momo.focus()
        textveg_momo.delete(0,END)
    elif var9.get() == 0:
        textveg_momo.config(state=DISABLED)
        e_veg_momo.set('0')

def mashroom():
    if var10.get()==1:
        textmashroom.config(state=NORMAL)
        textmashroom.focus()
        textmashroom.delete(0,END)
    elif var10.get() == 0:
        textmashroom.config(state=DISABLED)
        e_mashroom.set('0')

def reset():
    #textReceipt.delete(1.0,END)
    e_margherita.set('0')
    e_goldencorn.set('0')
    e_mixveg.set('0')
    e_farmhouse.set('0')
    e_peppy_paneer.set('0')
    e_smokey_paneer.set('0')
    e_mexican.set('0')
    e_pizza_paratha.set('0')
    e_veg_momo.set('0')
    e_mashroom.set('0')

    textmargherita.config(state=DISABLED)
    textgoldencorn.config(state=DISABLED)
    textmixveg.config(state=DISABLED)
    textfarmhouse.config(state=DISABLED)
    textpeppy_paneer.config(state=DISABLED)
    textsmokey_paneer.config(state=DISABLED)
    textmexican.config(state=DISABLED)
    textpizzaparatha.config(state=DISABLED)
    textveg_momo.config(state=DISABLED)
    textmashroom.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)

vegmenu=Tk()
vegmenu.geometry('1540x780+0+0')
vegmenu.title('Veg vegmenu')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\blackbg.png")
vegmenu.resizable(False,False)

bgLabel=Label(vegmenu,image=bgImage)
bgLabel.pack(fill=BOTH,expand=1)

labelTitle=Label(vegmenu,text='The Crispy Crust Pizzeria',font=('georgia',34,'bold'),fg='Maroon',border=10,borderwidth=10,
                 bg='white',width=30)
labelTitle.place(x=300,y=20)

labelType=Label(vegmenu,text='Veg Menu',font=('georgia',10,'bold'),fg='white',border=10,borderwidth=10,
                 bg='green',width=15)
labelType.place(x=30,y=20)

#Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

e_margherita=StringVar()
e_goldencorn=StringVar()
e_mixveg=StringVar()
e_farmhouse=StringVar()
e_peppy_paneer=StringVar()
e_smokey_paneer=StringVar()
e_mexican=StringVar()
e_pizza_paratha=StringVar()
e_veg_momo=StringVar()
e_mashroom=StringVar()

e_margherita.set('0')
e_goldencorn.set('0')
e_mixveg.set('0')
e_farmhouse.set('0')
e_peppy_paneer.set('0')
e_smokey_paneer.set('0')
e_mexican.set('0')
e_pizza_paratha.set('0')
e_veg_momo.set('0')
e_mashroom.set('0')

#Margherita
margherita_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\margherita.png")
img_label=Label(image=margherita_label)

margherita_lbl=Label(vegmenu,image=margherita_label,borderwidth=5,height=160,width=160)
margherita_lbl.place(x=70,y=130)

margherita=Checkbutton(vegmenu,text='Margherita',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var1
                 ,command=margherita)
margherita.place(x=70,y=312)

#text entry for golden corn
textmargherita = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_margherita)
textmargherita.place(x=70,y=360)

#goldencorn
goldencorn_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\goldencorn.png")
img_label=Label(image=goldencorn_label)

goldencorn_lbl=Label(vegmenu,image=goldencorn_label,borderwidth=5,height=160,width=160)
goldencorn_lbl.place(x=70,y=410)

goldencorn=Checkbutton(vegmenu,text='Golden Corn',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var2
                 ,command=goldencorn)
goldencorn.place(x=70,y=600)

#text entry for golden corn
textgoldencorn = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_goldencorn)
textgoldencorn.place(x=70,y=650)


#Mix Veg Delight
mixveg_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\mix-veg.png")
img_label=Label(image=mixveg_label)

mixveg_lbl=Label(vegmenu,image=mixveg_label,borderwidth=5,height=160,width=160)
mixveg_lbl.place(x=380,y=130)

mixveg=Checkbutton(vegmenu,text='Mix-Veg Delight',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var3
                 ,command=mixveg)
mixveg.place(x=380,y=312)

#text entry
textmixveg = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_mixveg)
textmixveg.place(x=380,y=360)

#Farmhouse
farmhouse_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\farmhouse.png")
img_label=Label(image=farmhouse_label)

farmhouse_lbl=Label(vegmenu,image=farmhouse_label,borderwidth=5,height=160,width=160)
farmhouse_lbl.place(x=380,y=410)

farmhouse=Checkbutton(vegmenu,text='Farm House',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var4
                 ,command=farmhouse)
farmhouse.place(x=380,y=600)

#text entry
textfarmhouse = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_farmhouse)
textfarmhouse.place(x=380,y=650)

#peppy paneer
peppypaneer_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\peppy_paneer.png")
img_label=Label(image=peppypaneer_label)

peppypaneer_lbl=Label(vegmenu,image=peppypaneer_label,borderwidth=5,height=160,width=160)
peppypaneer_lbl.place(x=690,y=130)

peppy_paneer=Checkbutton(vegmenu,text='Peppy Paneer',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var5
                 ,command=peppy_paneer)
peppy_paneer.place(x=700,y=312)

#text entry
textpeppy_paneer = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_peppy_paneer)
textpeppy_paneer.place(x=700,y=360)

#Smokey Paneer
smokeypaneer_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\smokeypaneer.png")
img_label=Label(image=smokeypaneer_label)

smokeypaneer_lbl=Label(vegmenu,image=smokeypaneer_label,borderwidth=5,height=160,width=160)
smokeypaneer_lbl.place(x=700,y=410)

smokey_paneer=Checkbutton(vegmenu,text='Smokey Paneer',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var6
                 ,command=smokey_paneer)
smokey_paneer.place(x=700,y=600)

#text entry
textsmokey_paneer = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_smokey_paneer)
textsmokey_paneer.place(x=700,y=650)

#Mexican Pizza
mexican_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\Mexican.png")
img_label=Label(image=mexican_label)

mexican_lbl=Label(vegmenu,image=mexican_label,borderwidth=5,height=160,width=160)
mexican_lbl.place(x=980,y=130)

mexican=Checkbutton(vegmenu,text='Mexican Pizza ',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var7
                 ,command=mexican)
mexican.place(x=990,y=312)

#text entry
textmexican = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_mexican)
textmexican.place(x=990,y=360)

#pizza paratha
parathapizza_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\parathapizza.png")
img_label=Label(image=parathapizza_label)

parathapizza_lbl=Label(vegmenu,image=parathapizza_label,borderwidth=5,height=160,width=160)
parathapizza_lbl.place(x=980,y=410)

pizza_paratha=Checkbutton(vegmenu,text='Pizza Paratha',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var8
                 ,command=pizza_paratha)
pizza_paratha.place(x=990,y=600)

#text entry
textpizzaparatha = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_pizza_paratha)
textpizzaparatha.place(x=990,y=650)

#Veg Momo Pizza
veg_momo_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\veg_momo_pizza.png")
img_label=Label(image=veg_momo_label)

veg_momo_lbl=Label(vegmenu,image=veg_momo_label,borderwidth=5,height=160,width=160)
veg_momo_lbl.place(x=1270,y=130)

veg_momo=Checkbutton(vegmenu,text='Veg Momos Pizza',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var9
                 ,command=veg_momo)
veg_momo.place(x=1270,y=312)

#text entry
textveg_momo = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_veg_momo)
textveg_momo.place(x=1270,y=360)

#mashroom Pizza
mashroom_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\mashroom_pizza.png")
img_label=Label(image=mashroom_label)

mashroom_lbl=Label(vegmenu,image=mashroom_label,borderwidth=5,height=160,width=160)
mashroom_lbl.place(x=1270,y=410)

mashroom=Checkbutton(vegmenu,text='Mashroom Pizza ',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var10
                 ,command=mashroom)
mashroom.place(x=1270,y=600)

#text entry
textmashroom = Entry(vegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_mashroom)
textmashroom.place(x=1270,y=650)

#Radio Button
r=IntVar()

smallButton=Radiobutton(vegmenu,text="Regular",variable=r,value=1,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
smallButton.place(x=1050,y=710)
mediumButton=Radiobutton(vegmenu,text="Medium",variable=r,value=2,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
mediumButton.place(x=1180,y=710)
largeButton=Radiobutton(vegmenu,text="Large",variable=r,value=3,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
largeButton.place(x=1310,y=710)

#Buttons
backButton=Button(vegmenu,text= "Back",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
backButton.place(x=50,y=720)

Confirm_order=Button(vegmenu,text= "Confirm Order",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=home_page)
Confirm_order.place(x=150,y=720)
searchmore=Button(vegmenu,text= "Search More",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
searchmore.place(x=340,y=720)



vegmenu.mainloop()


#------------------------NON VEG MENU---------------------------------

def home_page():
    nonvegmenu.destroy()
    import homepg

def option_page():
    nonvegmenu.destroy()
    import option

def clicked(value):
    radioLabel=Label(nonvegmenu,text=value)
    radioLabel.pack()

#Functions

def chickendelight():
    if var11.get()==1:
        textchicken_delight.config(state=NORMAL)
        textchicken_delight.delete(0,END)
        textchicken_delight.focus()
    elif var11.get() == 0:
        textchicken_delight.config(state=DISABLED)
        e_chicken_delight.set('0')

def chickendominator():
    if var12.get()==1:
        textchicken_dominator.config(state=NORMAL)
        textchicken_dominator.delete(0,END)
        textchicken_dominator.focus()
    elif var12.get() == 0:
        textchicken_dominator.config(state=DISABLED)
        e_chicken_dominator.set('0')
    
def chickensatay():
    if var13.get()==1:
        textchicken_satay.config(state=NORMAL)
        textchicken_satay.delete(0,END)
        textchicken_satay.focus()
    elif var13.get() == 0:
        textchicken_satay.config(state=DISABLED)
        e_chicken_satay.set('0')

def chickensausage():
    if var14.get()==1:
        textchicken_sausage.config(state=NORMAL)
        textchicken_sausage.delete(0,END)
        textchicken_sausage.focus()
    elif var14.get() == 0:
        textchicken_sausage.config(state=DISABLED)
        e_chicken_sausage.set('0')

def chicken_tikka():
    if var15.get()==1:
        textchicken_tikka.config(state=NORMAL)
        textchicken_tikka.delete(0,END)
        textchicken_tikka.focus()
    elif var15.get() == 0:
        textchicken_tikka.config(state=DISABLED)
        e_chicken_tikka.set('0')

def chicken_peri_peri():
    if var16.get()==1:
        textchicken_peri_peri.config(state=NORMAL)
        textchicken_peri_peri.delete(0,END)
        textchicken_peri_peri.focus()
    elif var16.get() == 0:
        textchicken_peri_peri.config(state=DISABLED)
        e_chicken_peri_peri.set('0')

def meatball():
    if var17.get()==1:
        textmeatball.config(state=NORMAL)
        textmeatball.delete(0,END)
        textmeatball.focus()
    elif var17.get() == 0:
        textmeatball.config(state=DISABLED)
        e_meatball.set('0')

def pesto_chicken():
    if var18.get()==1:
        textpesto_chicken.config(state=NORMAL)
        textpesto_chicken.delete(0,END)
        textpesto_chicken.focus()
    elif var18.get() == 0:
        textpesto_chicken.config(state=DISABLED)
        e_pesto_chicken.set('0')

def nonveg_momo():
    if var19.get()==1:
        textnonveg_momo.config(state=NORMAL)
        textnonveg_momo.delete(0,END)
        textnonveg_momo.focus()
    elif var19.get() == 0:
        textnonveg_momo.config(state=DISABLED)
        e_nonveg_momo.set('0')

def gamberi():
    if var20.get()==1:
        textgambiri.config(state=NORMAL)
        textgambiri.delete(0,END)
        textgambiri.focus()
    elif var20.get() == 0:
        textgambiri.config(state=DISABLED)
        e_gamberi.set('0')


def reset():
    #textReceipt.delete(1.0,END)
    e_chicken_delight.set('0')
    e_chicken_dominator.set('0')
    e_chicken_satay.set('0')
    e_chicken_sausage.set('0')
    e_chicken_tikka.set('0')
    e_chicken_peri_peri.set('0')
    e_meatball.set('0')
    e_pesto_chicken.set('0')
    e_nonveg_momo.set('0')
    e_gamberi.set('0')

    textchicken_delight.config(state=DISABLED)
    textchicken_dominator.config(state=DISABLED)
    textchicken_satay.config(state=DISABLED)
    textchicken_sausage.config(state=DISABLED)
    textchicken_tikka.config(state=DISABLED)
    textchicken_peri_peri.config(state=DISABLED)
    textmeatball.config(state=DISABLED)
    textpesto_chicken.config(state=DISABLED)
    textnonveg_momo.config(state=DISABLED)
    textgambiri.config(state=DISABLED)
    
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)


nonvegmenu=Tk()
nonvegmenu.geometry('1540x780+0+0')
nonvegmenu.title('Non-Veg menu')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\blackbg.png")
nonvegmenu.resizable(False,False)

bgLabel=Label(nonvegmenu,image=bgImage)
bgLabel.pack(fill=BOTH,expand=1)

labelType=Label(nonvegmenu,text='Non-Veg Menu',font=('georgia',10,'bold'),fg='white',border=10,borderwidth=10,
                 bg='red',width=15)
labelType.place(x=30,y=20)

labelTitle=Label(nonvegmenu,text='The Crispy Crust Pizzeria',font=('Georgia',34,'bold'),fg='Maroon',border=10,borderwidth=10,
                 bg='white',width=30)
labelTitle.place(x=300,y=20)

#Variables

var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

e_chicken_delight=StringVar()
e_chicken_dominator=StringVar()
e_chicken_satay=StringVar()
e_chicken_sausage=StringVar()
e_chicken_tikka=StringVar()
e_chicken_peri_peri=StringVar()
e_meatball=StringVar()
e_pesto_chicken=StringVar()
e_nonveg_momo=StringVar()
e_gamberi=StringVar()

e_chicken_delight.set('0')
e_chicken_dominator.set('0')
e_chicken_satay.set('0')
e_chicken_sausage.set('0')
e_chicken_tikka.set('0')
e_chicken_peri_peri.set('0')
e_meatball.set('0')
e_pesto_chicken.set('0')
e_nonveg_momo.set('0')
e_gamberi.set('0')

#chicken Delight
chickendelight_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\chicken-delight.png")
img_label=Label(image=chickendelight_label)

chickendelight_lbl=Label(nonvegmenu,image=chickendelight_label,borderwidth=5,height=160,width=150)
chickendelight_lbl.place(x=70,y=130)

chickendelight=Checkbutton(nonvegmenu,text='Chicken Delight',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var11
                 ,command=chickendelight)
chickendelight.place(x=70,y=315)

#Text Entries
textchicken_delight = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_delight)
textchicken_delight.place(x=70,y=360)

#chickendominator
chickendominator_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\Chicken-dominator.png")
img_label=Label(image=chickendominator_label)

chickendominator_lbl=Label(nonvegmenu,image=chickendominator_label,borderwidth=0,height=160,width=160)
chickendominator_lbl.place(x=70,y=410)

chickendominator=Checkbutton(nonvegmenu,text='Chicken Dominator',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var12
                 ,command=chickendominator)
chickendominator.place(x=70,y=600)

#Text Entries
textchicken_dominator = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_dominator)
textchicken_dominator.place(x=70,y=650)

#chicken Sataty
chicken_satay_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\chicken-satay.png")
img_label=Label(image=chicken_satay_label)

chickensatay_lbl=Label(nonvegmenu,image=chicken_satay_label,borderwidth=0,height=160,width=160)
chickensatay_lbl.place(x=380,y=130)

chickensatay=Checkbutton(nonvegmenu,text='Chicken Satay',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var13
                 ,command=chickensatay)
chickensatay.place(x=390,y=315)

#Text Entries
textchicken_satay = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_satay)
textchicken_satay.place(x=390,y=360)


#chicken_sausage
chicken_sausage_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\chicken-sausage.png")
img_label=Label(image=chicken_sausage_label)

chicken_sausage_lbl=Label(nonvegmenu,image=chicken_sausage_label,borderwidth=5,height=160,width=160)
chicken_sausage_lbl.place(x=380,y=410)

chickensausage=Checkbutton(nonvegmenu,text='Chicken Sausage',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var14
                 ,command=chickensausage)
chickensausage.place(x=380,y=600)

#Text Entries
textchicken_sausage = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_sausage)
textchicken_sausage.place(x=380,y=650)


#Chicken Tikka 
chicken_tikka_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\chicken-tikka.png")
img_label=Label(image=chicken_tikka_label)

chicken_tikka_lbl=Label(nonvegmenu,image=chicken_tikka_label,borderwidth=5,height=160,width=160)
chicken_tikka_lbl.place(x=690,y=130)

chicken_tikka=Checkbutton(nonvegmenu,text='Chicken Tikka',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var15
                 ,command=chicken_tikka)
chicken_tikka.place(x=700,y=315)

#Text Entries
textchicken_tikka = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_tikka)
textchicken_tikka.place(x=700,y=360)


#Chicken Peri Peri
chicken_peri_peri_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\chickenperi-peri.png")
img_label=Label(image=chicken_peri_peri_label)

chicken_peri_peri_lbl=Label(nonvegmenu,image=chicken_peri_peri_label,borderwidth=5,height=160,width=160)
chicken_peri_peri_lbl.place(x=690,y=410)

chicken_peri_peri=Checkbutton(nonvegmenu,text='Chicken Peri-Peri',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var16
                 ,command=chicken_peri_peri)
chicken_peri_peri.place(x=690,y=600)

#Text Entries
textchicken_peri_peri = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_peri_peri)
textchicken_peri_peri.place(x=690,y=650)


#MeatBall Pizza
meatball_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\meatball-pizza.png")
img_label=Label(image=meatball_label)

meatball_lbl=Label(nonvegmenu,image=meatball_label,borderwidth=5,height=160,width=160)
meatball_lbl.place(x=980,y=130)

meatball=Checkbutton(nonvegmenu,text='MeatBall Pizza ',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var17
                 ,command=meatball)
meatball.place(x=990,y=315)

#Text Entries
textmeatball = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_meatball)
textmeatball.place(x=990,y=360)


#Basil Pesto Pizza 
pesto_chicken_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\pesto-chicken.png")
img_label=Label(image=pesto_chicken_label)

pesto_chicken_lbl=Label(nonvegmenu,image=pesto_chicken_label,borderwidth=5,height=160,width=160)
pesto_chicken_lbl.place(x=980,y=410)

pesto_chicken=Checkbutton(nonvegmenu,text='Pesto Chicken',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var18
                 ,command=pesto_chicken)
pesto_chicken.place(x=990,y=600)

#Text Entries
textpesto_chicken = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_pesto_chicken)
textpesto_chicken.place(x=990,y=650)


#Momo Pizza
nonveg_momo_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\chicken_momo_pizza.png")
img_label=Label(image=nonveg_momo_label)

nonveg_momo_lbl=Label(nonvegmenu,image=nonveg_momo_label,borderwidth=5,height=160,width=160)
nonveg_momo_lbl.place(x=1270,y=130)

nonveg_momo=Checkbutton(nonvegmenu,text='chicken Momos Pizza',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var19
                 ,command=nonveg_momo)
nonveg_momo.place(x=1270,y=315)

#Text Entries
textnonveg_momo = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_nonveg_momo)
textnonveg_momo.place(x=1270,y=360)


#Gamberi Pizza
gamberi_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\gamberi.png")
img_label=Label(image=gamberi_label)

gamberi_lbl=Label(nonvegmenu,image=gamberi_label,borderwidth=5,height=160,width=160)
gamberi_lbl.place(x=1270,y=410)

gamberi=Checkbutton(nonvegmenu,text='Gamberi Shrimp Pizza ',font=('georgia',10,'bold'),fg='black',bd=8,bg='white',onvalue=1,offvalue=0,variable=var20
                 ,command=gamberi)
gamberi.place(x=1270,y=600)

#Text Entries
textgambiri = Entry(nonvegmenu, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_gamberi)
textgambiri.place(x=1270,y=650)


#Radio Button
r=IntVar()

smallButton=Radiobutton(nonvegmenu,text="Regular",variable=r,value=1,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
smallButton.place(x=1050,y=710)
mediumButton=Radiobutton(nonvegmenu,text="Medium",variable=r,value=2,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
mediumButton.place(x=1180,y=710)
largeButton=Radiobutton(nonvegmenu,text="Large",variable=r,value=3,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
largeButton.place(x=1310,y=710)

#Buttons
backButton=Button(nonvegmenu,text= "Back",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
backButton.place(x=50,y=720)

Confirm_order=Button(nonvegmenu,text= "Confirm Order",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=home_page)
Confirm_order.place(x=150,y=720)
searchmore=Button(nonvegmenu,text= "Search More",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
searchmore.place(x=340,y=720)




nonvegmenu.mainloop()


#--------------------------------------SIDES---------------------------------------

def home_page():
    sides.destroy()
    import homepg

def option_page():
    sides.destroy()
    import option

def clicked(value):
    radioLabel=Label(sides,text=value)
    radioLabel.pack()

#Functions
def cappeccino():
    if var21.get()==1:
        textcappeccino.config(state=NORMAL)
        textcappeccino.delete(0,END)
        textcappeccino.focus()
    elif var21.get() == 0:
        textcappeccino.config(state=DISABLED)
        e_cappeccino.set('0')

def black_tea():
    if var22.get()==1:
        textblack_tea.config(state=NORMAL)
        textblack_tea.delete(0,END)
        textblack_tea.focus()
    elif var22.get() == 0:
        textblack_tea.config(state=DISABLED)
        e_black_tea.set('0')
    
def garlic_bread():
    if var23.get()==1:
        textgarlic_bread.config(state=NORMAL)
        textgarlic_bread.delete(0,END)
        textgarlic_bread.focus()
    elif var23.get() == 0:
        textgarlic_bread.config(state=DISABLED)
        e_garlic_bread.set('0')

def stuffed_garlic_bread():
    if var24.get()==1:
        textstuffed_garlic_bread.config(state=NORMAL)
        textstuffed_garlic_bread.delete(0,END)
        textstuffed_garlic_bread.focus()
    elif var25.get() == 0:
        textstuffed_garlic_bread.config(state=DISABLED)
        e_stuffed_garlic_bread.set('0')

def french_fries():
    if var25.get()==1:
        textfrench_fries.config(state=NORMAL)
        textfrench_fries.delete(0,END)
        textfrench_fries.focus()
    elif var25.get() == 0:
        textfrench_fries.config(state=DISABLED)
        e_french_fries.set('0')

def chicken_popcorn():
    if var26.get()==1:
        textchicken_popcorn.config(state=NORMAL)
        textchicken_popcorn.delete(0,END)
        textchicken_popcorn.focus()
    elif var26.get() == 0:
        textchicken_popcorn.config(state=DISABLED)
        e_chicken_popcorn.set('0')

def potato_balls():
    if var27.get()==1:
        textpotato_balls.config(state=NORMAL)
        textpotato_balls.delete(0,END)
        textpotato_balls.focus()
    elif var27.get() == 0:
        textpotato_balls.config(state=DISABLED)
        e_potato_balls.set('0')

def veg_tacco():
    if var28.get()==1:
        textveg_tacco.config(state=NORMAL)
        textveg_tacco.delete(0,END)
        textveg_tacco.focus()
    elif var28.get() == 0:
        textveg_tacco.config(state=DISABLED)
        e_veg_tacco.set('0')

def drinks():
    if var29.get()==1:
        textdrinks.config(state=NORMAL)
        textdrinks.delete(0,END)
        textdrinks.focus()
    elif var29.get() == 0:
        textdrinks.config(state=DISABLED)
        e_drinks.set('0')

def nonveg_tacco():
    if var30.get()==1:
        textnonveg_tacco.config(state=NORMAL)
        textnonveg_tacco.delete(0,END)
        textnonveg_tacco.focus()
    elif var30.get() == 0:
        textnonveg_tacco.config(state=DISABLED)
        e_nonveg_tacco.set('0')


def reset():
    #textReceipt.delete(1.0,END)
    e_cappeccino.set('0')
    e_black_tea.set('0')
    e_garlic_bread.set('0')
    e_stuffed_garlic_bread.set('0')
    e_french_fries.set('0')
    e_chicken_popcorn.set('0')
    e_potato_balls.set('0')
    e_veg_tacco.set('0')
    e_drinks.set('0')
    e_nonveg_tacco.set('0')
    

    textcappeccino.config(state=DISABLED)
    textblack_tea.config(state=DISABLED)
    textgarlic_bread.config(state=DISABLED)
    textstuffed_garlic_bread.config(state=DISABLED)
    textfrench_fries.config(state=DISABLED)
    textchicken_popcorn.config(state=DISABLED)
    textpotato_balls.config(state=DISABLED)
    textveg_tacco.config(state=DISABLED)
    textdrinks.config(state=DISABLED)
    textnonveg_tacco.config(state=DISABLED)
    
    
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)




sides=Tk()
sides.geometry('1540x780+0+0')
sides.title('Sides & Breverages')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\blackbg.png")
sides.resizable(False,False)

bgLabel=Label(sides,image=bgImage)
bgLabel.pack(fill=BOTH,expand=1)

labelTitle=Label(sides,text='The Crispy Crust Pizzeria',font=('Georgia',34,'bold'),fg='Maroon',border=10,borderwidth=10,
                 bg='white',width=30)
labelTitle.place(x=300,y=20)

labelType=Label(sides,text='Sides & Breverages',font=('georgia',10,'bold'),fg='black',border=10,borderwidth=10,
                 bg='orange',width=15)
labelType.place(x=30,y=20)

#Variables

var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()

e_cappeccino=StringVar()
e_black_tea=StringVar()
e_garlic_bread=StringVar()
e_stuffed_garlic_bread=StringVar()
e_french_fries=StringVar()
e_chicken_popcorn=StringVar()
e_potato_balls=StringVar()
e_veg_tacco=StringVar()
e_drinks=StringVar()
e_nonveg_tacco=StringVar()

e_cappeccino.set('0')
e_black_tea.set('0')
e_garlic_bread.set('0')
e_stuffed_garlic_bread.set('0')
e_french_fries.set('0')
e_chicken_popcorn.set('0')
e_potato_balls.set('0')
e_veg_tacco.set('0')
e_drinks.set('0')
e_nonveg_tacco.set('0')

#cappecino
cappeccino_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\coffee.png")
img_label=Label(image=cappeccino_label)

cappeccino_lbl=Label(sides,image=cappeccino_label,borderwidth=5,height=160,width=150)
cappeccino_lbl.place(x=70,y=130)

cappeccino=Checkbutton(sides,text='Cappeccino',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var21
                 ,command=cappeccino)
cappeccino.place(x=70,y=315)

#Text Entries
textcappeccino = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_cappeccino)
textcappeccino.place(x=70,y=365)


#blacktea
blacktea_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\blacktea.png")
img_label=Label(image=blacktea_label)

black_tea_lbl=Label(sides,image=blacktea_label,borderwidth=5,height=160,width=160)
black_tea_lbl.place(x=70,y=410)

black_tea=Checkbutton(sides,text='Black Tea',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var22
                 ,command=black_tea)
black_tea.place(x=70,y=600)

#Text Entries
textblack_tea = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_black_tea)
textblack_tea.place(x=70,y=650)


#Garlic bread
garlic_bread_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\garlic_bread.png")
img_label=Label(image=garlic_bread_label)

garlic_bread_lbl=Label(sides,image=garlic_bread_label,borderwidth=5,height=160,width=160)
garlic_bread_lbl.place(x=380,y=130)

garlic_bread=Checkbutton(sides,text='Garlic Bread',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var23
                 ,command=garlic_bread)
garlic_bread.place(x=390,y=315)

#Text Entries
textgarlic_bread = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_garlic_bread)
textgarlic_bread.place(x=390,y=365)


#stuffed garlic bread
stuffed_garlic_bread_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\stuffed-gb.png")
img_label=Label(image=stuffed_garlic_bread_label)

stuffed_garlic_bread_lbl=Label(sides,image=stuffed_garlic_bread_label,borderwidth=5,height=160,width=160)
stuffed_garlic_bread_lbl.place(x=380,y=410)

stuffed_garlic_bread=Checkbutton(sides,text='Stuffed Garlic Bread',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var24
                 ,command=stuffed_garlic_bread)
stuffed_garlic_bread.place(x=380,y=600)

#Text Entries
textstuffed_garlic_bread = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_stuffed_garlic_bread)
textstuffed_garlic_bread.place(x=380,y=650)


#French Fries
french_fries_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\fries-with-ketchup.png")
img_label=Label(image=french_fries_label)

french_fries_lbl=Label(sides,image=french_fries_label,borderwidth=5,height=160,width=160)
french_fries_lbl.place(x=690,y=130)

french_fries=Checkbutton(sides,text='French Fries',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var25
                 ,command=french_fries)
french_fries.place(x=700,y=315)

#Text Entries
textfrench_fries = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_french_fries)
textfrench_fries.place(x=700,y=365)


#chicken Popcorn 
chickenpop_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\popcorn-chicken.png")
img_label=Label(image=chickenpop_label)

chicken_popcorn_lbl=Label(sides,image=chickenpop_label,borderwidth=5,height=160,width=160)
chicken_popcorn_lbl.place(x=690,y=410)

chicken_popcorn=Checkbutton(sides,text='chicken Popcorn',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var26
                 ,command=chicken_popcorn)
chicken_popcorn.place(x=700,y=600)

#Text Entries
textchicken_popcorn = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_chicken_popcorn)
textchicken_popcorn.place(x=700,y=650)


#Potato Balls 
potatoballs_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\potato_balls.png")
img_label=Label(image=potatoballs_label)

potato_balls_lbl=Label(sides,image=potatoballs_label,borderwidth=5,height=160,width=160)
potato_balls_lbl.place(x=980,y=130)

potato_balls=Checkbutton(sides,text='Potato Balls',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var27
                 ,command=potato_balls)
potato_balls.place(x=990,y=315)

#Text Entries
textpotato_balls = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_potato_balls)
textpotato_balls.place(x=990,y=365)


#Tacco veg
vegtacco_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\veg-tacco.png")
img_label=Label(image=vegtacco_label)

veg_tacco_lbl=Label(sides,image=vegtacco_label,borderwidth=5,height=160,width=160)
veg_tacco_lbl.place(x=980,y=410)

veg_tacco=Checkbutton(sides,text='Veg Taccos ',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var28
                 ,command=veg_tacco)
veg_tacco.place(x=990,y=600)

#Text Entries
textveg_tacco = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_veg_tacco)
textveg_tacco.place(x=990,y=650)

#Drinks
drinks_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\drinks.png")
img_label=Label(image=drinks_label)

drinks_lbl=Label(sides,image=drinks_label,borderwidth=5,height=160,width=160)
drinks_lbl.place(x=1270,y=130)

drinks=Checkbutton(sides,text='Drinks',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var29
                 ,command=drinks)
drinks.place(x=1270,y=315)

#Text Entries
textdrinks = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_drinks)
textdrinks.place(x=1270,y=365)

#Tacco non-veg
nonvegtacco_label=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\nonveg-tacco.png")
img_label=Label(image=nonvegtacco_label)

nonveg_tacco_lbl=Label(sides,image=nonvegtacco_label,borderwidth=5,height=160,width=160)
nonveg_tacco_lbl.place(x=1270,y=410)

nonveg_tacco=Checkbutton(sides,text='Non-veg Taccos',font=('georgia',10,'bold'),fg='black',bd=10,bg='white',onvalue=1,offvalue=0,variable=var30
                 ,command=nonveg_tacco)
nonveg_tacco.place(x=1270,y=600)

#Text Entries
textnonveg_tacco = Entry(sides, font=('arial', 14, 'bold'), bd=2, width=6, state=DISABLED, textvariable=e_nonveg_tacco)
textnonveg_tacco.place(x=1270,y=650)


#Radio Button
r=IntVar()

smallButton=Radiobutton(sides,text="Regular",variable=r,value=1,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
smallButton.place(x=1050,y=710)
mediumButton=Radiobutton(sides,text="Medium",variable=r,value=2,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
mediumButton.place(x=1180,y=710)
largeButton=Radiobutton(sides,text="Large",variable=r,value=3,bd=8,font=("comic sans",14,"bold"),bg='white',fg='maroon',command=clicked(r.get()))
largeButton.place(x=1310,y=710)

#Buttons
backButton=Button(sides,text= "Back",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
backButton.place(x=50,y=720)

Confirm_order=Button(sides,text= "Confirm Order",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=home_page)
Confirm_order.place(x=150,y=720)
searchmore=Button(sides,text= "Search More",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
searchmore.place(x=340,y=720)


sides.mainloop()