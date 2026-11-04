# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("520x380")

        self.label1 = tk.Label(root, text="Label")
        self.label1.place(x=80, y=50, width=90, height=30)

        self.text1 = tk.Text(root)
        self.text1.place(x=170, y=50, width=220, height=30)

        self.text2 = tk.Text(root)
        self.text2.place(x=170, y=100, width=220, height=30)

        self.text3 = tk.Text(root)
        self.text3.place(x=170, y=150, width=220, height=30)

        self.label2 = tk.Label(root, text="Label")
        self.label2.place(x=80, y=100, width=90, height=30)

        self.label3 = tk.Label(root, text="Label")
        self.label3.place(x=80, y=150, width=90, height=30)

        self.button1 = tk.Button(root, text="Button", command=self.on_button1)
        self.button1.place(x=212, y=240, width=96, height=32)

    def on_button1(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
