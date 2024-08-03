from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Billing Management System')
root.geometry('1280x720')
bg_color = '#bb8fce'

# Variables
bread = IntVar()
Tea = IntVar()
Milk = IntVar()
coffee = IntVar()
total_items = IntVar()
cb = StringVar()
cT = StringVar()
cm = StringVar()
cc = StringVar()
total_cost = StringVar()

# Functions
def calculate_total():
    if bread.get() == 0 and Tea.get() == 0 and Milk.get() == 0 and coffee.get() == 0:
        messagebox.showerror('Error', 'Please select number of quantities.')
    else:
        b = bread.get()
        T = Tea.get()
        M = Milk.get()
        c = coffee.get()

        t = float(b * 5 + T * 10 + M * 10 + c * 15)
        total_items.set(b + T + M + c)
        total_cost.set('${:.2f}'.format(t))

        cb.set('${:.2f}'.format(b * 5))
        cT.set('${:.2f}'.format(T * 10))
        cm.set('${:.2f}'.format(M * 10))
        cc.set('${:.2f}'.format(c * 15))


def reset_values():
    bread.set(0)
    Tea.set(0)
    Milk.set(0)
    coffee.set(0)
    cb.set('')
    cT.set('')
    cm.set('')
    cc.set('')
    total_items.set(0)
    total_cost.set('')
    textarea.delete(1.0, END)

def print_receipt():
    messagebox.showinfo('Print', 'Printing functionality will be implemented in future versions.')

# GUI Layout
title = Label(root, text='Billing Management System', bg=bg_color, fg='white', font=('times new roman', 35, 'bold'),
              relief=GROOVE, bd=12)
title.pack(fill=X)

# Product Details Frame
F1 = LabelFrame(root, text='Product Details', font=('times new roman', 18, 'bold'), fg='gold', bg=bg_color,
                relief=RIDGE, bd=15)
F1.place(x=5, y=90, width=800, height=500)

Label(F1, text='Items', font=('times new roman', 25, 'bold', 'underline'), fg='black').grid(row=0, column=0, padx=20, pady=15)
Label(F1, text='No of Items', font=('times new roman', 25, 'bold', 'underline'), fg='black').grid(row=0, column=1, padx=20,
                                                                                           pady=15)
Label(F1, text='Cost of Items', font=('times new roman', 25, 'bold', 'underline'), fg='black').grid(row=0, column=2, padx=20,
                                                                                              pady=15)

Label(F1, text='Bread', font=('times new roman', 28, 'bold'), fg='lawngreen', bg=bg_color).grid(row=1, column=0,
                                                                                                padx=20, pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=bread).grid(row=1, column=1, padx=20,
                                                                                                pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cb).grid(row=1, column=2, padx=20,
                                                                                            pady=15)

Label(F1, text='Tea', font=('times new roman', 28, 'bold'), fg='lawngreen', bg=bg_color).grid(row=2, column=0,
                                                                                              padx=20, pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=Tea).grid(row=2, column=1, padx=20,
                                                                                              pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cT).grid(row=2, column=2, padx=20,
                                                                                          pady=15)

Label(F1, text='Milk', font=('times new roman', 28, 'bold'), fg='lawngreen', bg=bg_color).grid(row=3, column=0,
                                                                                               padx=20, pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=Milk).grid(row=3, column=1, padx=20,
                                                                                               pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cm).grid(row=3, column=2, padx=20,
                                                                                           pady=15)

Label(F1, text='Coffee', font=('times new roman', 28, 'bold'), fg='lawngreen', bg=bg_color).grid(row=4, column=0,
                                                                                                 padx=20, pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=coffee).grid(row=4, column=1, padx=20,
                                                                                                 pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=cc).grid(row=4, column=2, padx=20,
                                                                                             pady=15)

Label(F1, text='Total Price', font=('times new roman', 28, 'bold'), fg='lawngreen', bg=bg_color).grid(row=5, column=0,
                                                                                                     padx=20, pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=total_items).grid(row=5, column=1,
                                                                                                     padx=20, pady=15)
Entry(F1, font='arial 15 bold', relief=SUNKEN, bd=7, justify=CENTER, textvariable=total_cost).grid(row=5, column=2,
                                                                                                  padx=20, pady=15)

# Bill Area
F2 = Frame(root, relief=GROOVE, bd=10)
F2.place(x=820, y=90, width=430, height=500)

Label(F2, text='Receipt', font='arial 15 bold', bd=7, relief=GROOVE).pack()
scrol = Scrollbar(F2, orient=VERTICAL)
scrol.pack(side=RIGHT, fill=Y)
textarea = Text(F2, font='arial 15 bold', yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

# Buttons
F3 = Frame(root, relief=GROOVE, bd=10)
F3.place(x=5, y=590, width=1270, height=120)

Button(F3, text='Total', font='arial 25 bold', bg='yellow', fg='crimson', padx=5, pady=5, width=10,
       command=calculate_total).grid(row=0, column=0, padx=10, pady=10)

Button(F3, text='Receipt', font='arial 25 bold', bg='yellow', fg='crimson', padx=5, pady=5, width=10,
       command=generate_receipt).grid(row=0, column=1, padx=10, pady=10)

Button(F3, text='Reset', font='arial 25 bold', bg='yellow', fg='crimson', padx=5, pady=5, width=10,
       command=reset_values).grid(row=0, column=3, padx=10, pady=10)

Button(F3, text='Exit', font='arial 25 bold', bg='yellow', fg='crimson', padx=5, pady=5, width=10,
       command=root.destroy).grid(row=0, column=4, padx=10, pady=10)

root.mainloop()
