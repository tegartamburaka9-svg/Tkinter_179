import tkinter as tk

m1 = tk.PanedWindow(orient=tk.HORIZONTAL)
m1.pack(fill=tk.BOTH, expand=1)

left = tk.Label(m1, text="left pane")
m1.add(left)

m2 = tk.PanedWindow(m1, orient=tk.VERTICAL)
m1.add(m2)

top = tk.Label(m2, text="top pane")
m2.add(top)

bottom = tk.Label(m2, text="bottom pane")
m2.add(bottom)

tk.mainloop()
