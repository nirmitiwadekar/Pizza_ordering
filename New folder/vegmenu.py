from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk
import random
import time
import requests

def receipt_page():
    vegmenu.destroy()
    import receipt

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

    #costofvegpizzasvar.set('')
    #subtotalvar.set('')
    #GSTvar.set('')

    

'''def receipt():
    global billnumber,date
    if costofvegpizzasvar.get() != '' :#or costofnvpizzasvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_margherita.get()!='0':
            textReceipt.insert(END,f'Maargherita :\t\t\t{int(e_margherita.get())*99}\n\n')

        if e_goldencorn.get()!='0':
            textReceipt.insert(END,f'Golden Corn :\t\t\t{int(e_goldencorn.get())*99}\n\n')

        if e_mixveg.get()!='0':
            textReceipt.insert(END,f'Mix-veg :\t\t\t{int(e_mixveg.get())*120}\n\n')

        if e_farmhouse.get() != '0':
            textReceipt.insert(END, f'Farmhouse :\t\t\t{int(e_farmhouse.get()) * 130}\n\n')

        if e_peppy_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer Special:\t\t\t{int(e_peppy_paneer.get()) * 140}\n\n')

        if e_smokey_paneer.get() != '0':
            textReceipt.insert(END, f'Smokey Paneer:\t\t\t{int(e_smokey_paneer.get()) * 150}\n\n')

        if e_mexican.get() != '0':
            textReceipt.insert(END, f'Smokey veggie:\t\t\t{int(e_mexican.get()) * 150}\n\n')

        if e_pizza_paratha.get() != '0':
            textReceipt.insert(END, f'Mexican :\t\t\t{int(e_mexican.get()) * 180}\n\n')

        if e_veg_momo.get() != '0':
            textReceipt.insert(END, f'paratha pizza:\t\t\t{int(e_pizza_paratha.get()) * 200}\n\n')
        if e_mashroom.get() != '0':
            textReceipt.insert(END, f'paratha pizza:\t\t\t{int(e_mashroom.get()) * 200}\n\n')


def totalcost():
    global priceofvegpizzas #,priceofDrinks,priceofnvpizzas,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0:
        
        item1=int(e_margherita.get())
        item2=int(e_goldencorn.get())
        item3=int(e_mixveg.get())
        item4 = int(e_farmhouse.get())
        item5 = int(e_peppy_paneer.get())
        item6 = int(e_smokey_paneer.get())
        item7 = int(e_mexican.get())
        item8 = int(e_pizza_paratha.get())
        item9 = int(e_veg_momo.get())
        item9 = int(e_mashroom.get())

        priceofvegpizzas=(item1*99)+(item2*99)+(item3*120)+(item4*130)+ (item5*140) + (item6 * 150) + (item7 * 150) \
                    + (item8 * 199) + (item9 * 219) + (item9 * 249)
        
        costofvegpizzasvar.set(str(priceofvegpizzas)+ ' Rs')
'''

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
                   activebackground='orange',bg="white",fg="black",command=receipt_page)
Confirm_order.place(x=150,y=720)
searchmore=Button(vegmenu,text= "Search More",cursor="hand2", bd=2,font=("comic sans",16, 'bold'),
                   activebackground='orange',bg="white",fg="black",command=option_page)
searchmore.place(x=340,y=720)



vegmenu.mainloop()