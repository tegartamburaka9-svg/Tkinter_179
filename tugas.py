import tkinter as tk
root = tk.Tk()
root.title("Contoh Tk")
root.mainloop()

import tkinter as tk
root = tk.Tk()
btn = tk.Button(root, text="Klik Saya", command=lambda: print("Tombol diklik!"))
btn.pack()
root.mainloop()

import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.create_oval(50, 50, 150, 150, fill="blue")
canvas.pack()
root.mainloop()