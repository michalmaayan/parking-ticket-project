import tkinter as tk
from demo import run_demo
LARGE_FONT = ("Verdana", 12)

class App(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		self.day =  tk.StringVar()
		self.time = tk.StringVar()
		self.street =  tk.StringVar()
		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		controller.title("Welcome")
		controller.wm_iconbitmap("map.ico")
		width = controller.winfo_width()

		height  = controller.winfo_height()

		controller.geometry('{}x{}'.format(width+280, height+350))

		canvas = tk.Canvas(self)
		canvas.pack(expand=True)
		tk_img = tk.PhotoImage(file="Cover2.png")
		canvas.img=tk_img
		background_label = tk.Label(self, image=tk_img)
		background_label.place(x=0, y=0, relwidth=1, relheight=1)
		# canvas.create_image(125, 125, image=tk_img)

		button = tk.Button(self, text="Press to start", fg="white", bg="#8e24aa",
						   font=("Helvetica", 24), command=lambda: controller.show_frame(PageOne), anchor='w',
								width=10, activebackground="#33B5E5")
		button.configure(width=10, activebackground="#33B5E5")
		canvas.create_window(80, 100, anchor='nw', window=button)


class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		self.configure(background="#009788")

		photo = tk.PhotoImage(file="giphy.gif")
		label = tk.Label(self, image=photo)
		label.image = photo
		label.pack()

		tk.Label(self, text="Please enter information below", fg="#383a39",
									 bg="#009788",
									 font=("Helvetica", 20)).pack()
		tk.Label(self, text="Enter day (i.e. 0-Sunday,...6-Saturday)", fg="#383a39",
						   bg="#009788", font=("Helvetica", 11)).pack()
		entry_day = tk.Entry(self, textvariable=controller.day)
		entry_day.focus()
		entry_day.pack()
		tk.Label(self, text="Enter the time in HHMM format (i.e. 2300)", fg="#383a39",
							bg="#009788", font=("Helvetica", 11)).pack()
		tk.Entry(self, textvariable=controller.time).pack()
		tk.Label(self, text="Enter street name", fg="#383a39", bg="#009788", font=("Helvetica", 11)).pack()
		tk.Entry(self, textvariable=controller.street).pack()

		button = tk.Button(self, text="Continue", fg="#009788", bg="#383a39",font=("Helvetica", 12),
						   command= lambda: controller.show_frame(PageTwo))
		button.pack()
		button1 = tk.Button(self, text="Back to Home", fg="#009788", bg="#383a39",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()


class PageTwo(tk.Frame):
	def print_text(self, controller):
		run_demo(controller.day.get(), controller.time.get(), controller.street.get())

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.configure(background="#009788")
		label = tk.Label(self,fg="#383a39", bg="#009788", text="Have patience it might take a few minutes",
						 font=("Helvetica", 10))
		label.pack()
		label = tk.Label(self, fg="#383a39",bg="#009788", text="we are learning from a database"
															   " with 4 million rows:)", font=("Helvetica", 10))
		label.pack()
		button2 = tk.Button(self, fg="#009788",bg="#383a39",text="Run", font=("Helvetica", 10),width=10,
							command=lambda: self.print_text(controller))
		button2.pack()
		button1 = tk.Button(self, fg="#009788",bg="#383a39", text="Back",width=10,
							command=lambda: controller.show_frame(PageOne))
		button1.pack()
		photo = tk.PhotoImage(file="page2.png")
		label = tk.Label(self, image=photo)
		label.image = photo
		label.pack()


app = App()
app.mainloop()