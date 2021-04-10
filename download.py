import tkinter as tk

colourpalette: list = ["#005BE8", "#009EF2", "#0BCADB", "#00F2C3", "#00E879"]

l1 = tk.Label(text="Enter Download Link: ", bg=colourpalette[0])
e1 = tk.Entry()
l2 = tk.Label(text="Enter Server Address: ", bg=colourpalette[0])
e2 = tk.Entry()
l1.pack()
e1.pack()
l2.pack()
e2.pack()
tk.mainloop()
