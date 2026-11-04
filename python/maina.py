import tkinter as tk
from tkinter import ttk


class Application:

  def __init__(self, root):
    self.root = root
    root.title("Kalkulator Penjumlahan")
    root.geometry("520x380")

    self.label1 = tk.Label(root, text="Angka Pertama")
    self.label1.place(x=60, y=50, width=110, height=30)

    self.entry1 = tk.Entry(root)
    self.entry1.place(x=180, y=50, width=220, height=30)

    self.label2 = tk.Label(root, text="Angka Kedua")
    self.label2.place(x=60, y=100, width=110, height=30)

    self.entry2 = tk.Entry(root)
    self.entry2.place(x=180, y=100, width=220, height=30)

    self.label3 = tk.Label(root, text="Hasil")
    self.label3.place(x=60, y=150, width=110, height=30)

    self.entry3 = tk.Entry(root)
    self.entry3.place(x=180, y=150, width=220, height=30)

    self.button1 = tk.Button(
        root, text="Jumlahkan (+)", command=self.on_button1
    )
    self.button1.place(x=212, y=240, width=120, height=32)

  def on_button1(self):
    try:

      angka1 = float(self.entry1.get())
      angka2 = float(self.entry2.get())

      hasil = angka1 + angka2

      self.entry3.delete(0, tk.END)
      self.entry3.insert(0, str(hasil))
    except ValueError:
      self.entry3.delete(0, tk.END)
      self.entry3.insert(0, "Error: Masukkan angka!")

if __name__ == "__main__":
  root = tk.Tk()
  app = Application(root)
  root.mainloop()