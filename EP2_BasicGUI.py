# BasicGUI.py
# -*- coding: utf-8 -*-

from tkinter import * # * เพื่อให้โหลดเฉพาะไฟล์ main
from tkinter import ttk, messagebox #ไฟล์ย่อยปรับให้ดูสวยงาม + popup
from datetime import datetime, timedelta
import csv

################################
def timestam(thai=False):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) #บวกเป็น พ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		# เพิ่มวัน เวลา EN
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return stamp #ที่ต้อง return เพราะต้องการนำค่าออกไปใช้งานต่อ

def writetext(quantity,total):
	stamp = timestam()
	# ฟังชั่นบันทึกข้อมูลลง txt.
	filename = 'data.txt'
	with open(filename,'a') as file:
		file.write('\n'+'วัน-เวลา: {} แมว: {} ตัว รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))

def writecsv(data):
	#data = ['Time','10',500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) #fw = file writer
		fw.writerow(data)
	print('Success')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	# ใช้สำหรับรวมค่าที่ได้จาก csv ไฟล์สรุปออกมาเป็น 2 อย่าง
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)
	return(sumquan,sumtotal)

################################
GUI = Tk()
GUI.geometry("600x1000") #ปรับขนาดความกว้าง x ความสูง
GUI.title("โปรแกรมสำหรับแม่ค้าแมว v.0.0.1") #ใส่ชื่อโปรแกรม

file = PhotoImage(file="cat.png")
IMG = Label(GUI,image=file,text="")
IMG.pack()

L1 = Label(GUI,text="โปรแกรมคำนวณราคาแมว",font=("Angsana New",20,"bold"), foreground='green') #ใส่ข้อความลงใน GUI
L1.pack() # .place(x,y) , .grid(row=0,column=0), .pack()

L2 = Label(GUI,text="กรุณากรอกจำนวนแมว",font=("Angsana New",15)) #ใส่ข้อความลงใน GUI
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก
E1 = ttk.Entry(GUI,textvariable=v_quantity,font=("impact",30)) # ttk.Entry() หมายถึงดึง Entry มาจาก ttk
E1.pack()

def Calculate(event=None): #event=None เมื่อมีการกดปุ่ม จะใช้ event แต่ถ้ากดด้วยเมาส์ จะไม่มีการส่ง event เข้าไป
	quantity = v_quantity.get()
	price = 100
	print("จำนวน",float(quantity)*price)
	cal = float(quantity) * price

	# writetext(quantity,cal)
	data = [timestam(),quantity,cal]
	writecsv(data)

	# popup
	sm = sumdata()
	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'แมวจำนวน {} ตัว รวมทั้งหมด: {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	#เคลียร์ข้อมูล set 0
	v_quantity.set('')

	# ให้ curser วิ่งไปที่ช่อง E1
	E1.focus()



B1 = ttk.Button(GUI,text="คำนวณ",command=Calculate) #ปุ่มกดเพื่อคำนวณ
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>',Calculate)

def SummaryData(event):
	# popup
	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text = 'จำนวนที่ขายได้:{:,.2f} ตัว \nยอดขาย:{:,.2f} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',SummaryData) # ผูกโปรแกรมกับปุ่มบนคีย์บอร์ดเมื่อกดปุ่ม f1 จะ popup ขึ้นมาเพื่อให้สรุปข้อมูลให้เรา
GUI.bind('<F2>',SummaryData) # ผูกโปรแกรมกับปุ่มบนคีย์บอร์ดเมื่อกดปุ่ม f1 จะ popup ขึ้นมาเพื่อให้สรุปข้อมูลให้เรา

E1.focus() # ให้ curser วิ่งไปที่ช่อง E1

GUI.mainloop() #เพื่อให้ตัว software run ตลอดเวลา