from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk
import random
import time
import requests

def receipt_page():
    sides.destroy()
    import receipt

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
                   activebackground='orange',bg="white",fg="black",command=receipt_page)
Confirm_order.place(x=150,y=720)
searchmore=Button(sides,text= "Search More",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
searchmore.place(x=340,y=720)


sides.mainloop()