from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

GUI = Tk()
GUI.title('HI-LOW GAME')
GUI.geometry('800x400')

#### ปุ่ม LOW
def LOW(): #ข้อความหลังกดปุ่ม
    hl = [1,2,3,4,5,6,7,8,9,10,11,12] #ข้อความ
    random_number = random.choice(hl)
    if random_number < 6:
        result_text = 'WIN!' # ถ้าสุ่มได้ต่ำกว่า 6 ให้แสดงข้อความ WIN!
    else:
        result_text = 'LOSE!' # ถ้าสุ่มได้มากกว่าหรือเท่ากับ 6 ให้แสดงข้อความ LOSE!
    result_label.config(text=f'Random Number: {random_number} - {result_text}') 
    
def llow():
    LOW()

FB1 = Frame(GUI)
FB1.place(x=150,y=200) #กำหนดตำแหน่ง
B1 = ttk.Button(FB1,text='LOW',command=llow) #ข้อความหน้าปุ่ม
B1.pack(ipadx=20,ipady=20) #กำหนดขนาดปุ่ม

result_label = ttk.Label(GUI, text='Press Choose "LOW" or "HI" to start the game', font=('Angsana News', 18))
result_label.pack(pady=20)

#### ปุ่ม HI
def HI(): #ข้อความหลังกดปุ่ม
    hl = [1,2,3,4,5,6,7,8,9,10,11,12] #ข้อความ
    random_number = random.choice(hl)
    if random_number < 6:
        result_text = 'LOSE!' 
    else:
        result_text = 'WIN!' 
    result_label.config(text=f'Random Number: {random_number} - {result_text}') 
    
def hhi():
    HI()

FB2 = Frame(GUI)
FB2.place(x=500,y=200) #กำหนดตำแหน่ง
B2 = ttk.Button(FB2,text='HI',command=hhi) #ข้อความหน้าปุ่ม
B2.pack(ipadx=20,ipady=20) #กำหนดขนาดปุ่ม

GUI.mainloop()
