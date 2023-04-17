from  tkinter import*
from PIL import ImageTk

def home_page():
    aboutus_window.destroy()
    import homepg


aboutus_window=Tk()
aboutus_window.geometry('500x330+500+230')
aboutus_window.title('About Us Window')
bgImage=ImageTk.PhotoImage(file="C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\images\\aboutus.png")
aboutus_window.resizable(False,False)

bgLabel=Label(aboutus_window,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH,expand=1)

backButton=Button(aboutus_window,text= "back",cursor="hand2", bd=2,font=("comic sans",12, 'bold'),
                   activebackground='orange',bg="firebrick",fg="white",command=home_page)
backButton.place(x=220,y=280)

aboutus_window.mainloop()