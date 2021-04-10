import tkinter as tk

colourpalette: list = ["#005BE8", "#009EF2", "#0BCADB", "#00F2C3", "#00E879"]

def exceute_download_section():
    with open("download.py", "r", encoding="utf-8") as file:
        exec(file.read())

app = tk.Tk()
app.geometry("300x400")
app.configure(bg=colourpalette[0])
b1 = tk.Button(text="Download", command=exceute_download_section)
b1.pack()
tk.mainloop()
