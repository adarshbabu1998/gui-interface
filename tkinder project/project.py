from tkinter import*
d=Tk()
d.geometry('500x500')
d.resizable(True,False)
d.title(' ')
d.configure(background='grey')

heading1=Label(d,text='STUDENT MARK SHEETS',bg='grey',fg='black',font=('Arial bold',18))
heading1.place(x=0)
heading2=Label(d,text='NAME:',bg='grey',fg='black',)
heading2.place(x=0,y=55)
name_entry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='black')
name_entry.place(x=40,y=55)


heading3=Label(d,text='ENROLL NO:',bg='grey',fg='black')
heading3.place(x=200,y=55)
enroll_entry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='black')
enroll_entry.place(x=270,y=55)

sub_heading1=Label(d,text='SUBJECTS',bg='brown',fg='white',font=('arial bold',10),width=30,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
sub_heading1.place(x=10,y=100)
sub_heading2=Label(d,text='MARKS',bg='brown',fg='white',font=('arial bold',10),width=20,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
sub_heading2.place(x=200,y=100)
sub_heading3=Label(d,text='GRADE',bg='brown',fg='white',font=('arial bold',10),width=15,
                   borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
sub_heading3.place(x=350,y=100)

subject1=Label(d,text='ENGLISH',bg='GREY',fg='BLACK',font=('arial bold',8))
subject1.place(x=100,y=130)
subjectentry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
subjectentry.place(x=250,y=130,)
subjectgrade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
subjectgrade.place(x=380,y=130)


hindi=Label(d,text='HINDI',bg='GREY',fg='BLACK',font=('arial bold',8))
hindi.place(x=100,y=150)
hindi_ent=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
hindi_ent.place(x=250,y=150)
hind_grade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
hind_grade.place(x=380,y=150)

science=Label(d,text='SCIENCE',bg='GREY',fg='BLACK',font=('arial bold',8))
science.place(x=100,y=170)
science_entry=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
science_entry.place(x=250,y=170)
science_grade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
science_grade.place(x=380,y=170)


maths=Label(d,text='MATHS',bg='GREY',fg='BLACK',font=('arial bold',8))
maths.place(x=100,y=190)
math_ent=Entry(d,width=20,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
math_ent.place(x=250,y=190)
math_grade=Entry(d,width=10,borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='red')
math_grade.place(x=380,y=190)

b = Button(d,text='SUBMIT',bg='blue',fg='white') 
b.place(x=430,y=470)







d.mainloop()