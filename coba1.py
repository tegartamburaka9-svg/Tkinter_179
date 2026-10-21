import tkinter as tk
import tkinter.messagebox as msg
top = tk.Tk()
def helloCallBack():
    msg.showinfo("Hello Python!", "tailaso kau nabule")

w = tk.Button(top, text="Hello", command=helloCallBack)
w.pack()
top.mainloop()