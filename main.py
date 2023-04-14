import tkinter as tk
from tkinter import filedialog
from scanner import scanner

class MCreatorScanner():

    def __init__(self) -> None:
        self.padding = 20

        self.root = tk.Tk()
        self.root.title('MCreator Mod Scanner')
        self.root.geometry('400x200')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.modpath = tk.StringVar()
        self.modpath.set('No path selected')

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.button = tk.Button(self.root,
            text="Select mods/ folder", command=self.get_modpath)
        self.button.grid(row=0, column=0, pady=self.padding)

        self.label = tk.Label(self.root, text=self.modpath.get())
        self.label.grid(row=1, column=0, pady=self.padding)

        self.root.mainloop()

    def get_modpath(self):
        directory = filedialog.askdirectory()
        if not directory:
            return
        self.modpath.set(directory)
        self.label.config(text=f"Scanning mod folder:\n{self.modpath.get()}")
        self.label.config(text=scanner(self.modpath.get()))

MCreatorScanner()
