from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk
import random
import time
import requests

def receipt_page():
    nonvegmenu.destroy()
    import receipt

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
                   activebackground='orange',bg="white",fg="black",command=receipt_page)
Confirm_order.place(x=150,y=720)
searchmore=Button(nonvegmenu,text= "Search More",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
searchmore.place(x=340,y=720)




nonvegmenu.mainloop()