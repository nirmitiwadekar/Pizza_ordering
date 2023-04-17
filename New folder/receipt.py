from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk
import random
import time
import requests


receipt=Tk()

receipt.geometry('1000x780+100+0')

receipt.resizable(0,0)

receipt.title('Pizza Order Management System ')

bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\receiptbg4.png")
receipt.resizable(False,False)

bgLabel=Label(receipt,image=bgImage)
bgLabel.pack(fill=BOTH,expand=1)

labelType=Label(receipt,text='Bill For Your Order ',font=('georgia',15,'bold'),fg='white',border=10,borderwidth=10,
                 bg='red',width=15)
labelType.place(x=400,y=100)

labelTitle=Label(receipt,text='The Crispy Crust Pizzeria',font=('Georgia',25,'bold'),fg='Maroon',border=10,borderwidth=10,
                 bg='white',width=25)
labelTitle.place(x=200,y=20)

signupframe=Frame(receipt,width=550,height=600,bg='wheat',border=5)
signupframe.place(x=30,y=170)

def reset():
    costofsidessvar.set('')
    costofvegpizzasvar.set('')
    costofnvpizzasvar.set('')
    subtotalvar.set('')
    GSTvar.set('')
    totalcostvar.set('')
    
receipt.mainloop()