from tkinter import*
d=Tk()
d.geometry('300x200')
d.resizable(True,False)
d.title('SAMPLE')
d.configure(background='black')

s=Label(d,text='LOGINFORM',bg='black',fg='red')
s.pack()
r=Label(d,text='name',bg='black',fg='white',padx=5)
r.place(x=60,y=30)

en = Entry(d,width=20)
en.place(x=120,y=30)


m=Label(d,text='password',bg='black',fg='white',padx=3)
m.place(x=60,y=60)

g = Entry(d,width=20)
g.place(x=120,y=60)




def display():
    uname_l = Label(d,text=en.get(),bg='black',fg='red')
    upass_l=Label(d,text=g.get(),bg='black',fg='red')
    uname_l.place(x=120,y=150,)
    upass_l.place(x=120,y=170)

b = Button(d,text='submit',bg='black',fg='red',command=display).place(x=120,y=100)
d.mainloop()