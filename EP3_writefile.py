# writefile.py
from datetime import datetime

quantity = 10
cal = quantity * 100

def writetext(quantity,total):
	# เพิ่มวัน เวลา TH
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) #บวกเป็น พ.ศ.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')

	# ฟังชั่นบันทึกข้อมูลลง txt.
	filename = 'data.txt'
	with open(filename,'a') as file:
		file.write('\n'+'วัน-เวลา: {} แมว: {} ตัว รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))