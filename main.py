import serial
import time
import datetime
import os
import numpy as np
import sys
import ipcam_yolo as iy
from tkinter import*
from multiprocessing import Process, Queue

class arduino_interface:
    '''
    Created by Steven Smiley on 11/27/2022
    
    This class interfaces with an arduino nano 
    to send servo motors (connected to the arduino nano) signals it can interpet via serial to move.

    This 

    '''
    def __init__(self,USB_NAME='/dev/Arduino',baudrate=115200):
        self.USB_NAME=USB_NAME
        self.baudrate=baudrate
        self.UP=30#120#140
        self.DOWN=150#60#20
        self.MIDDLE=90
        self.initalize_usb()

    def initalize_usb(self):
        os.system(f'ls {self.USB_NAME} >ff.txt')
        f=open('ff.txt','r')
        f_read=f.readlines()
        f.close()
        os.system('rm ff.txt')
        for line in f_read:
            print(line)
            try:
                line=line.strip()
                self.ser=serial.Serial(line,115200,timeout=5) #change ACM number as found from ls /dev/tty/ACM*
                #print(ser) 
                break
            except:
                pass
        self.ser.baudrate=self.baudrate


    def enc(self,message):
        print(message)
        self.ser.write(message.encode())
        print(message,' sent')


    def servo_to(self,x):
        servo_write=str(x)
        servo_write='serv1&'+servo_write.strip()+':;\n'
        self.enc(servo_write)

    def servos_UP(self):
        x=self.UP
        servo_1=str(x)
        servo_2=str(self.comp(x))
        servo_write='serv1&'+servo_1.strip()+':'
        servo_write=servo_write+'serv2&'+servo_2.strip()+':\r\n'
        self.enc(servo_write)

    def servos_DOWN(self):
        x=self.DOWN
        servo_1=str(x)
        servo_2=str(self.comp(x))
        servo_write='serv1&'+servo_1.strip()+':'
        servo_write=servo_write+'serv2&'+servo_2.strip()+':\r\n'
        self.enc(servo_write)

    def servos_RIGHT(self):
        x=self.DOWN
        servo_1=str(x)
        servo_2=str(self.MIDDLE)
        servo_write='serv1&'+servo_1.strip()+':'
        servo_write=servo_write+'serv2&'+servo_2.strip()+':\r\n'
        self.enc(servo_write)

    def servos_LEFT(self):
        x=self.UP
        servo_1=str(x)
        servo_2=str(self.MIDDLE)
        servo_write='serv1&'+servo_1.strip()+':'
        servo_write=servo_write+'serv2&'+servo_2.strip()+':\r\n'
        self.enc(servo_write)

    def servos_STOP(self):
        x=self.MIDDLE
        servo_1=str(x)
        servo_2=servo_1
        servo_write='serv1&'+servo_1.strip()+':'
        servo_write=servo_write+'serv2&'+servo_2.strip()+':\r\n'
        self.enc(servo_write)


    def comp(self,y):
        y=abs(180-y)
        return y



    def servo_loop(self):
        valid_ints=list(np.arange(0,180))
        while True:
            answer=input('Where do you want the servo?\n')
            answer=answer.replace('\n','').replace(' ',"")
            try:
                answer=int(answer)
                if int(answer) in valid_ints:
                    self.servo_to(str(answer))
                else:
                    print(f'Not a valid value:\n {str(answer)}')
            except:
                print(f'Not a valid value:\n {str(answer)}')
                pass

    def control_ai(self,target='Steven',img_size=640,path_weights="weights/best.pt"):
        '''This is an autonmous control of the servos through YOLOv7'''
        self.q=Queue()
        self.img_size=img_size
        self.path_weights=path_weights
        self.p1=Process(target=iy.main,args=(self.q,self.img_size,self.path_weights,))
        self.p1.start()
        self.target=target
        while True:
            try:
                self.detections_i=self.q.get()
                detected=False
                for det in self.detections_i:
                    if str(det).find(self.target)!=-1:
                        detected=True
                        name,xmin,ymin,xmax,ymax,conf,h,w=det
                        xc=(xmax+xmin)/2.
                        fc=w/2. 
                        d_x=(xc)/w
                        print('xc',xc,'fc',fc,'d_xf',d_x)
                        THRESH=0.8
                        if d_x>THRESH:
                            self.servos_LEFT()
                        elif d_x<(1-THRESH):
                            self.servos_RIGHT()
                        elif d_x<THRESH and d_x>(1-THRESH):
                            self.servos_UP()
                        else:
                            self.servos_STOP()
                        break
                if detected==False:
                    self.servos_STOP()
            except:
                pass

        
    def control_servo_keyboard(self):
        '''This is a manual control of the servos through the keyboard'''
        import tkinter as tk
        from tkinter import Tk
        self.Tk=Tk()
        self.frame=tk.Frame(self.Tk,width=100,height=100)
        self.Tk.bind('<Left>',self.leftKey)
        self.Tk.bind('<Right>',self.rightKey)
        self.Tk.bind('<Up>',self.upKey)
        self.Tk.bind('<Down>',self.downKey)
        self.Tk.bind('s',self.stopKey)
        self.frame.pack()
        self.Tk.mainloop()

    
    def upKey(self,event):
        self.servos_UP()
    def downKey(self,event):
        self.servos_DOWN()
    def leftKey(self,event):
        self.servos_LEFT()
    def rightKey(self,event):
        self.servos_RIGHT()
    def stopKey(self,event):
        self.servos_STOP()
    

if __name__=='__main__':
    case=3
    ai=arduino_interface()
    if case==1:
        '''Test a specific input command for a servo or servos'''
        ai.servo_loop()
    elif case==2:
        '''Test the manual control of the servos through the keyboard up/down/left/right and "s" for stop etc'''
        run='y'
        while run=='y':
            try:
                ai.control_servo_keyboard()
            except:
                ai.Tk.destroy()
                ai.initalize_usb()
                run=input('Want to run again?\n')
                run=run[0].lower()
    elif case==3:
        '''This is a autonmous control of the servos using YOLOv7 as optical input'''
        p2=Process(target=ai.control_ai,args=('Steven',640,))
        p2.start()


