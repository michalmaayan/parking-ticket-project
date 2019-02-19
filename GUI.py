from tkinter import *
from tkinter import messagebox
from demo import run_demo


def print_text():
	global day
	global time
	global street
	run_demo(day.get(), time.get(), street.get())


root = Tk()
# gui = GUI(root)
day = StringVar()
time = StringVar()
street = StringVar()

root.configure(background="#009788")
root.title("Welcome")
root.wm_iconbitmap("map.ico")

photo = PhotoImage(file="giphy.gif")
label = Label(root, image=photo).pack()

instruction_label = Label(root, text="Please enter information below", fg="#383a39", bg="#009788",
						  font=("Helvetica", 16)).pack()
lbl_day = Label(root, text="Enter day (i.e. 0-Sunday,...6-Saturday)", fg="#383a39",
				bg="#009788").pack()
entry_day = Entry(root, textvariable=day)
entry_day.focus()
entry_day.pack()
lbl_time = Label(root, text="Enter the time in HHMM format (i.e. 2300)", fg="#383a39",
				 bg="#009788").pack()
entry_time = Entry(root, textvariable=time).pack()
lbl_street = Label(root, text="Enter street name", fg="#383a39", bg="#009788").pack()
entry_street = Entry(root, textvariable=street).pack()

button = Button(root, text="Submit", fg="#009788", bg="#383a39", command=print_text).pack()

root.mainloop()


class GUI:

	def print_text(self):
		day = self.day.get()
		time = self.time.get()
		street_name = self.street.get()
		run_demo(day, time, street_name)

	# self.root.messagebox.showinfo("window title", message)

	def __init__(self, root):
		# variables
		self.root = root
		self.day = StringVar()
		self.time = StringVar()
		self.street = StringVar()

	# #design
	# customFont = tkFont.Font(family="Arial", size=12)
	# photo = PhotoImage(file=r"pnggrad16rgba.png")
	#
	# #frames
	# top_frame = Frame(self.root)
	# top_frame.pack()
	#
	#
	# L1 = Label(top_frame,image = photo, text="Enter day of the week (i.e. 0-Sunday,...6-Saturday)",compound=TOP,
	# 		   font=customFont)
	# L2 = Label(top_frame,image = photo, text="Enter the time in HHMM format", compound=TOP,font=customFont)
	# L3 = Label(top_frame,image = photo, text="Enter street name",compound=TOP, font=customFont)
	#
	# entry1 = Entry(top_frame, textvariable=self.day)
	# entry2 = Entry(top_frame, textvariable=self.time)
	# entry3 = Entry(top_frame, textvariable=self.street)
	#
	# L1.pack(row=0, sticky=E)
	# L2.pack(row=1, sticky=E)
	# L3.pack(row=2, sticky=E)
	#
	# entry1.pack(row=0, column=1)
	# entry2.pack(row=1, column=1)
	# entry3.pack(row=2, column=1)
	# entry1.focus_set()
	# entry2.focus_set()
	# entry3.focus_set()
	#
	# bottom_frame = Frame(root)
	# bottom_frame.pack(side=BOTTOM)
	# button = Button(bottom_frame, text="Submit", fg="purple", font=customFont,
	# 				command=self.print_text)
	# button.pack()
