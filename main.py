from tkinter import *
import ctypes,os
from tkinter.tix import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from time import sleep
from tkinter.filedialog import askopenfile
import cv2
from detect import start_detecttion
import imageio
from PIL import Image, ImageTk
import threading

def HomePage():
	global cntct,about
	try:
		cntct.destroy()
	except:
		pass
	try:
		about.destroy()
	except:
		pass

	window = Tk()
	img = Image.open("C:/Users/Sudheep/Downloads/Helmet_Number Plate Detection-GUI/Helmet_Number Plate Detection-GUI/Images/Home.png")
	img = ImageTk.PhotoImage(img)
	panel = Label(window, image=img)
	panel.pack(side="top", fill="both", expand="yes")

	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
	lt = [w, h]
	a = str(lt[0]//2-446)
	b= str(lt[1]//2-383)

	window.title("HOME - H&N")
	window.geometry("956x717+"+a+"+"+b)
	window.resizable(0,0)

	def contactus():
		global cntct,about
		try:
			window.destroy()
		except:
			pass
	
		cntct = Tk()
		img = Image.open("Images\\OurTeam.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(cntct, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-446)
		b= str(lt[1]//2-383)

		cntct.title("CONTACT US - H&N")
		cntct.geometry("956x717+"+a+"+"+b)
		cntct.resizable(0,0)

		homebtn = Button(cntct,text = "GO BACK TO HOME",font = ("Agency FB",19,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="#3E7A9B",fg="white",activebackground = "#3E7A9B",activeforeground = "white",command=HomePage)
		homebtn.place(x=114,y = 478)
		

		cntct.mainloop()

	def stream(label, video):
		for image in video.iter_data():
			frame_image = ImageTk.PhotoImage(Image.fromarray(image))
			label.config(image=frame_image)
			label.image = frame_image

	def detection_result(image_file):
		global cntct
		window.destroy()
		cntct = Tk()

		if image_file[-4:] == '.mp4':			
			panel = Label(cntct)
			panel.pack(side="top", fill="both", expand="yes")
			video = imageio.get_reader(image_file)
			thread = threading.Thread(target=stream, args=(panel, video))
			thread.daemon = 1
			thread.start()

		else:
			image = Image.open(image_file)
			width, height = image.size
			

			if width > 854 or height > 628:
				resize_factor = (72000) / width
				height = int((height * resize_factor) / 100)
				image = image.resize((720, height))
			
			image = ImageTk.PhotoImage(image)

			panel = Label(cntct, image=image)
			panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-446)
		b = str(lt[1]//2-383)

		cntct.title("Detection Result | H & N")
		cntct.geometry("904x678+"+a+"+"+b)
		cntct.resizable(0, 0)

		homebtn = Button(cntct, text="GO BACK", font=("Arial Black", 12, "bold"), height=1, relief=FLAT, bd=0, borderwidth='0',
							bg="#F7F8FA", fg="#5C8EC6", activebackground="#F7F8FA", activeforeground="#5C8EC6", command=HomePage)
		homebtn.place(x=390, y=630)
		cntct.mainloop()


	def aboutus():
		global about,cntct
		try:
			window.destroy()
		except:
			pass


		about = Tk()
		img = Image.open("Images/AboutProject.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(about, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-446)
		b= str(lt[1]//2-383)

		about.title("ABOUT US - H&N")
		about.geometry("956x717+"+a+"+"+b)
		about.resizable(0,0)

		homebtn = Button(about,text = "GO BACK TO HOME",font = ("Agency FB",15,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="#479ECE",fg="white",activebackground = "#479ECE",activeforeground = "white",command=HomePage)
		homebtn.place(x=412,y = 509)

		about.mainloop()

	# EXIT . . . 
	def exit():
		global cntct,about
		result = tkMessageBox.askquestion("H&N", "Are you sure you want to exit?", icon= "warning")
		if result == 'yes':
			window.destroy()

	''' MENU BAR '''             

	def open_file():
		file = askopenfile(mode='r')
		if file is not None:
			filename = file.name[file.name.rfind('/')+1:]
			save_dir = start_detecttion(file.name)
			detection_result(os.path.join(save_dir, os.listdir(save_dir)[0]))

			
	aboutusbtn = Button(window,text = "About Us",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#69418B",activebackground = "white",activeforeground = "#69418B",command=aboutus)
	aboutusbtn.place(x=575,y = 150)
	contactusbtn = Button(window,text = "Contact Us",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#69418B",activebackground = "white",activeforeground = "#69418B",command=contactus)
	contactusbtn.place(x=665,y = 150)
	exitbtn = Button(window,text = "Exit",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#69418B",activebackground = "white",activeforeground = "#69418B",command=exit)
	exitbtn.place(x=765,y = 150)

	browsebtn = Button(window,text = "BROWSE" ,font = ("Arial Narrow",17,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="#69418B",fg="white",activebackground = "#69418B",activeforeground = "white",  command=lambda: open_file())
	browsebtn.place(x=236,y = 427)

	window.mainloop()

HomePage()