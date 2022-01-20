import time


enroll = 180130107086
print(enroll)
print(time.ctime())
from tkinter import *
master = Tk()
def red():
    frame.configure(background = "red")
    print('Button1 Clicked!')
def green():
    frame.configure(background = "green")
    print('Buttno2 Clicked!')
def pink():
    frame.configure(background = "pink")
    print('Button3 Clicked!')
frame = Frame(master, background="blue")
btn1 = Button(frame, command=red, padx = 20)
btn2 = Button(frame, command=green, padx = 20)
btn3 = Button(frame, command=pink, padx = 20)
btn1['text'] = 'Button1'
btn2['text'] = 'Button2'
btn3['text'] = 'Button3'
btn1.pack(pady = 20, padx = 20)
btn2.pack(pady = 20, padx = 20)
btn3.pack(pady = 20, padx = 20)

frame.pack()
master.mainloop()
