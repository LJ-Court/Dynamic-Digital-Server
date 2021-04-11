from tkinter import *
from tkinter import ttk
import os

class DynamicDigital:

    def __init__(self, root):

        root.title("Dynamic Digital Server Tools")

        baseframe = ttk.Frame(root, padding="3 3 12 12")
        baseframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        username_label = ttk.Label(baseframe, text="Enter Username: ")
        username_label.grid(column=1, row=1, sticky=(W, E))

        self.username = StringVar()
        username_entry = ttk.Entry(baseframe, width=20, textvariable=self.username)
        username_entry.grid(column=2, row=1, sticky=(W, E))

        serveraddress_label = ttk.Label(baseframe, text="Enter Server Address: ")
        serveraddress_label.grid(column=1, row=2, sticky=(W, E))

        self.serveraddress = StringVar()
        serveraddress_entry = ttk.Entry(baseframe, width=20, textvariable=self.serveraddress)
        serveraddress_entry.grid(column=2, row=2, sticky=(W, E))

        downloadaddress_label = ttk.Label(baseframe, text="Enter Download Address: ")
        downloadaddress_label.grid(column=1, row=3, sticky=(W, E))

        self.downloadaddress = StringVar()
        downloadaddress_entry = ttk.Entry(baseframe, width=20, textvariable=self.downloadaddress)
        downloadaddress_entry.grid(column=2, row=3, sticky=(W, E))

        startdownload = ttk.Button(baseframe, text="Start Download On Server", command=self.download)
        startdownload.grid(column=2, row=4, sticky=(W, E))

        for child in baseframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def download(self, *args):
        usedownloadaddress = self.downloadaddress.get()
        useserveraddress = self.serveraddress.get()
        useUserName = self.username.get()
        os.popen("ssh " + useUserName + "@" + useserveraddress + " wget " + usedownloadaddress)

root = Tk()
DynamicDigital(root)
root.mainloop()