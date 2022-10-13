# Создайте программу для игры в 'Крестики-нолики'.

from tkinter import *

def konec():
	krestik.destroy()
	if igrok.get() == 1: 
		knc = Label(win, text ="Первый игрок победил!")
		knc.pack()
	else:
		knc = Label(win, text ="Второй игрок победил!")
		knc.pack()

def proverka1():
	u11()
	u21()
	u31()
	u41()
	u51()
	u61()
	u71()
	u81()

def proverka2():
	u12()
	u22()
	u32()
	u42()
	u52()
	u62()
	u72()
	u82()

def u11 ():
	if pobeda[0] == pobeda[1] == pobeda[2] == 1:
		konec()		
def u21 ():
	if pobeda[0]==1:
		if pobeda[3]==1:
			if pobeda[6]==1:
				konec()
def u31 ():
	if pobeda[0]==1:
		if pobeda[4]==1:
			if pobeda[8]==1:
				konec()
def u41 ():
	if pobeda[1]==1:
		if pobeda[4]==1:
			if pobeda[7]==1:
				konec()
def u51 ():
	if pobeda[2]==1:
		if pobeda[5]==1:
			if pobeda[8]==1:
				konec()
def u61 ():
	if pobeda[2]==1:
		if pobeda[4]==1:
			if pobeda[6]==1:
				konec()
def u71 ():
	if pobeda[3]==1:
		if pobeda[4]==1:
			if pobeda[5]==1:
				konec()
def u81 ():
	if pobeda[6]==1:
		if pobeda[7]==1:
			if pobeda[8]==1:
				konec()
def u12 ():
	if pobeda[0]==0:
		if pobeda[1]==0:
			if pobeda[2]==0:
				konec()
def u22 ():
	if pobeda[0]==0:
		if pobeda[3]==0:
			if pobeda[6]==0:
				konec()
def u32 ():
	if pobeda[0]==0:
		if pobeda[4]==0:
			if pobeda[8]==0:
				konec()
def u42 ():
	if pobeda[1]==0:
		if pobeda[4]==0:
			if pobeda[7]==0:
				konec()
def u52 ():
	if pobeda[2]==0:
		if pobeda[5]==0:
			if pobeda[8]==0:
				konec()
def u62 ():
	if pobeda[2]==0:
		if pobeda[4]==0:
			if pobeda[6]==0:
				konec()
def u72 ():
	if pobeda[3]==0:
		if pobeda[4]==0:
			if pobeda[5]==0:
				konec()
def u82 ():
	if pobeda[6]==0:
		if pobeda[7]==0:
			if pobeda[8]==0:
				konec()

def p1 ():
	if igrok.get() == 1:
		btn1.destroy()
		pobeda[0]=igrok.get()
		krest1 = Label (krestik, text= "X")
		krest1.grid(column=0, row=1)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn1.destroy()
		pobeda[0]=igrok.get()
		nol1 = Label (krestik, text= "O")
		nol1.grid(column=0, row=1)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)		
def p2 ():
	if igrok.get() == 1:
		btn2.destroy()
		pobeda[1]=igrok.get()
		krest2 = Label (krestik, text= "X")
		krest2.grid(column=1, row=1)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn2.destroy()
		pobeda[1]=igrok.get()
		nol2 = Label (krestik, text= "O")
		nol2.grid(column=1, row=1)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p3 ():
	if igrok.get() == 1:
		btn3.destroy()
		pobeda[2]=igrok.get()
		krest3 = Label (krestik, text= "X")
		krest3.grid(column=2, row=1)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn3.destroy()
		pobeda[2]=igrok.get()
		nol3 = Label (krestik, text= "O")
		nol3.grid(column=2, row=1)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p4 ():
	if igrok.get() == 1:
		btn4.destroy()
		pobeda[3]=igrok.get()
		krest4 = Label (krestik, text= "X")
		krest4.grid(column=0, row=2)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn4.destroy()
		pobeda[3]=igrok.get()
		nol4 = Label (krestik, text= "O")
		nol4.grid(column=0, row=2)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p5 ():
	if igrok.get() == 1:
		btn5.destroy()
		pobeda[4]=igrok.get()
		krest5 = Label (krestik, text= "X")
		krest5.grid(column=1, row=2)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn5.destroy()
		pobeda[4]=igrok.get()
		nol5 = Label (krestik, text= "O")
		nol5.grid(column=1, row=2)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p6 ():
	if igrok.get() == 1:
		btn6.destroy()
		pobeda[5]=igrok.get()
		krest6 = Label (krestik, text= "X")
		krest6.grid(column=2, row=2)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn6.destroy()
		pobeda[5]=igrok.get()
		nol6 = Label (krestik, text= "O")
		nol6.grid(column=2, row=2)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p7 ():
	if igrok.get() == 1:
		btn7.destroy()
		pobeda[6]=igrok.get()
		krest7 = Label (krestik, text= "X")
		krest7.grid(column=0, row=3)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn7.destroy()
		pobeda[6]=igrok.get()
		nol7 = Label (krestik, text= "O")
		nol7.grid(column=0, row=3)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p8 ():
	if igrok.get() == 1:
		btn8.destroy()
		pobeda[7]=igrok.get()
		krest8 = Label (krestik, text= "X")
		krest8.grid(column=1, row=3)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn8.destroy()
		pobeda[7]=igrok.get()
		nol8 = Label (krestik, text= "O")
		nol8.grid(column=1, row=3)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)
def p9 ():
	if igrok.get() == 1:
		btn9.destroy()
		pobeda[8]=igrok.get()
		krest9 = Label (krestik, text= "X")
		krest9.grid(column=2, row=3)
		nadpis.config(text= "Игрок 2: O")
		proverka1()
		igrok.set(0)
	else:	
		btn9.destroy()
		pobeda[8]=igrok.get()
		nol9 = Label (krestik, text= "O")
		nol9.grid(column=2, row=3)
		nadpis.config(text= "Игрок 1: X")
		proverka2()
		igrok.set(1)

win = Tk()

krestik = Frame(win)
krestik.pack()

igrok = IntVar()
igrok.set(1)
pobeda = [2,2,2,2,2,2,2,2,2]

nadpis = Label (krestik, text= "Игрок 1: X")
nadpis.grid(column=0, row=0, columnspan=3)

btn1 = Button(krestik, text="???", command=p1)
btn1.grid(column=0, row=1)

btn2 = Button(krestik, text="???", command=p2)
btn2.grid(column=1, row=1)

btn3 = Button(krestik, text="???", command=p3)
btn3.grid(column=2, row=1)

btn4 = Button(krestik, text="???", command=p4)
btn4.grid(column=0, row=2)

btn5 = Button(krestik, text="???", command=p5)
btn5.grid(column=1, row=2)

btn6 = Button(krestik, text="???", command=p6)
btn6.grid(column=2, row=2)

btn7 = Button(krestik, text="???", command=p7)
btn7.grid(column=0, row=3)

btn8 = Button(krestik, text="???", command=p8)
btn8.grid(column=1, row=3)

btn9 = Button(krestik, text="???", command=p9)
btn9.grid(column=2, row=3)


krestik.mainloop()