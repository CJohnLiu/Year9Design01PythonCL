import math
from tkinter import *


root = Tk()
root.title("Heron's Formula by Christopher Liu")
root.minsize(width=1000,height=2000)


def _init_(self, master):
	entry_1=tk.IntVar()
	entry_2=tk.IntVar()
	entry_3=tk.IntVar()

def clear_content():
	entry_1.delete(0,END)
	entry_2.delete(0,END)
	entry_3.delete(0,END)
	outlabel1 = Label(root,text='                                                                    ')
	outlabel1.grid(row=2,columnspan=2)
	outlabel2 = Label(root,text='                                                                    ')
	outlabel2.grid(row=3,columnspan=2)  
	label_rat = Label(root,text='                                                                    ')
	label_rat.grid(row=11,columnspan=2)
	label_rr = Label (root,text='                                                                    ')
	label_rr.grid(row=12,columnspan=2)
	label_rac = Label(root,text='                                                                     ')
	label_rac.grid(row=13,columnspan=2)
	Label_name = Label (root, text='                                                                                          ')
	Label_name.grid(row=1,columnspan=2)      

def calculate():
	aa = entry_1.get()
	bb = entry_2.get()
	cc = entry_3.get()

	a=int(aa)
	b=int(bb)
	c=int(cc)

	name_of_user = entry_name.get()
	name_to_display = "Hello " +  name_of_user
	label_name=Label(root, text=name_to_display)
	label_name.grid(row=1,columnspan=2)

	if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100:
		outlabel1 = Label(root, text="          there is an out of range value        ")
		outlabel1.grid(row=2,columnspan=2)
	else:
		outlabel1 = Label(root, text="")
		outlabel1.grid(row=2,columnspan=2)

		if  a + b <= c or a + c <= b or b + c <= a:
			outlabel2 = Label(root, text="        this is an impossible triangle       ")
			outlabel2.grid(row=3,columnspan=2)
		else:
			outlabel2 = Label(root, text="")	
			outlabel2.grid(row=3,columnspan=2)

			s = (a+b+c)/2.0
			areatriangle = (s*(s-a)*(s-b)*(s-c))**0.5
			roundareatriangle = round(areatriangle)
			label_rat = Label(root, text="            triangle area: " + str(roundareatriangle) + " units squared.         ")
			label_rat.grid(row=11,columnspan=2)

			r = areatriangle/s
			roundradius = round(r,1)
			label_rr = Label(root, text="        inscribed circle radius: " + str(roundradius) + " units.              ")
			label_rr.grid(row=12,columnspan=2)

			areacircle = 3.14159*r*r
			roundareacircle = round(areacircle)
			label_rac = Label(root, text="        inscrbed circle area: " + str(roundareacircle) + " units squared.        ")
			label_rac.grid(row=13,columnspan=2)

			angle = math.degrees(math.acos((a**2 + b**2 - c**2)/(2.0 * a * b)))

			d = b * math.cos(math.radians(angle))
			e = b * math.sin(math.radians(angle))

			#magnifying the shape by 10 and shifting 100 units vertically and horizontally
			l1 = 100
			l2 = 100
			l3 = a*10 + 100
			l4 = 100
			l5 = d*10 + 100
			l6 = e*10 + 100


			halfangle = angle/2.0
			f = math.sin(math.radians(90-halfangle))
			g = math.sin(math.radians(halfangle))
			h = r * f / g
			
			#magnifying the shape by 10 and shifting 100 units vertically and horozontally
			x0 = (h-r)*10+100
			y0 = (2*r)*10+100
			x1 = (h+r)*10+100
			y1 = 100	


			mycanvas = Canvas(root, width=1100, height=1100, bg="yellow")
			mycanvas.grid(row=15,columnspan=2)

			mycanvas.create_line(l1,l2,l3,l4,l5,l6,l1,l2, fill="red", width="3")
			mycanvas.create_oval(x0,y0,x1,y1, fill="grey")



message1=Label(root,text='This program calculates areas of triangles and radius/area of inscribed circles', font=('Purisa',20), bg="black", fg="white")
message1.grid(row=0,columnspan=2)

label_name=Label(root,text='Enter your first name', relief=RIDGE, width=30)
label_name.grid(row=4,column=0)

entry_name=Entry(root, relief=SUNKEN,width=30)
entry_name.grid(row=4,column=1)

label_1=Label(root,text="Enter (1-100) for 1st side length", relief=RIDGE, width=30)
label_1.grid(row=5,column=0)

entry_1=Entry(root, relief=SUNKEN,width=30)
entry_1.grid(row=5,column=1)

label_2=Label(root,text="Enter (1-100) for 2nd side length", relief=RIDGE, width=30)
entry_2=Entry(root, relief=SUNKEN,width=30)
label_2.grid(row=6,column=0)
entry_2.grid(row=6,column=1)

label_3=Label(root,text="Enter (1-100) for 3rd side length", relief=RIDGE, width=30)
entry_3=Entry(root, relief=SUNKEN,width=30)
label_3.grid(row=7,column=0)
entry_3.grid(row=7,column=1)

button_1=Button(root,text="calculate",relief=RIDGE, width=30, command=calculate)
button_1.grid(row=8,columnspan=2)

button_3=Button(root,text="clear",relief=RIDGE, width=30, command=clear_content)
button_3.grid(row=14,columnspan=2)



root.mainloop()
