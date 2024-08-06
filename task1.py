from tkinter import*
from requests import*
from PIL import Image,ImageTk
from tkinter.messagebox import*
root=Tk()
root.title("Motivational Image Application")
root.geometry("810x500+350+150")

lab_i=Label(root)
lab_i.pack(pady=5)

def gi():
	try:
		url="https://zenquotes.io/api/image"
		res=get(url)
		try:
			with open("mq.png","wb") as f:
				f.write(res.content)
			img=Image.open("mq.png")
			imgtk=ImageTk.PhotoImage(image=img)
			lab_i.configure(image=imgtk)
			lab_i.photo=imgtk
		except Exception as e:
			print("issue",e)


	except Exception as e:
		print("issue",e)
	root.after(10000,gi)
gi()

def close():
	if askyesno("Quit","Do you want to exit?"):
		root.destroy()
root.protocol("WM_DELETE_WINDOW",close)

root.mainloop()