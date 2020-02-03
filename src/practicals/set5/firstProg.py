import tkinter


class MyClass(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.btn = tkinter.Button(self, text='PUSH', command=self.buttonCmd)
        self.btn.grid(row=0, column=0, sticky='nwes')
        self.lbl = tkinter.Label(self, text='Hello')
        self.lbl.grid(row=0, column=1, sticky='nwes')
        self.lbl.grid_forget()

    def buttonCmd(self, *args, **kwargs):
        self.lbl.grid()


root = tkinter.Tk()
MyFrame = MyClass(root)
MyFrame.pack(expand='true', fill='both')
root.mainloop()
