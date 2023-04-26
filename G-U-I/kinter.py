from tkinter import *

s = Tk()
s.geometry('400x300')
s.resizable(False,False)
s.title('sample')
s.configure(background='green')




en = Entry(s,width=30)
en.pack(side=BOTTOM)

# 


def add():
    l = Label(s,text='welcome',bg='yellow',fg='black')
    l.pack(fill='both',pady=10)

b = Button(s,text='click here',bg='red',fg='white',command=add).place(x=20,y=150)
# b.pack(fill='none')

s.mainloop()