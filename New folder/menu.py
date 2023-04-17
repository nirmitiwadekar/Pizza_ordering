from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_margherita.set('0')
    e_goldencorn.set('0')
    e_mixveg.set('0')
    e_farmhouse.set('0')
    e_paneerspecial.set('0')
    e_smokeypaneer.set('0')
    e_smokeyveg.set('0')
    e_mexican.set('0')
    e_parathapizza.set('0')

    e_coffee.set('0')
    e_tea.set('0')
    e_cold_drinks.set('0')
    e_stuffed_garlic_bread.set('0')
    e_garlic_bread.set('0')
    e_french_fries.set('0')
    e_taco_mexicana_veg.set('0')
    e_taco_mexicana_nv.set('0')
    e_potato_shots.set('0')

    e_pepper_bbq_chicken.set('0')
    e_chicken_delight.set('0')
    e_chicken_dominator.set('0')
    e_chicken_sausage.set('0')
    e_chicken_fiesta.set('0')
    e_chicken_tikka.set('0')
    e_chicken_mexican.set('0')
    e_tandoori_chicken.set('0')
    e_fantastic_four.set('0')

    textmargherita.config(state=DISABLED)
    textgoldencorn.config(state=DISABLED)
    textmixveg.config(state=DISABLED)
    textfarmhouse.config(state=DISABLED)
    textpaneerspecial.config(state=DISABLED)
    textsmokeypaneer.config(state=DISABLED)
    textsmokeyveg.config(state=DISABLED)
    textmexican.config(state=DISABLED)
    textparathapizza.config(state=DISABLED)

    textcoffee.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textfrench_fries.config(state=DISABLED)
    textstuffed_garlic_bread.config(state=DISABLED)
    textgarlic_bread.config(state=DISABLED)
    texttaco_mexicana_nv.config(state=DISABLED)
    texttaco_mexicana_veg.config(state=DISABLED)
    textcold_drinks.config(state=DISABLED)
    textcold_drinks.config(state=DISABLED)

    textchicken_delight.config(state=DISABLED)
    textchicken_dominator.config(state=DISABLED)
    textpepper_bbq_chicken.config(state=DISABLED)
    textchicken_sausage.config(state=DISABLED)
    textchicken_fiesta.config(state=DISABLED)
    textchicken_tikka.config(state=DISABLED)
    textchicken_mexican.config(state=DISABLED)
    texttandoori_chicken.config(state=DISABLED)
    textfantastic_four.config(state=DISABLED)

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
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costofvegpizzasvar.set('')
    costofnvpizzasvar.set('')
    subtotalvar.set('')
    GSTvar.set('')
    totalcostvar.set('')



def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='a94VecEO5LZFHgKdUWbrJfN61DpIPAwhQ3zs0MBRSyviY7l8tTZitdLkAOfcymHsC5K1uY9EvGp6h3al'
            url='https://www.fast2sms.com/dev/bulk-api'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')

        root2=Toplevel()

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')

        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
        numberLabel.pack(pady=5)

        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costofvegpizzasvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Veg Pizza: \t\t\t{priceofvegpizzas}Rs\n')
        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks/Sides:\t\t\t{priceofDrinks}Rs\n')
        if costofnvpizzasvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Non-veg Pizza\t\t\t{priceofnvpizzas}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE
                          ,command=send_msg)
        sendButton.pack(pady=5)
    
        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

def receipt():
    global billnumber,date
    if costofvegpizzasvar.get() != '' or costofnvpizzasvar.get() != '' or costofdrinksvar.get() != '':
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

        if e_paneerspecial.get() != '0':
            textReceipt.insert(END, f'Paneer Special:\t\t\t{int(e_paneerspecial.get()) * 140}\n\n')

        if e_smokeypaneer.get() != '0':
            textReceipt.insert(END, f'Smokey Paneer:\t\t\t{int(e_smokeypaneer.get()) * 150}\n\n')

        if e_smokeyveg.get() != '0':
            textReceipt.insert(END, f'Smokey veggie:\t\t\t{int(e_smokeyveg.get()) * 150}\n\n')

        if e_mexican.get() != '0':
            textReceipt.insert(END, f'Mexican :\t\t\t{int(e_mexican.get()) * 180}\n\n')

        if e_parathapizza.get() != '0':
            textReceipt.insert(END, f'paratha pizza:\t\t\t{int(e_parathapizza.get()) * 200}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_tea.get()) * 50}\n\n')

        if e_tea.get() != '0':
            textReceipt.insert(END, f'tea:\t\t\t{int(e_tea.get()) * 40}\n\n')

        if e_cold_drinks.get() != '0':
            textReceipt.insert(END, f'cold_drinks:\t\t\t{int(e_cold_drinks.get()) * 80}\n\n')

        if e_garlic_bread.get() != '0':
            textReceipt.insert(END, f'garlic_bread:\t\t\t{int(e_garlic_bread.get()) * 30}\n\n')

        if e_french_fries.get() != '0':
            textReceipt.insert(END, f'french_fries:\t\t\t{int(e_french_fries.get()) * 40}\n\n')

        if e_stuffed_garlic_bread.get() != '0':
            textReceipt.insert(END, f'stuffed_garlic_bread:\t\t\t{int(e_stuffed_garlic_bread.get()) * 60}\n\n')

        if e_taco_mexicana_veg.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_taco_mexicana_veg.get()) * 20}\n\n')

        if e_taco_mexicana_nv.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_taco_mexicana_nv.get()) * 50}\n\n')

        if e_potato_shots.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_potato_shots.get()) * 80}\n\n')

        if e_chicken_delight.get() != '0':
            textReceipt.insert(END, f'Chicken Delight:\t\t\t{int(e_chicken_delight.get()) * 400}\n\n')

        if e_chicken_dominator.get() != '0':
            textReceipt.insert(END, f'Chicken_Dominator:\t\t\t{int(e_chicken_dominator.get()) * 300}\n\n')

        if e_pepper_bbq_chicken.get() != '0':
            textReceipt.insert(END, f'Pepper BBq Chicken:\t\t\t{int(e_pepper_bbq_chicken.get()) * 500}\n\n')

        if e_chicken_fiesta.get() != '0':
            textReceipt.insert(END, f'Chicken Fiesta:\t\t\t{int(e_chicken_fiesta.get()) * 450}\n\n')

        if e_chicken_tikka.get() != '0':
            textReceipt.insert(END, f'Chicken Tikka:\t\t\t{int(e_chicken_tikka.get()) * 800}\n\n')

        if e_chicken_mexican.get() != '0':
            textReceipt.insert(END, f'Chicken Mexican:\t\t\t{int(e_chicken_mexican.get()) * 620}\n\n')

        if e_tandoori_chicken.get() != '0':
            textReceipt.insert(END, f'Tandoori Chicken:\t\t\t{int(e_tandoori_chicken.get()) * 700}\n\n')

        if e_fantastic_four.get() != '0':
            textReceipt.insert(END, f'Fantastic Four:\t\t\t{int(e_fantastic_four.get()) * 550}\n\n')

        if e_chicken_sausage.get() != '0':
            textReceipt.insert(END, f'Chicken Sausage:\t\t\t{int(e_chicken_sausage.get()) * 550}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costofvegpizzasvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Veg Pizza\t\t\t{priceofvegpizzas}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofnvpizzasvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Non-Veg Pizza\t\t\t{priceofnvpizzas}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'GST \t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofvegpizzas,priceofDrinks,priceofnvpizzas,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_margherita.get())
        item2=int(e_goldencorn.get())
        item3=int(e_mixveg.get())
        item4 = int(e_farmhouse.get())
        item5 = int(e_paneerspecial.get())
        item6 = int(e_smokeypaneer.get())
        item7 = int(e_smokeyveg.get())
        item8 = int(e_mexican.get())
        item9 = int(e_parathapizza.get())

        item10 = int(e_coffee.get())
        item11 = int(e_tea.get())
        item12 = int(e_cold_drinks.get())
        item13 = int(e_garlic_bread.get())
        item14 = int(e_french_fries.get())
        item15 = int(e_stuffed_garlic_bread.get())
        item16 = int(e_taco_mexicana_veg.get())
        item17 = int(e_taco_mexicana_nv.get())
        item18 = int(e_potato_shots.get())

        item19 = int(e_chicken_delight.get())
        item20 = int(e_chicken_dominator.get())
        item21 = int(e_pepper_bbq_chicken.get())
        item22 = int(e_chicken_sausage.get())
        item23 = int(e_chicken_fiesta.get())
        item24 = int(e_chicken_tikka.get())
        item25 = int(e_chicken_mexican.get())
        item26 = int(e_tandoori_chicken.get())
        item27 = int(e_fantastic_four.get())

        priceofvegpizzas=(item1*99)+(item2*99)+(item3*120)+(item4*130)+ (item5*140) + (item6 * 150) + (item7 * 150) \
                    + (item8 * 180) + (item9 * 200)

        priceofDrinks=(item10*30)+(item11*25)+ (item12 * 30) + (item13 * 99) + (item14 * 129) + (item15 * 79) \
                      + (item16 * 149) + (item17 * 189) + (item18 * 99)

        priceofnvpizzas=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

        costofvegpizzasvar.set(str(priceofvegpizzas)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        costofnvpizzasvar.set(str(priceofnvpizzas)+ ' Rs')

        subtotalofItems=priceofvegpizzas+priceofDrinks+priceofnvpizzas
        subtotalvar.set(str(subtotalofItems)+' Rs')

        GSTvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')



def margherita():
    if var1.get()==1:
        textmargherita.config(state=NORMAL)
        textmargherita.delete(0,END)
        textmargherita.focus()
    else:
        textmargherita.config(state=DISABLED)
        e_margherita.set('0')

def goldencorn():
    if var2.get()==1:
        textgoldencorn.config(state=NORMAL)
        textgoldencorn.delete(0,END)
        textgoldencorn.focus()

    else:
        textgoldencorn.config(state=DISABLED)
        e_goldencorn.set('0')

def mixveg():
    if var3.get()==1:
        textmixveg.config(state=NORMAL)
        textmixveg.delete(0,END)
        textmixveg.focus()

    else:
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


def paneerspecial():
    if var5.get() == 1:
        textpaneerspecial.config(state=NORMAL)
        textpaneerspecial.focus()
        textpaneerspecial.delete(0, END)
    elif var5.get() == 0:
        textpaneerspecial.config(state=DISABLED)
        e_paneerspecial.set('0')


def smokeypaneer():
    if var6.get() == 1:
        textsmokeypaneer.config(state=NORMAL)
        textsmokeypaneer.focus()
        textsmokeypaneer.delete(0, END)
    elif var6.get() == 0:
        textsmokeypaneer.config(state=DISABLED)
        e_smokeypaneer.set('0')


def smokeyveg():
    if var7.get() == 1:
        textsmokeyveg.config(state=NORMAL)
        textsmokeyveg.focus()
        textsmokeyveg.delete(0, END)
    elif var7.get() == 0:
        textsmokeyveg.config(state=DISABLED)
        e_smokeyveg.set('0')


def mexican():
    if var8.get() == 1:
        textmexican.config(state=NORMAL)
        textmexican.focus()
        textmexican.delete(0, END)
    elif var8.get() == 0:
        textmexican.config(state=DISABLED)
        e_mexican.set('0')


def parathapizza():
    if var9.get() == 1:
        textparathapizza.config(state=NORMAL)
        textparathapizza.focus()
        textparathapizza.delete(0, END)
    elif var9.get() == 0:
        textparathapizza.config(state=DISABLED)
        e_parathapizza.set('0')


def coffee():
    if var10.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var10.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def tea():
    if var11.get() == 1:
        texttea.config(state=NORMAL)
        texttea.focus()
        texttea.delete(0, END)
    elif var11.get() == 0:
        texttea.config(state=DISABLED)
        e_tea.set('0')


def cold_drinks():
    if var12.get() == 1:
        textcold_drinks.config(state=NORMAL)
        textcold_drinks.focus()
        textcold_drinks.delete(0, END)
    elif var12.get() == 0:
        textcold_drinks.config(state=DISABLED)
        e_cold_drinks.set('0')


def garlic_bread():
    if var13.get() == 1:
        textgarlic_bread.config(state=NORMAL)
        textgarlic_bread.focus()
        textgarlic_bread.delete(0, END)
    elif var13.get() == 0:
        textgarlic_bread.config(state=DISABLED)
        e_garlic_bread.set('0')


def french_fries():
    if var14.get() == 1:
        textfrench_fries.config(state=NORMAL)
        textfrench_fries.focus()
        textfrench_fries.delete(0, END)
    elif var14.get() == 0:
        textfrench_fries.config(state=DISABLED)
        e_french_fries.set('0')


def stuffed_garlic_bread():
    if var15.get() == 1:
        textstuffed_garlic_bread.config(state=NORMAL)
        textstuffed_garlic_bread.focus()
        textstuffed_garlic_bread.delete(0, END)
    elif var15.get() == 0:
        textstuffed_garlic_bread.config(state=DISABLED)
        e_stuffed_garlic_bread.set('0')


def taco_mexicana_veg():
    if var16.get() == 1:
        texttaco_mexicana_veg.config(state=NORMAL)
        texttaco_mexicana_veg.focus()
        texttaco_mexicana_veg.delete(0, END)
    elif var16.get() == 0:
        texttaco_mexicana_veg.config(state=DISABLED)
        e_taco_mexicana_veg.set('0')


def taco_mexicana_nv():
    if var17.get() == 1:
        texttaco_mexicana_nv.config(state=NORMAL)
        texttaco_mexicana_nv.focus()
        texttaco_mexicana_nv.delete(0, END)
    elif var17.get() == 0:
        texttaco_mexicana_nv.config(state=DISABLED)
        e_taco_mexicana_nv.set('0')


def potato_shots():
    if var18.get() == 1:
        textpotato_shots.config(state=NORMAL)
        textpotato_shots.focus()
        textpotato_shots.delete(0, END)
    elif var18.get() == 0:
        textpotato_shots.config(state=DISABLED)
        e_potato_shots.set('0')


def chicken_delight():
    if var19.get() == 1:
        textchicken_delight.config(state=NORMAL)
        textchicken_delight.focus()
        textchicken_delight.delete(0, END)
    elif var19.get() == 0:
        textchicken_delight.config(state=DISABLED)
        e_chicken_delight.set('0')


def chicken_dominator():
    if var20.get() == 1:
        textchicken_dominator.config(state=NORMAL)
        textchicken_dominator.focus()
        textchicken_dominator.delete(0, END)
    elif var20.get() == 0:
        textchicken_dominator.config(state=DISABLED)
        e_chicken_dominator.set('0')


def pepper_bbq_chicken():
    if var21.get() == 1:
        textpepper_bbq_chicken.config(state=NORMAL)
        textpepper_bbq_chicken.focus()
        textpepper_bbq_chicken.delete(0, END)
    elif var21.get() == 0:
        textpepper_bbq_chicken.config(state=DISABLED)
        e_pepper_bbq_chicken.set('0')


def chicken_sausage():
    if var22.get() == 1:
        textchicken_sausage.config(state=NORMAL)
        textchicken_sausage.focus()
        textchicken_sausage.delete(0, END)
    elif var22.get() == 0:
        textchicken_sausage.config(state=DISABLED)
        e_chicken_sausage.set('0')


def chicken_fiesta():
    if var23.get() == 1:
        textchicken_fiesta.config(state=NORMAL)
        textchicken_fiesta.focus()
        textchicken_fiesta.delete(0, END)
    elif var23.get() == 0:
        textchicken_fiesta.config(state=DISABLED)
        e_chicken_fiesta.set('0')


def chicken_tikka():
    if var24.get() == 1:
        textchicken_tikka.config(state=NORMAL)
        textchicken_tikka.focus()
        textchicken_tikka.delete(0, END)
    elif var24.get() == 0:
        textchicken_tikka.config(state=DISABLED)
        e_chicken_tikka.set('0')


def chicken_mexican():
    if var25.get() == 1:
        textchicken_mexican.config(state=NORMAL)
        textchicken_mexican.focus()
        textchicken_mexican.delete(0, END)
    elif var25.get() == 0:
        textchicken_mexican.config(state=DISABLED)
        e_chicken_mexican.set('0')


def tandoori_chicken():
    if var26.get() == 1:
        texttandoori_chicken.config(state=NORMAL)
        texttandoori_chicken.focus()
        texttandoori_chicken.delete(0, END)
    elif var26.get() == 0:
        texttandoori_chicken.config(state=DISABLED)
        e_tandoori_chicken.set('0')


def fantastic_four():
    if var27.get() == 1:
        textfantastic_four.config(state=NORMAL)
        textfantastic_four.focus()
        textfantastic_four.delete(0, END)
    elif var27.get() == 0:
        textfantastic_four.config(state=DISABLED)
        e_fantastic_four.set('0')



root=Tk()

root.geometry('1545x785+0+0')

root.resizable(0,0)

root.title('Pizza Order Management System ')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Pizza Order Management System',font=('arial',30,'bold'),fg='red',bd=9,
                 bg='gold',width=51)
labelTitle.grid(row=0,column=0)

#frames

nonvegmenuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
nonvegmenuFrame.pack(side=LEFT)

costFrame=Frame(nonvegmenuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(nonvegmenuFrame,text='Veg-Pizzas',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(nonvegmenuFrame,text='Breverages and Sides',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(nonvegmenuFrame,text='Non-veg-Pizzas',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
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
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_margherita=StringVar()
e_goldencorn=StringVar()
e_mixveg= StringVar()
e_farmhouse = StringVar()
e_paneerspecial = StringVar()
e_smokeypaneer= StringVar()
e_smokeyveg= StringVar()
e_mexican = StringVar()
e_parathapizza= StringVar()

e_coffee=StringVar()
e_tea = StringVar()
e_cold_drinks = StringVar()
e_garlic_bread = StringVar()
e_stuffed_garlic_bread = StringVar()
e_french_fries = StringVar()
e_taco_mexicana_veg = StringVar()
e_taco_mexicana_nv = StringVar()
e_potato_shots = StringVar()

e_chicken_delight=StringVar()
e_pepper_bbq_chicken = StringVar()
e_chicken_sausage = StringVar()
e_chicken_dominator = StringVar()
e_fantastic_four = StringVar()
e_chicken_fiesta = StringVar()
e_chicken_tikka = StringVar()
e_chicken_mexican = StringVar()
e_tandoori_chicken = StringVar()

costofvegpizzasvar=StringVar()
costofdrinksvar=StringVar()
costofnvpizzasvar=StringVar()
subtotalvar=StringVar()
GSTvar=StringVar()
totalcostvar=StringVar()

e_margherita.set('0')
e_goldencorn.set('0')
e_mixveg.set('0')
e_farmhouse.set('0')
e_paneerspecial.set('0')
e_smokeypaneer.set('0')
e_smokeyveg.set('0')
e_mexican.set('0')
e_parathapizza.set('0')

e_coffee.set('0')
e_tea.set('0')
e_cold_drinks.set('0')
e_stuffed_garlic_bread.set('0')
e_garlic_bread.set('0')
e_french_fries.set('0')
e_taco_mexicana_veg.set('0')
e_taco_mexicana_nv.set('0')
e_potato_shots.set('0')

e_pepper_bbq_chicken.set('0')
e_chicken_fiesta.set('0')
e_chicken_mexican.set('0')
e_chicken_dominator.set('0')
e_tandoori_chicken.set('0')
e_chicken_delight.set('0')
e_fantastic_four.set('0')
e_chicken_tikka.set('0')
e_chicken_sausage.set('0')

#--------------------------Veg Pizza------------------------

margherita=Checkbutton(foodFrame,text='Margherita',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=margherita)
margherita.grid(row=0,column=0,sticky=W)

goldencorn=Checkbutton(foodFrame,text='Golden Corn',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=goldencorn)
goldencorn.grid(row=1,column=0,sticky=W)

mixveg=Checkbutton(foodFrame,text='Mix-Veg-Delight',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=mixveg)
mixveg.grid(row=2,column=0,sticky=W)

farmhouse=Checkbutton(foodFrame,text='Farmhouse',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=farmhouse)
farmhouse.grid(row=3,column=0,sticky=W)

paneerspecial=Checkbutton(foodFrame,text='Paneer Special',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=paneerspecial)
paneerspecial.grid(row=4,column=0,sticky=W)

smokeypaneer=Checkbutton(foodFrame,text='Smokey Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=smokeypaneer)
smokeypaneer.grid(row=5,column=0,sticky=W)

smokeyveg=Checkbutton(foodFrame,text='Smokey Vegies',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=smokeyveg)
smokeyveg.grid(row=6,column=0,sticky=W)

mexican=Checkbutton(foodFrame,text='Mexican Platter',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=mexican)
mexican.grid(row=7,column=0,sticky=W)

parathapizza=Checkbutton(foodFrame,text='Paratha Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                    ,command=parathapizza)
parathapizza.grid(row=8,column=0,sticky=W)

#Entry Fields for Veg Pizza Items

textmargherita=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_margherita)
textmargherita.grid(row=0,column=1)

textgoldencorn=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_goldencorn)
textgoldencorn.grid(row=1,column=1)

textmixveg=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mixveg)
textmixveg.grid(row=2,column=1)

textfarmhouse = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_farmhouse)
textfarmhouse.grid(row=3, column=1)

textpaneerspecial = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneerspecial)
textpaneerspecial.grid(row=4, column=1)

textsmokeypaneer = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_smokeypaneer)
textsmokeypaneer.grid(row=5, column=1)

textsmokeyveg = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_smokeyveg)
textsmokeyveg.grid(row=6, column=1)

textmexican= Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mexican)
textmexican.grid(row=7, column=1)

textparathapizza = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_parathapizza)
textparathapizza.grid(row=8, column=1)

#----------------------------------Drinks------------------------------------

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=coffee)
coffee.grid(row=0,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=tea)
tea.grid(row=1,column=0,sticky=W)

cold_drinks=Checkbutton(drinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=cold_drinks)
cold_drinks.grid(row=2,column=0,sticky=W)

garlic_bread=Checkbutton(drinksFrame,text='Garlic Bread',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=garlic_bread)
garlic_bread.grid(row=3,column=0,sticky=W)

french_fries=Checkbutton(drinksFrame,text='French Fries',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                     ,command=french_fries)
french_fries.grid(row=4,column=0,sticky=W)

stuffed_garlic_bread=Checkbutton(drinksFrame,text='Stuffed Garlic Bread',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                     ,command=stuffed_garlic_bread)
stuffed_garlic_bread.grid(row=5,column=0,sticky=W)

taco_mexicana_veg=Checkbutton(drinksFrame,text='Taco-Mexicana(V)',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                      ,command=taco_mexicana_veg)
taco_mexicana_veg.grid(row=6,column=0,sticky=W)

taco_mexicana_nv=Checkbutton(drinksFrame,text='Taco-Mexicana(NV)',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                      ,command=taco_mexicana_nv)
taco_mexicana_nv.grid(row=7,column=0,sticky=W)

potato_shots=Checkbutton(drinksFrame,text='Potato Shots',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                       ,command=potato_shots)
potato_shots.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=0, column=1)

texttea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tea)
texttea.grid(row=1, column=1)

textcold_drinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cold_drinks)
textcold_drinks.grid(row=2, column=1)

textgarlic_bread = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_garlic_bread)
textgarlic_bread.grid(row=3, column=1)

textfrench_fries = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_french_fries)
textfrench_fries.grid(row=4, column=1)

textstuffed_garlic_bread = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_stuffed_garlic_bread)
textstuffed_garlic_bread.grid(row=5, column=1)

texttaco_mexicana_veg = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_taco_mexicana_veg)
texttaco_mexicana_veg.grid(row=6, column=1)

texttaco_mexicana_nv = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_taco_mexicana_nv)
texttaco_mexicana_nv.grid(row=7, column=1)

textpotato_shots = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_potato_shots)
textpotato_shots.grid(row=8, column=1)

#---------------------------------------------Non-Veg Pizza-----------------------------

chicken_delightcake=Checkbutton(cakesFrame,text='Chicken Delight',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=chicken_delight)
chicken_delightcake.grid(row=0,column=0,sticky=W)

chicken_dominatorcake=Checkbutton(cakesFrame,text='Chicken Dominator',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=chicken_dominator)
chicken_dominatorcake.grid(row=1,column=0,sticky=W)

pepper_bbq_chickencake=Checkbutton(cakesFrame,text='Pepper BBQ Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=pepper_bbq_chicken)
pepper_bbq_chickencake.grid(row=2,column=0,sticky=W)

chicken_sausagecake=Checkbutton(cakesFrame,text='Chicken Sausage',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=chicken_sausage)
chicken_sausagecake.grid(row=3,column=0,sticky=W)

chicken_fiestacake=Checkbutton(cakesFrame,text='Chicken Fiesta',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=chicken_fiesta)
chicken_fiestacake.grid(row=4,column=0,sticky=W)

chicken_tikkacake=Checkbutton(cakesFrame,text='Chicken Tikka',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=chicken_tikka)
chicken_tikkacake.grid(row=5,column=0,sticky=W)

chicken_mexicancake=Checkbutton(cakesFrame,text='Chicken Mexican',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=chicken_mexican)
chicken_mexicancake.grid(row=6,column=0,sticky=W)

tandoori_chickencake=Checkbutton(cakesFrame,text='Tandoori Thicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=tandoori_chicken)
tandoori_chickencake.grid(row=7,column=0,sticky=W)

fantastic_fourcake=Checkbutton(cakesFrame,text='Fantastic Four',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=fantastic_four)
fantastic_fourcake.grid(row=8,column=0,sticky=W)

#entry fields for Non-Veg Pizza

textchicken_delight = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_delight)
textchicken_delight.grid(row=0, column=1)

textchicken_dominator = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_dominator)
textchicken_dominator.grid(row=1, column=1)

textpepper_bbq_chicken = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pepper_bbq_chicken)
textpepper_bbq_chicken.grid(row=2, column=1)

textchicken_sausage = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_sausage)
textchicken_sausage.grid(row=3, column=1)

textchicken_fiesta = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_fiesta)
textchicken_fiesta.grid(row=4, column=1)

textchicken_tikka = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_tikka)
textchicken_tikka.grid(row=5, column=1)

textchicken_mexican = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken_mexican)
textchicken_mexican.grid(row=6, column=1)

texttandoori_chicken = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tandoori_chicken)
texttandoori_chicken.grid(row=7, column=1)

textfantastic_four = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_fantastic_four)
textfantastic_four.grid(row=8, column=1)

#costlabels & entry fields

labelCostofvegpizzas=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofvegpizzas.grid(row=0,column=0)

textCostofvegpizzas=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofvegpizzasvar)
textCostofvegpizzas.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelcostofnvpizzas=Label(costFrame,text='Cost of Non-Veg Pizza',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelcostofnvpizzas.grid(row=2,column=0)

textcostofnvpizzas=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofnvpizzasvar)
textcostofnvpizzas.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelGST=Label(costFrame,text='GST',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelGST.grid(row=1,column=2)

textGST=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=GSTvar)
textGST.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()