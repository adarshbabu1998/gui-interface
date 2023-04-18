import tkinter
r=tkinter.Tk()
w=tkinter.Label(r,text="hello",bg="yellow",fg="blue").pack(fill="x",pady=10)

tkinter.Label(r,text="world",bg="blue",fg="red").pack(fill="x",pady=10)
r.mainloop()