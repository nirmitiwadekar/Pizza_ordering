from  tkinter import*
from PIL import ImageTk

def option_page():
    deliverypickup_window.destroy()
    import option

def option_page():
    deliverypickup_window.destroy()
    import option


deliverypickup_window=Tk()
deliverypickup_window.geometry('900x500+300+55')
deliverypickup_window.title('Delivery/PickUp Window')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\deliverypickup.png")
deliverypickup_window.resizable(False,False)

bgLabel=Label(deliverypickup_window,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH,expand=1)

heading=Label(deliverypickup_window,text='Please Choose Your Order Type From The Below',fg='Firebrick',font=('georgia',25,'bold'),
              bg="white")
heading.place(x=30,y=50)

#------------------Dine In------------------
dinein=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\dinein.png")
img_label=Label(image=dinein)
img_label.pack(pady=20)

dineinButton=Button(deliverypickup_window,image=dinein,command=option_page)
                  
dineinButton.place(x=350,y=250)

#------------------Delivery-------------------
delivery=PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\delivery.png")
img_label=Label(image=delivery)
img_label.pack(pady=20)

deliveryinButton=Button(deliverypickup_window,image=delivery,command=option_page)
                  
deliveryinButton.place(x=50,y=250)

#-------------------Labels-----------------------------
dineinlabel=Label(deliverypickup_window,text='Dine In',fg='firebrick',font=('georgia',25,'bold'),
              bg="white")
dineinlabel.place(x=400,y=430)

deliverylabel=Label(deliverypickup_window,text='Delivery',fg='firebrick',font=('georgia',25,'bold'),
              bg="white")
deliverylabel.place(x=100,y=430)

deliverypickup_window.mainloop()