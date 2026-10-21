import tkinter as tk
root = tk.Tk()
root.title("Contoh Tk")
root.mainloop()

import tkinter as tk
root = tk.Tk()
btn = tk.Button(root, text="Klik Saya", command=lambda: print("Tombol diklik!"))
btn.pack()
root.mainloop()