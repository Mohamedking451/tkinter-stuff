from tkinter import *
mo = Tk()
user5 = StringVar()
Pass5 = StringVar()
gmail5 = StringVar()
def register():
	def hacky():
			user_retr = user5.get()
			pass_retr = Pass5.get()
			gmail_retr = gmail5.get()
			Word = "Username: '" + user_retr + "'\n"
			vary1 = "Password: '" + pass_retr + "'\n" 
			vary2 = "Gmail: '" + gmail_retr + "'"
			hi.delete("1.0", "end")
			hi.insert(END, Word)
			hi.insert(END, vary1)
			hi.insert(END, vary2)
	pass_retr = Pass5.get()
	user_retr = user5.get()
	gmail_retr = gmail5.get()
	password_label.destroy()
	gmail1.destroy()
	gmail6_label.destroy()
	username.destroy()
	password.destroy()
	username_label.destroy()
	button5.destroy()
	hi = Text(mo, width = 36, height = 20)
	hi.place(relx = 0.1, rely = 0.1)
	hi.config(fg = "green")
	hi.config(bg = "black")
	button7 = Button(mo, text = "Hack", command = hacky, padx = 50, pady = 20)
	button7.config(bg = "red")
	button7.place(relx = 0.4, rely = 0.7)
username_label = Label(mo, text = "Username")
username = Entry(mo, textvariable = user5 )
password_label = Label(mo, text = "Password")
username_label.config(font = ("calibre", 10))
password = Entry(mo, textvariable = Pass5, show = "*")
password_label.config(font = ("calibre", 10))
gmail6_label = Label(mo, text = "Gmail", font = ("calibre", 11))
gmail1 = Entry(mo, textvariable = gmail5)
button5 = Button(mo, text = "Register", command = register)
#now that we have built the entries and the labels
#we have to place them into a certain position
username_label.place(relx = 0.2, rely = 0.1)	

username.place(relx = 0.1, rely = 0.14)

password_label.place(relx = 0.21, rely = 0.2)

password.place(relx = 0.1, rely = 0.24)

gmail6_label.place(relx = 0.26 , rely = 0.31)

gmail1.place(relx = 0.1, rely = 0.35)

button5.place(relx = 0.19, rely = 0.43)

mo.mainloop()
