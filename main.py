from tkinter import *
import func

# ====================  windows  =======================
window = Tk()
window.title("book store")
window.geometry("490x280")
window.resizable(width=False,height=False)
color='#e0e0e0'
window.config(bg=color)
# ====================  static function  =======================
def clear_list():
    list1.delete(0,END)

def fill_list(books):
    for book in books:
        list1.insert(END,book)

# ====================  Label  =======================

l1 = Label(window, text=' Name',bd='3',anchor=CENTER,font=('B Tir',10,'bold'),width='5',height='1',bg='#00a2ff',padx='8',pady='1',relief=RAISED)
#l1.grid(row=0, column=0,padx='10',pady='5')
l1.place(x=10,y=10)

l2 = Label(window, text=' Family',anchor=CENTER,font=('B Tir',10,'bold'),bd='3',width='5',height='1',bg='#00a2ff',padx='8',pady='1',relief=RAISED)
#l2.grid(row=1, column=0,padx='10',pady='5')
l2.place(x=10,y=50)

l3 = Label(window, text=' Number',anchor=CENTER,font=('B Tir',10,'bold'),bd='3',width='5',height='1',bg='#00a2ff',padx='8',pady='1', relief=RAISED)
##l3.grid(row=2, column=0,padx='10',pady='5')
l3.place(x=10,y=90)


# ====================  Entry  =======================
name_text = StringVar()
e1 = Entry(window, textvariable=name_text,bd='4',font=('mitra',10,'bold'),width='15')
#e1.grid(row=0, column=1)
e1.place(x=90,y=12)

family_text = StringVar()
e2 = Entry(window, textvariable=family_text,bd='4',font=('mitra',10,'bold'),width='15')
#e2.grid(row=1, column=1)
e2.place(x=90,y=52)

number_text = StringVar()
e3 = Entry(window, textvariable=number_text,bd='4',font=('mitra',10,'bold'),width='15')
#e3.grid(row=2, column=1)
e3.place(x=90,y=92)



# =============  ListBox and Scrollbar  ================
list1 = Listbox(window, width=34, height=10,activestyle='dotbox',font=('mitra',10,'bold'),highlightcolor='red',relief=RAISED)
#list1.grid(row=1, column=2, rowspan=5, columnspan=2,pady='10',padx='20')
list1.place(x=220,y=50)

sb1 = Scrollbar(window,width='20')
#sb1.place(x=470,y=100)
sb1.pack(side=RIGHT,fill='both')



list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def get_selected_row(event):
    global select_book
    if len(list1.curselection()) >0:
        index=list1.curselection()[0]
        select_book=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,select_book[1])
        e2.delete(0,END)
        e2.insert(END,select_book[2])
        e3.delete(0,END)
        e3.insert(END,select_book[3])
      
    
list1.bind("<<ListboxSelect>>",get_selected_row)

# =======================================  Button  ======================================
#================  View All  ==============
def view_command():
    clear_list()
    books=func.view()
    fill_list(books)

btn1 = Button(window, text="View All",font=('mitra',10,'bold'), width=28,command=lambda:view_command(),bd='5',height='1',bg='#09a93a',activebackground='#d8cc0f')
btn1.place(x=220,y=10)


#================  Search Entry  ==============
def search_command():
    clear_list()
    books=func.search(name_text.get(),family_text.get(),number_text.get())
    fill_list(books)

btn2 = Button(window, text="Search Entry", width=19,command=lambda:search_command(),font=('mitra',10,'bold'),bd='5',height='1',bg='#09a93a',activebackground='#d8cc0f',pady='3')

btn2.place(x=10,y=185)

#================  Add Entry  ==============
def add_command():
    func.insert(name_text.get(),family_text.get(),number_text.get())
    view_command()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
   

btn3 = Button(window, text="Add", width=8,command=add_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#09a93a',activebackground='#d8cc0f',pady='3')
#btn3.grid(row=15, column=3)
btn3.place(x=100,y=140)

#================  Update Selected  ==============
def update_command():
    func.update(select_book[0],name_text.get(),family_text.get(),number_text.get())
    view_command()

btn4 = Button(window, text="Update", width=19,command=update_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#09a93a',activebackground='#d8cc0f',pady='3')

btn4.place(x=10,y=230)


#================  Delet Selected  ==============
def delete_command():
    func.delet(select_book[0])
    view_command()
btn5 = Button(window, text="Delete", width=8,command=delete_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#09a93a',activebackground='#d8cc0f',pady='3')

btn5.place(x=10,y=140)

#================  Close  ==============
def close_command():
    window.destroy()

btn6 = Button(window, text="Close", width=7,command=close_command,font=('mitra',10,'bold'),bd='5',height='1',bg='#bd0009',activebackground='#d8cc0f',pady='3')
btn6.place(x=385,y=230)



window.mainloop()
