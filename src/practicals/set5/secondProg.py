from tkinter import *

root = Tk()


def grey(*args, **kwargs):
    root.configure(backgroud='grey')


def bthing():
    root.configure(background='red')


def bthing1():
    root.configure(background='green')


def bthing2():
    root.configure(background='blue')
    root.after(1000, grey)


Button(text='RED', command=bthing).pack()
Button(text='GREEN', command=bthing1).pack()
Button(text='BLUE', command=bthing2).pack()

root.configure(background='grey')
root.geometry("400x400")

root.mainloop()