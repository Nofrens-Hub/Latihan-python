# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Main:

    def __init__(self, root):
        self.root = root
        root.title("Main - Login")
        root.geometry("520x380")

        self.label1 = tk.Label(root, text="Login", font=("Arial", 16, "bold"))
        self.label1.place(x=215, y=40, width=90, height=26)

        self.label2 = tk.Label(root, text="username", anchor="w")
        self.label2.place(x=140, y=80, width=90, height=26)

        self.entry1 = tk.Entry(root)
        self.entry1.place(x=140, y=106, width=240, height=30)

        self.label3 = tk.Label(root, text="password", anchor="w")
        self.label3.place(x=140, y=164, width=90, height=26)

        # Menambahkan show="*" agar password disamarkan
        self.entry2 = tk.Entry(root, show="*")
        self.entry2.place(x=140, y=190, width=240, height=30)

        self.button1 = tk.Button(root, text="Login", command=self.on_button1)
        self.button1.place(x=212, y=260, width=96, height=32)

    def open_form_2(self):
        # Membuka Form 2 dan menyembunyikan jendela Login utama
        self.root.withdraw()
        Form2(self.root)

    def on_button1(self):
        username = self.entry1.get()
        password = self.entry2.get()

        # Validasi sederhana: form tidak boleh kosong
        if not username or not password:
            messagebox.showwarning(
                "Peringatan", "Username dan Password harus diisi!"
            )
        else:
            # Jika diisi, lanjut buka Form 2
            self.open_form_2()


class Form2:

    def __init__(self, master):
        self.master = master
        root = tk.Toplevel(master)
        self.root = root
        root.title("Form 2 - Data")
        root.geometry("520x380")

        # Menangani tombol 'X' (close) pada Form 2 agar aplikasi menutup sempurna
        root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.checkbutton1_var = tk.IntVar()
        self.checkbutton2_var = tk.IntVar()

        self.label1 = tk.Label(root, text="Nama", anchor="w")
        self.label1.place(x=90, y=60, width=90, height=26)

        self.entry1 = tk.Entry(root)
        self.entry1.place(x=180, y=60, width=150, height=28)

        self.label2 = tk.Label(root, text="Kelas", anchor="w")
        self.label2.place(x=90, y=110, width=90, height=26)

        self.combobox1 = ttk.Combobox(
            root,
            values=[
                "XI AKL 1",
                "XI AKL 2",
                "XI MP 1",
                "XI MP 2",
                "XI RPL",
                "XI BR",
                "XI DKV 1",
                "XI DKV 2",
            ],
            state="readonly",
        )
        self.combobox1.place(x=180, y=110, width=150, height=30)

        self.label3 = tk.Label(root, text="Mapel diklat", anchor="w")
        self.label3.place(x=80, y=200, width=90, height=26)

        self.checkbutton1 = tk.Checkbutton(
            root, text="Python", variable=self.checkbutton1_var, anchor="w"
        )
        self.checkbutton1.place(x=180, y=200, width=120, height=26)

        self.checkbutton2 = tk.Checkbutton(
            root,
            text="Budaya Kerja",
            variable=self.checkbutton2_var,
            anchor="w",
        )
        self.checkbutton2.place(x=300, y=200, width=120, height=26)

    def on_close(self):
        # Menutup seluruh aplikasi ketika Form 2 ditutup
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
