import tkinter as tk
from tkinter import ttk


class Application:

  def __init__(self, root):
    self.root = root
    root.title("Main")
    root.geometry("520x330")

    # Top Labels
    self.label_top = tk.Label(root, text="kalkulator diklat", font=("Arial", 10, "bold"))
    self.label_top.place(x=140, y=10, width=220, height=20)

    self.label_bottom = tk.Label(root, text="Mikhail XI RPL", font=("Arial", 9))
    self.label_bottom.place(x=140, y=30, width=220, height=20)

    # Entry Box (shifted down)
    self.entry1 = tk.Entry(root, justify="left", font=("Arial", 12))
    self.entry1.place(x=20, y=60, width=480, height=30)
    self.entry1.insert(0, "0")

    # Row 1
    self.button1 = tk.Button(root, text="7", command=lambda: self.on_click("7"))
    self.button1.place(x=30, y=110, width=96, height=32)

    self.button2 = tk.Button(root, text="8", command=lambda: self.on_click("8"))
    self.button2.place(x=140, y=110, width=96, height=32)

    self.button3 = tk.Button(root, text="9", command=lambda: self.on_click("9"))
    self.button3.place(x=250, y=110, width=96, height=32)

    self.button4 = tk.Button(root, text="/", command=lambda: self.on_click("/"))
    self.button4.place(x=360, y=110, width=96, height=32)

    # Row 2
    self.button5 = tk.Button(root, text="4", command=lambda: self.on_click("4"))
    self.button5.place(x=30, y=150, width=96, height=32)

    self.button8 = tk.Button(root, text="5", command=lambda: self.on_click("5"))
    self.button8.place(x=140, y=150, width=96, height=32)

    self.button11 = tk.Button(
        root, text="6", command=lambda: self.on_click("6")
    )
    self.button11.place(x=250, y=150, width=96, height=32)

    self.button14 = tk.Button(
        root, text="*", command=lambda: self.on_click("*")
    )
    self.button14.place(x=360, y=150, width=96, height=32)

    # Row 3
    self.button6 = tk.Button(root, text="1", command=lambda: self.on_click("1"))
    self.button6.place(x=30, y=190, width=96, height=32)

    self.button9 = tk.Button(root, text="2", command=lambda: self.on_click("2"))
    self.button9.place(x=140, y=190, width=96, height=32)

    self.button12 = tk.Button(
        root, text="3", command=lambda: self.on_click("3")
    )
    self.button12.place(x=250, y=190, width=96, height=32)

    self.button15 = tk.Button(
        root, text="-", command=lambda: self.on_click("-")
    )
    self.button15.place(x=360, y=190, width=96, height=32)

    # Row 4
    self.button7 = tk.Button(root, text="0", command=lambda: self.on_click("0"))
    self.button7.place(x=30, y=230, width=96, height=32)

    self.button10 = tk.Button(
        root, text=".", command=lambda: self.on_click(".")
    )
    self.button10.place(x=140, y=230, width=96, height=32)

    self.button13 = tk.Button(root, text="=", command=self.on_calculate)
    self.button13.place(x=250, y=230, width=96, height=32)

    self.button16 = tk.Button(
        root, text="+", command=lambda: self.on_click("+")
    )
    self.button16.place(x=360, y=230, width=96, height=32)

  def on_click(self, char):
    current = self.entry1.get()
    if current == "0" or current == "Error":
      self.entry1.delete(0, tk.END)
      self.entry1.insert(0, char)
    else:
      self.entry1.insert(tk.END, char)

  def on_calculate(self):
    try:
      result = eval(self.entry1.get())
      self.entry1.delete(0, tk.END)
      self.entry1.insert(0, str(result))
    except Exception:
      self.entry1.delete(0, tk.END)
      self.entry1.insert(0, "Error")


if __name__ == "__main__":
  root = tk.Tk()
  app = Application(root)
  root.mainloop()