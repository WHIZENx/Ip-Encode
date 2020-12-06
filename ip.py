from tkinter import *
from tkinter import messagebox
import os, string
import encode
def resource_path(relative_path):
	try:
		base_path = os.path.join(sys._MEIPASS, 'data')
	except Exception:
		base_path = '...' # folder path of code
	return os.path.join(base_path, relative_path)

def main():
	root = Tk()
	root.title("IP Encoder")
	root.resizable(width=False, height=False)
	root.geometry('370x200')
	root.iconbitmap(resource_path("ip.ico"))
	Label(root, text="_________", font=("Tahoma", 20)).place(x=115, y=7)
	Label(root, text="IP Encoder", font=("Tahoma", 20)).pack()
	Label(root,  text="Enter IP address :", font=("Tahoma", 10)).place(x=40, y=50)

	str_var1 = StringVar()
	str_var2 = StringVar()
	str_var3 = StringVar()
	str_var4 = StringVar()
	str_var5 = StringVar()

	def Written_1(*args):
		if str_var1.get().isdigit() == False and "." not in str_var1.get():
			entry1.delete(0, END)
		text = str_var1.get().split(".")
		if len(text) == 4:
			if text[0].isalpha(): entry1.delete(0, END)
			if text[1].isalpha(): entry2.delete(0, END)
			if text[2].isalpha(): entry3.delete(0, END)
			if text[3].isalpha(): entry4.delete(0, END)
			entry1.delete(0, END)
			entry2.delete(0, END)
			entry3.delete(0, END)
			entry4.delete(0, END)
			entry1.insert(INSERT, text[0])
			entry2.insert(INSERT, text[1])
			entry3.insert(INSERT, text[2])
			entry4.insert(INSERT, text[3])
	str_var1.trace("w", Written_1)
	entry1 = Entry(root, width=4, textvariable=str_var1)
	entry1.place(x=150, y=50)

	Label(root,  text=".", font=("Tahoma", 10)).place(x=180, y=50)

	def Written_2(*args):
		if str_var2.get().isdigit() == False and "." not in str_var2.get():
			entry2.delete(0, END)
		text = str_var1.get().split(".")
		if len(text) == 4:
			if text[0].isalpha(): entry1.delete(0, END)
			if text[1].isalpha(): entry2.delete(0, END)
			if text[2].isalpha(): entry3.delete(0, END)
			if text[3].isalpha(): entry4.delete(0, END)
			entry1.delete(0, END)
			entry2.delete(0, END)
			entry3.delete(0, END)
			entry4.delete(0, END)
			entry1.insert(INSERT, text[0])
			entry2.insert(INSERT, text[1])
			entry3.insert(INSERT, text[2])
			entry4.insert(INSERT, text[3])
	str_var2.trace("w", Written_2)
	entry2 = Entry(root, width=4, textvariable=str_var2)
	entry2.place(x=190, y=50)

	Label(root,  text=".", font=("Tahoma", 10)).place(x=220, y=50)

	def Written_3(*args):
		if str_var3.get().isdigit() == False and "." not in str_var3.get():
			entry3.delete(0, END)
		text = str_var1.get().split(".")
		if len(text) == 4:
			if text[0].isalpha(): entry1.delete(0, END)
			if text[1].isalpha(): entry2.delete(0, END)
			if text[2].isalpha(): entry3.delete(0, END)
			if text[3].isalpha(): entry4.delete(0, END)
			entry1.delete(0, END)
			entry2.delete(0, END)
			entry3.delete(0, END)
			entry4.delete(0, END)
			entry1.insert(INSERT, text[0])
			entry2.insert(INSERT, text[1])
			entry3.insert(INSERT, text[2])
			entry4.insert(INSERT, text[3])
	str_var3.trace("w", Written_3)
	entry3 = Entry(root, width=4, textvariable=str_var3)
	entry3.place(x=230, y=50)

	Label(root,  text=".", font=("Tahoma", 10)).place(x=260, y=50)

	def Written_4(*args):
		if str_var4.get().isdigit() == False and "." not in str_var4.get():
			entry4.delete(0, END)
		text = str_var1.get().split(".")
		if len(text) == 4:
			if text[0].isalpha(): entry1.delete(0, END)
			if text[1].isalpha(): entry2.delete(0, END)
			if text[2].isalpha(): entry3.delete(0, END)
			if text[3].isalpha(): entry4.delete(0, END)
			entry1.delete(0, END)
			entry2.delete(0, END)
			entry3.delete(0, END)
			entry4.delete(0, END)
			entry1.insert(INSERT, text[0])
			entry2.insert(INSERT, text[1])
			entry3.insert(INSERT, text[2])
			entry4.insert(INSERT, text[3])
	str_var4.trace("w", Written_4)
	entry4 = Entry(root, width=4, textvariable=str_var4)
	entry4.place(x=270, y=50)

	Label(root,  text="Binary Octets :", font=("Tahoma", 10)).place(x=20, y=80)
	entry5 = Entry(root, width=8)
	entry5.configure(state="readonly")
	entry5.place(x=110, y=80)
	entry6 = Entry(root, width=8)
	entry6.configure(state="readonly")
	entry6.place(x=170, y=80)
	entry7 = Entry(root, width=8)
	entry7.configure(state="readonly")
	entry7.place(x=230, y=80)
	entry8 = Entry(root, width=8)
	entry8.configure(state="readonly")
	entry8.place(x=290, y=80)
	Label(root,  text="32-Bit Binary :", font=("Tahoma", 10)).place(x=30, y=110)
	entry9 = Entry(root, width=32)
	entry9.configure(state="readonly")
	entry9.place(x=120, y=110)
	Label(root,  text="Decimal :", font=("Tahoma", 10)).place(x=80, y=140)
	def Written_5(*args):
		if str_var5.get().isdigit() == False:
			entry10.delete(0, END)
	str_var5.trace("w", Written_5)
	entry10 = Entry(root, width=25, textvariable=str_var5)
	entry10.place(x=140, y=140)

	def calculate():
		if str_var1.get() == "" or str_var2.get() == "" or str_var3.get() == "" or str_var4.get() == "":
			if entry10.get() == "":
				return messagebox.showerror("Error!", "Please input your ip address or decimal number.")

		if str_var1.get() != "" and str_var2.get() != "" and str_var3.get() != "" and str_var4.get() != "":

			if int(str_var1.get()) < 0 or int(str_var1.get()) > 255:
				return messagebox.showerror("Error!", "Error value 0-255.")
			if int(str_var2.get()) < 0 or int(str_var2.get()) > 255:
				return messagebox.showerror("Error!", "Error value 0-255.")
			if int(str_var3.get()) < 0 or int(str_var3.get()) > 255:
				return messagebox.showerror("Error!", "Error value 0-255.")
			if int(str_var4.get()) < 0 or int(str_var4.get()) > 255:
				return messagebox.showerror("Error!", "Error value 0-255.")
			entry5.configure(state="normal")
			entry6.configure(state="normal")
			entry7.configure(state="normal")
			entry8.configure(state="normal")
			entry5.delete(0, END)
			entry6.delete(0, END)
			entry7.delete(0, END)
			entry8.delete(0, END)
			entry5.insert(INSERT, encode.convert_to_bin(int(str_var1.get()), 1))
			entry6.insert(INSERT, encode.convert_to_bin(int(str_var2.get()), 1))
			entry7.insert(INSERT, encode.convert_to_bin(int(str_var3.get()), 1))
			entry8.insert(INSERT, encode.convert_to_bin(int(str_var4.get()), 1))
			entry5.configure(state="readonly")
			entry6.configure(state="readonly")
			entry7.configure(state="readonly")
			entry8.configure(state="readonly")

			entry9.configure(state="normal")
			entry9.delete(0, END)
			entry9.insert(INSERT, entry5.get()+entry6.get()+entry7.get()+entry8.get())
			entry9.configure(state="readonly")
			entry10.delete(0, END)
			entry10.insert(INSERT, encode.convert_to_dec(entry5.get()+entry6.get()+entry7.get()+entry8.get()))
		else:
			if int(entry10.get()) < 0 or int(entry10.get()) >= 2 << 31:
				return messagebox.showerror("Error!", "Error value 0-4294967295.")

			entry1.delete(0, END)
			entry2.delete(0, END)
			entry3.delete(0, END)
			entry4.delete(0, END)
			entry5.configure(state="normal")
			entry6.configure(state="normal")
			entry7.configure(state="normal")
			entry8.configure(state="normal")
			entry5.delete(0, END)
			entry6.delete(0, END)
			entry7.delete(0, END)
			entry8.delete(0, END)
			entry5.insert(INSERT, encode.convert_to_bin(int(entry10.get()), 2)[:8])
			entry6.insert(INSERT, encode.convert_to_bin(int(entry10.get()), 2)[8:16])
			entry7.insert(INSERT, encode.convert_to_bin(int(entry10.get()), 2)[16:24])
			entry8.insert(INSERT, encode.convert_to_bin(int(entry10.get()), 2)[24:])
			entry5.configure(state="readonly")
			entry6.configure(state="readonly")
			entry7.configure(state="readonly")
			entry8.configure(state="readonly")

			entry1.insert(INSERT, encode.convert_to_dec(encode.convert_to_bin(int(entry10.get()), 2)[:8]))
			entry2.insert(INSERT, encode.convert_to_dec(encode.convert_to_bin(int(entry10.get()), 2)[8:16]))
			entry3.insert(INSERT, encode.convert_to_dec(encode.convert_to_bin(int(entry10.get()), 2)[16:24]))
			entry4.insert(INSERT, encode.convert_to_dec(encode.convert_to_bin(int(entry10.get()), 2)[24:]))

			entry9.configure(state="normal")
			entry9.delete(0, END)
			entry9.insert(INSERT, encode.convert_to_bin(int(entry10.get()), 2))
			entry9.configure(state="readonly")
	def reset():
		entry1.delete(0, END)
		entry2.delete(0, END)
		entry3.delete(0, END)
		entry4.delete(0, END)
		entry5.configure(state="normal")
		entry6.configure(state="normal")
		entry7.configure(state="normal")
		entry8.configure(state="normal")
		entry5.delete(0, END)
		entry6.delete(0, END)
		entry7.delete(0, END)
		entry8.delete(0, END)
		entry5.configure(state="readonly")
		entry6.configure(state="readonly")
		entry7.configure(state="readonly")
		entry8.configure(state="readonly")
		entry9.configure(state="normal")
		entry9.delete(0, END)
		entry9.configure(state="readonly")
		entry10.delete(0, END)

	Button(root, text="Calculate", fg="green", command=calculate, width=10).place(x=100, y=170)
	Button(root, text="Reset", fg="red", command=reset, width=10).place(x=190, y=170)
	root.mainloop()

if __name__ == '__main__':
	main()
