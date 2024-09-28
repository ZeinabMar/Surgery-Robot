#import
#--------------------------------------------------------------------------------------------------------------------------------
import socket
import subprocess
import time
import math
from multiprocessing import Process,Value
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import ImageTk
from PIL import Image

#tarif kardan tavabee
#-------------------------------------------------------------------------------------------------------------------------------
def recivedata(xr,yr,xl,yl,error,error1,Clutch,a,roboterror,checkerrorvar,pre_connectionstatus,connectionstatus,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance,scale,timer,prevtimer,PositionSound,LGraspLck,RGraspLck,ArmsAreClosToEachother,RightArmIsCloseToLens,LeftArmIsCloseToLens): 
   
    def connect1(sock,ip,port):
        try:
            sock.connect((ip,port))
            print("Connected to surgery :)")
            
        except:    
            return 0
        return 1
    def dataspilit(data):
        aa=data.split(str.encode("[END]"))
        n=0
        while aa[n]:
            b[n]=aa[n].split(str.encode("/"))
            n=n+1
        return
    def convertfloat():
        n=d=0
        k=1
        while k:
            while d<21:
                b[n][d]=float(b[n][d])
                d=d+1
            n=n+1
            d=0
            k=int((float(b[n][0]))*math.pow(10,18))
        return
    def sumdata(a1,ce,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2,a3,a4,t,t2,t3):
       data=str(a1)+"/"+str(ce)+"/"+str(b1)+"/"+str(c1)+"/"+str(d1)+"/"+str(e1)+"/"+str(f1)+"/"+str(a2)+"/"+str(b2)+"/"+str(c2)+"/"+str(d2)+"/"+str(e2)+"/"+str(f2)+"/"+str(a3)+"/"+str(a4)+"/"+str(t)+"/"+str(t2)+"/"+str(t3)+"[END]" 
       return data

    def errordata(data):
        if data==str.encode("error"):
            #print("Application in server has error, please fix it...")
            time.sleep(0.5)
            #print("Retrying....")
            error.value=3
            data=sock.recv(128)
            if data==str.encode("ok"):
                #print("")
                error.value=0
            return 1
        return 0
                    

#-----------------------------------------------------------------------------------------------------------------------------
#recive data main:
    z=i=a1=b1=c1=d1=e1=f1=a2=b2=c2=d2=e2=f2=a3=a4=bb=t=t2=t3=t4=0
    print("Trying to connect...")
    while True:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip1=socket.gethostbyname("192.168.17.2")
        port1=9996
        sock.settimeout(20)
        if connect1(sock,ip1,port1)==1:
            error.value=0
            connectionstatus.value=0
            pre_connectionstatus.value=connectionstatus.value

            
        #sock.close()
            while True:
                try:
                    while True:
                        
                        if error1.value==1:
                            break
                        tt=1
                        b=[[0 for j in range (21)]for i in range(21)]
                        
                        a1=a.value
                        data=sock.recv(1024)
                        #sock.sendall(str.encode(sumdata(a1,checkerrorvar.value,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2,a3,a4,t,t2,t3)))
                        #print("Hey")
                        checkerrorvar.value = 0
                        #print(5)
                        if errordata(data)==1:
                            data=sock.recv(8192)
                        dataspilit(data)
                        convertfloat()
                       

        #global data transfer---------------------------------------------------------------------------------------------------------
                        #tic=time.time
                        xl.value=b[0][0]
                        yl.value=b[0][1]
                        xr.value=b[0][2]
                        yr.value=b[0][3]
                        Clutch.value=b[0][4]
                        SlvCntrl.value=b[0][5]
                        LeftLoadCell.value=b[0][6]
                        RightLoadCell.value=b[0][7]
                        SystemState.value=b[0][8]
                        LeftConstWrist.value=b[0][9]
                        RightConstWrist.value=b[0][10]
                        LeftVirtualClutch.value=b[0][11]
                        RightVirtualClutch.value=b[0][12]

                        Distance.value=b[0][13]
                        scale.value=b[0][14]
                        timer.value=timer.value+1#b[0][15]
                        RGraspLck.value=b[0][15]
                        LGraspLck.value=b[0][16]
                        ArmsAreClosToEachother.value=b[0][17]
                        RightArmIsCloseToLens.value=b[0][18]
                        LeftArmIsCloseToLens.value=b[0][19]
                        roboterror.value=b[0][20]
                        
                        VoiceCheck=100
                        
                        #print(connectionstatus.value)
                        #a.value=5
                        if pre_connectionstatus.value-connectionstatus.value!=0:
                            
                            
                            break
                        message = str(a.value)
                      
                        sock.send(message.encode('utf_8'))
                        
                        #toc=time.time
                        #print(toc-tic)
                        #SystemState.value=1
                        
                    #print(2)    #
                        #print(SlvCntrl.value)
        #-----------------------------------------------------------------------------------------------------------------------------    
                except:
                        
                    print('problem')    
                    sock.close()
                    break
        if error1.value==1:
            sock.close()
            break
    return
#-----------------------------------------------------------------------------------------------------------------------------
def recivedata2(xr,yr,xl,yl,error,error1,Clutch,a,roboterror,checkerrorvar,pre_connectionstatus,connectionstatus,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance,scale,timer,prevtimer2,PositionSound,LGraspLck,RGraspLck,ArmsAreClosToEachother,RightArmIsCloseToLens,LeftArmIsCloseToLens): 
   
    

#-----------------------------------------------------------------------------------------------------------------------------
#recive data main:
    def connect(sock,ip,port):
        try:
            sock.connect((ip,port))
            print("Connected  to simulation:)")
            
        except:    
            return 0
        return 1
    def dataspilit(data):
        aa=data.split(str.encode("[END]"))
        n=0
        while aa[n]:
            b[n]=aa[n].split(str.encode("/"))
            n=n+1
        return
    def convertfloat():
        n=d=0
        k=1
        while k:
            while d<21:
                b[n][d]=float(b[n][d])
                d=d+1
            n=n+1
            d=0
            k=int((float(b[n][0]))*math.pow(10,18))
        return
    def sumdata(a1,ce,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2,a3,a4,t,t2,t3):
       data=str(a1)+"/"+str(ce)+"/"+str(b1)+"/"+str(c1)+"/"+str(d1)+"/"+str(e1)+"/"+str(f1)+"/"+str(a2)+"/"+str(b2)+"/"+str(c2)+"/"+str(d2)+"/"+str(e2)+"/"+str(f2)+"/"+str(a3)+"/"+str(a4)+"/"+str(t)+"/"+str(t2)+"/"+str(t3)+"[END]" 
       return data

    def errordata(data):
        if data==str.encode("error"):
            #print("Application in server has error, please fix it...")
            time.sleep(0.5)
            #print("Retrying....")
            error.value=3
            data=sock.recv(128)
            if data==str.encode("ok"):
                #print("")
                error.value=0
            return 1
        return 0
                    

#-----------------------------------------------------------------------------------------------------------------------------
#recive data main:
    z=i=a1=b1=c1=d1=e1=f1=a2=b2=c2=d2=e2=f2=a3=a4=bb=t=t2=t3=t4=0
    #print("Trying to connect...")
    while True:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip=socket.gethostbyname("192.168.17.1")
        port=9992
        sock.settimeout(20)
        if connect(sock,ip,port)==1:
            error.value=0
            connectionstatus.value=1
            pre_connectionstatus.value=connectionstatus.value

            
        #sock.close()
            while True:
                                    
                
                
                try:
                    while True:
                        
                        if error1.value==1:
                            break
                        tt=1
                        b=[[0 for j in range (21)]for i in range(21)]
                        
                              
                        a1=a.value
                        data=sock.recv(1024)
                        
                        #sock.sendall(str.encode(sumdata(a1,checkerrorvar.value,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2,a3,a4,t,t2,t3)))
                        #print("Hey")
                        checkerrorvar.value = 0
                        #print(5)
                        if errordata(data)==1:
                            data=sock.recv(8192)
                        dataspilit(data)
                        convertfloat()
                       

        #global data transfer---------------------------------------------------------------------------------------------------------
                        #tic=time.time
                        xl.value=b[0][0]
                        yl.value=b[0][1]
                        xr.value=b[0][2]
                        yr.value=b[0][3]
                        Clutch.value=b[0][4]
                        SlvCntrl.value=b[0][5]
                        LeftLoadCell.value=b[0][6]
                        RightLoadCell.value=b[0][7]
                        SystemState.value=b[0][8]
                        LeftConstWrist.value=b[0][9]
                        RightConstWrist.value=b[0][10]
                        LeftVirtualClutch.value=b[0][11]
                        RightVirtualClutch.value=b[0][12]
 
                        Distance.value=b[0][13]
                        scale.value=b[0][14]
   
                        timer.value=timer.value+1#b[0][15]
                        RGraspLck.value=b[0][15]
                        LGraspLck.value=b[0][16]
                        ArmsAreClosToEachother.value=b[0][17]
                        RightArmIsCloseToLens.value=b[0][18]
                        LeftArmIsCloseToLens.value=b[0][19]
                        roboterror.value=b[0][20]
                        VoiceCheck=100
                        
                        #print(connectionstatus.value)
                        #a.value=5
                        message = str(a.value)
                        #print(message.encode('utf_8'))
                        sock.send(message.encode('utf_8')) 
                        if pre_connectionstatus.value-connectionstatus.value!=0:
                            
                            
                            break
                        
                        #toc=time.time
                        #print(toc-tic)
                        #SystemState.value=1
                        
                    #print(2)    #
                        #print(SlvCntrl.value)
        #-----------------------------------------------------------------------------------------------------------------------------    
                except:
                        
                        
                    sock.close()
                    break
        if error1.value==1:
            sock.close()
            break
    return
#-----------------------------------------------------------------------------------------------------------------------------
#GUI main:
def gui(show,xr,yr,xl,yl,error,error1,Clutch,a,roboterror,checkerrorvar,connectionstatus,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance,scale,timer,prevtimer,prevtimer2,VoiceCheck,PositionSound,LGraspLck,RGraspLck,ArmsAreClosToEachother,RightArmIsCloseToLens,LeftArmIsCloseToLens):
    reboot_shutdown=False
    
    def send(msg):
        
        sock.send(msg.encode('utf_8'))
    
    def change_text(sys_text):
        canvas.itemconfig(sys_text,text="11")
        

    def create_circle1(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        z=canvasName.create_oval(x0, y0, x1, y1,fill=rgb_hack((67, 67, 84)),outline=rgb_hack((67, 67, 84)),width=3)
        return z
    def create_circle_arc(canvasName, x, y, r, **kwargs):
        if "start" in kwargs and "end" in kwargs:
            kwargs["extent"] = kwargs["end"] - kwargs["start"]
            del kwargs["end"]
        return canvasName.create_arc(x-r, y-r, x+r, y+r, **kwargs)
        
    def create_circle2(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        z=canvasName.create_oval(x0, y0, x1, y1,fill=rgb_hack((0, 200, 250)),outline=rgb_hack((0, 0, 0)),width=3)
        return z
    def create_circle(x, y, r, canvasName):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        z=canvasName.create_oval(x0, y0, x1, y1,fill=rgb_hack((0,254,103)),outline=rgb_hack((0,254,103)),width=3)
        return z
        
    def create_circle3(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        z=canvasName.create_oval(x0, y0, x1, y1,fill=rgb_hack((138, 255, 243)),outline=rgb_hack((138, 255, 243)),width=3)
        return z
  

    def move(obj,canvas,x1,y1,x,y):
        #x1,y1 point of center circle
        #x,y point of input from twincat
        z=canvas.coords(obj)
        #print(x)
        aa=x1+(x*68)-z[0]
#         print(aa)
        #print(xr.value)
        bb=y1+(y*68)-z[1]
        canvas.move(obj,aa-35, bb-35)    
        canvas.update()
        return
    
    def checkroboterror(e):
        VoiceCheck=100
        if e==1.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Master-moved-so-quickly1598081048.mp3')
            pygame.mixer.music.play(loops=0) 
            messagebox.showerror('ERROR','Master moved so quickly')
        if e==2.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Difference-between-desire-and-1598081128.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Difference between desire and actual value on slave is too much')
        if e==3.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/There-is-a-mechanical-stop-for1598081162.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','There is a mechanical stop for robots')
        if e==4.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Some-axis-are-in-error1598081195.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Some axis are in error')
        if e==5.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Too-much-pressure-on-robots1598081223.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Too much pressure on robots')
        if e==6.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Some-of-Master-RLS-got-noisy1598081242.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Some of Master RLS got noisy')
        if e==7.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Some-of-RoClutchens-RLS-got-noisy1598081309.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Some of RoClutchens RLS got noisy')
        if e==8.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Problem-with-connection-of-Mas1598081328.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Problem with connection of Master and Kiosk') 
        if e==9.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Robots-are-in-Out-of-range-pos1598081350.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Robots are in Out of range positions') 
        if e==10.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Too-much-pressure-on-Master1598081367.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Too much pressure on Master')
        if e==11.0:
            pygame.mixer.music.load('/home/pi/Desktop/RaspberryCodes/Master-Motors-over-heated1598081387.mp3')
            pygame.mixer.music.play(loops=0)
            messagebox.showerror('ERROR','Master Motors over heated')    
        checkerrorvar.value = 1
        return

    

    
    def tools():
        #tools event
        pass

    def setting():
        #setting event
        pass

    def view():
        #view event
        pass
    def datashowmode():
        top=Toplevel()
        top.title('Data Show Mode')
        return
   
    def sina():
        reboot1.place(x=w/2-105,y=70)
        shutdown1.place(x=w/2+65,y=70)
        #switch1.place(x=w/2+65,y=70)
        #reset1.place(x=w/2+65,y=110)
        #sinabut.place_forget()
        #sinabut2.place(x=w/2-65,y=0)
    def sina2():
        reboot1.place_forget()
        shutdown1.place_forget()
        #switch1.place_forget()
        #reset1.place_forget()

        #sinabut.place(x=w/2-65,y=0)
        #sinabut2.place_forget()
        
    def shutdown():
        if messagebox.askquestion('Shotdown','Are You Sure To Shotdown?')=="yes":
            cmdCommand = "sudo shutdown -h now"
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
        return
    def reboot():
        if messagebox.askquestion('Reboot','Are You Sure To Reboot?')=="yes":
            cmdCommand = "sudo reboot -h now"
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
        return
    def switch():
        if messagebox.askquestion('Switch','Are You Sure To Switch?')=="yes":
            cmdCommand = "sudo reboot -h now"
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
        return
    def reset():
#        if messagebox.askquestion('Reboot','Are You reseting?')=="yes:
        if connectionstatus.value==0:
            connectionstatus.value=1
        else:
            connectionstatus.value=0
                
                
        i=152
        switch1.place_forget()
        
    def click(event):
        
        
        if event.x>w/2-100 and event.x<w/2+100 and event.y>0 and event.y<70:
            
#             print(show.value)
            if show.value==1:
                show.value=2
                
                reboot1.place(x=w/2-115,y=80)
                shutdown1.place(x=w/2+55,y=80)
            else:
                show.value=1
                
                
                reboot1.place_forget()
                shutdown1.place_forget()
                
        
    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb
    def rgb_hack(rgb):
        return '#%02x%02x%02x' % rgb
    

#window
    root = tk.Tk()
    
    images = []  # to hold the newly created image

    def create_rectangle(x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = root.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            images.append(ImageTk.PhotoImage(image))
            canvas.create_image(x1, y1, image=images[-1], anchor='nw')
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
   # root.attributes("-fullscreen",True)
    w=(root.winfo_screenwidth())
    h=(root.winfo_screenheight())
    #root.geometry("484x807")
    root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
    root.configure(background=rgb_hack((21, 21, 46)))
    
    root.bind('<Button-1>', click)
    
    #root.geometry("484x807")
    root.title('Sina Robot Aplication')
    menubar=tk.Menu(root)
    root.config(menu=menubar)
    root.config(cursor="none")
    pygame.mixer.init()
    canvas = tk.Canvas(root, width=w, height=h, borderwidth=0, highlightthickness=0, bg=rgb_hack((21,21,46)))
    canvas.place(x=0,y=0)
    background = PhotoImage(file='/home/pi/Codes/New/blue_back.png')
    background=background.subsample(1, 1)
    backgroundc=canvas.create_image(w/2-290,h/2-570, anchor=NW, image=background)
    #canvas.itemconfig(backgroundc,state='hidden')
    
    
    #canvas.itemconfig(collisionbackgroundc,state='hidden')
    
    img2 = PhotoImage(file='/home/pi/Codes/New/blueplane2.png')
    img2=img2.subsample(4, 4)
    img2c=canvas.create_image(w/2+15,h/2-380, anchor=NW, image=img2)
    
    img3 = PhotoImage(file='/home/pi/Codes/New/blueplane2.png')
    img3=img3.subsample(4, 4)
    img3c=canvas.create_image(w/2-250,h/2-380,anchor=NW, image=img3)
    
    
    
    
    
    
    #rectangleBlue = PhotoImage(file='/home/pi/Codes/New/r100.png')
    rectangleRed = PhotoImage(file='/home/pi/Codes/New/orange.png')
    rectangleBlue = PhotoImage(file='/home/pi/Codes/New/blue.png')
    
    errorpage1 = PhotoImage(file='/home/pi/Codes/New/Error.png')
    errorpage1=errorpage1.subsample(1, 1)
    errorpage=canvas.create_image(w/2-540,h/2-630, anchor=NW, image=errorpage1)
    canvas.itemconfig(errorpage,state='hidden')

    BrectangleUR=canvas.create_image(w/2+30,h/2-10, anchor=NW, image=rectangleBlue)
    BrectangleUL=canvas.create_image(w/2-180,h/2-10, anchor=NW, image=rectangleBlue)
    BrectangleDR=canvas.create_image(w/2+30,h/2+90, anchor=NW, image=rectangleBlue)
    BrectangleDL=canvas.create_image(w/2-180,h/2+90, anchor=NW, image=rectangleBlue)
    
    RrectangleUR=canvas.create_image(w/2+30,h/2-10, anchor=NW, image=rectangleRed)
    RrectangleUL=canvas.create_image(w/2-180,h/2-10, anchor=NW, image=rectangleRed)
    RrectangleDR=canvas.create_image(w/2+30,h/2+90, anchor=NW, image=rectangleRed)
    RrectangleDL=canvas.create_image(w/2-180,h/2+90, anchor=NW, image=rectangleRed)
    

    sc1=Scale(root,from_=1,to=10,orient='horizontal',resolution=0.1,bg=rgb_hack((21,21,46)),highlightbackground='blue' ,label='Change the scale.',font='mitra' ,length=480,width=100)#,lenght=200

    reboot1=Button(canvas,width=5,height=2,text='reboot',bg=rgb_hack((21,21,46)),bd=0,fg=rgb_hack((80, 170, 127)),command=reboot)

    shutdown1=Button(canvas,width=5,height=2,text='shutdown',bg=rgb_hack((21,21,46)),bd=0,fg=rgb_hack((80, 170, 127)),command=shutdown)
    
    switch1=Button(canvas,width=5,height=2,text='switch',bg=rgb_hack((21,21,46)),bd=0,fg=rgb_hack((80, 170, 127)),command=reset)
    reset1=Button(canvas,width=5,height=2,text='reset',bg=rgb_hack((21,21,46)),bd=0,fg=rgb_hack((80, 170, 127)),command=reset)

    

    
#menubar.....................................................
#tools
   
   
#create circle.................................................................

    Left_Wrist=canvas.create_text(w/2-87,round(0.28*h)+368,fill="white",font=("Times New Roman", 16, "bold"),text=" ")
    Right_Wrist=canvas.create_text(w/2+120,round(0.28*h)+368,fill="white",font=("Times New Roman", 16, "bold"),text=" ")
   
    LeftGrasp=canvas.create_text(w/2-87,round(0.28*h)+265,fill="white",font=("Times New Roman", 16, "bold"),text=" ")
    RightGrasp=canvas.create_text(w/2+120,round(0.28*h)+265,fill="white",font=("Times New Roman", 16, "bold"),text=" ")
    #canvas.create_text(120,10,fill="darkblue",font="mitrea 10 italic bold",text="Left Hand Calibration")
    #canvas.create_text(360,10,fill="darkblue",font="mitrea 10 italic bold",text="Right Hand Calibration")
    
    
    connection= canvas.create_text(w/2+10,h/2+360,fill=rgb_hack((255, 255, 255)),font=("Times New Roman", 16,"bold"),text=" ")

    c3lg=create_circle(w/2-138, round(0.28*h)-35, 35,canvas) 
    c4rg=create_circle(w/2+128, round(0.28*h)-35, 35,canvas) 
    c3l=create_circle2(w/2-138, round(0.28*h)-35, 35,canvas) 
    c4r=create_circle2(w/2+128, round(0.28*h)-35, 35,canvas)
    
    arc2=create_circle_arc(canvas,w/2+132, round(0.28*h), 90, style="arc", outline=rgb_hack((80, 170, 127)), width=20,
                             start=90, end=90)
    arc1=create_circle_arc(canvas,w/2-132, round(0.28*h), 90, style="arc", outline=rgb_hack((80, 170, 127)), width=20,
                               start=90, end=90)
    #,state='hidden')

    l3=canvas.create_text(w/2-113,round(0.28*h)-20,fill="white",font=("Times New Roman", 11, "bold"),text=" ")
    l4=canvas.create_text(w/2-180,round(0.28*h)-20,fill=rgb_hack((80, 170, 127)),font=("Times New Roman", 10, "bold"),text="")
    l5=canvas.create_text(w/2+152,round(0.28*h)-20,fill="white",font=("Times New Roman", 11, "bold"),text=" ")
    l6=canvas.create_text(w/2+82,round(0.28*h)-20,fill=rgb_hack((80, 170, 127)),font=("Times New Roman", 10, "bold"),text="")
    l7=canvas.create_text(w/2,h-320,fill=rgb_hack((80, 170, 127)),font=("Times New Roman", 14, "bold"),text=" ")
    l8=canvas.create_text(w/2+17,h/2-70,fill=rgb_hack((255, 255, 255)),font=("Times New Roman", 16,"bold"),text="Connecting... ")
    l9=canvas.create_text(w/2+7,h/2+280,fill=rgb_hack((255, 255, 255)),font=("Times New Roman", 16, "bold"),text=" ")


   
    box=canvas.create_rectangle(0, 0, w,  h, fill=rgb_hack((21,21,46)), outline=rgb_hack((21,21,46)),width=3)
    #box1=canvas.create_rectangle(0, 0, 28,  h, fill=rgb_hack((0,0,0)), outline=rgb_hack((21,21,46)),width=3)
    #box2=canvas.create_rectangle(0, 0, w,  20, fill=rgb_hack((0,0,0)), outline=rgb_hack((21,21,46)),width=3)

    canvas.itemconfig(box,state='hidden')
    timercircle1=create_circle1(w/2, round(0.4*h), 120,canvas)
    timercircle2=create_circle2(w/2, round(0.4*h), 100,canvas) 
    canvas.itemconfig(timercircle1,state='hidden')
    canvas.itemconfig(timercircle2,state='hidden')

    arc3=create_circle_arc(canvas,w/2, round(0.4*h), 110, style="arc", outline=rgb_hack((200, 0, 0)), width=20,
                               start=90, end=90)
    l10=canvas.create_text(w/2,round(0.4*h),fill=rgb_hack((80, 170, 127)),font=("Times New Roman", 14, "bold"),text=" ")

    #sc1.destroy()
    s=1
    i=0
   
    
   
     
    var1 = tk.IntVar()
    var2 = tk.IntVar()
   
    
    
    root.update()
    while True:

        try:
            root.update()
            
            
        except:
            error1=1
            break
      
#         print("here")
        #time.sleep(0.5)
        #sendmsg('ab')
        try:
            #root.update()
            
            while SystemState.value>-10:
                
                root.update()
                #if connectionstatus.value==1:
                 #   canvas.itemconfig(l90prin,text='Simulator      ')
                #elif connectionstatus.value==0:
                 #   canvas.itemconfig(l90prin,text='Surgical Robot')
                #print(timer.value-prevtimer.value)
                if timer.value-prevtimer.value!=0.0:
                    
                    canvas.itemconfig(box,state='hidden')
                    #connectionstatus.value=0
                    
                    i=0
                    canvas.itemconfig(timercircle1,state='hidden')
                    canvas.itemconfig(timercircle2,state='hidden')
                    canvas.itemconfig(arc3,state='hidden')
                    canvas.itemconfig(l10, text = ' ')
                    #canvas.itemconfig(l90prin,state='normal')
                   
                    #l11.place(x=w/2-40,y=h-400)
                    #reset1.place_forget()
                else:
                    
                    i=i+1
                   # if i>150:
                        
                       # canvas.itemconfig(box,state='normal')
                       # canvas.itemconfig(l90prin,state='hidden')
                       # canvas.itemconfig(timercircle1,state='normal')
                       # canvas.itemconfig(timercircle2,state='normal')
                       # canvas.itemconfig(arc3,state='normal')
                       # canvas.itemconfig(arc3,extent=-(i-150)*2)
                       # canvas.itemconfig(l10, text = 'Check connections ...')
                        
                
                    
                prevtimer.value=timer.value
                
                    #print(i)
                    #print(i%500)
                #print(prevtimer.value) 
                #print(connectionstatus.value)
#                 SystemState.value=1
#                 ArmsAreClosToEachother.value=0
#                 RightArmIsCloseToLens.value=0
#                 LeftArmIsCloseToLens.value=1
                #SystemState.value=0
#                 print("right virtual:")
#                 print(RightVirtualClutch.value)
#                 print("left virtual:")
#                 print(LeftVirtualClutch.value)
                if SystemState.value==0 or SystemState.value==13 or SystemState.value==21:
#                     print('system state is in error')
                    canvas.itemconfig(errorpage, state = 'normal')
                    
                    canvas.itemconfig(BrectangleDL,state='hidden')
                    canvas.itemconfig(RrectangleDL,state='hidden') 
                    canvas.itemconfig(Left_Wrist,state='hidden')
                    canvas.itemconfig(Left_Wrist,state='hidden')
                    canvas.itemconfig(BrectangleDR,state='hidden')
                    canvas.itemconfig(RrectangleDR,state='hidden') 
                    canvas.itemconfig(Right_Wrist,state='hidden')
                    canvas.itemconfig(BrectangleUL,state='hidden')
                    canvas.itemconfig(RrectangleUL,state='hidden') 
                    canvas.itemconfig(LeftGrasp,state='hidden')
                    canvas.itemconfig(BrectangleUR,state='hidden')
                    canvas.itemconfig(RrectangleUR,state='hidden') 
                    canvas.itemconfig(RightGrasp,state='hidden')
                    canvas.itemconfig(c3l,state='hidden')
                    canvas.itemconfig(c4r,state='hidden')
                    canvas.itemconfig(c3lg,state='hidden')
                    canvas.itemconfig(c4rg,state='hidden')
                    canvas.itemconfig(connection,state='hidden')
                    canvas.itemconfig(img2c,state='hidden')
                    canvas.itemconfig(img3c,state='hidden')
                    canvas.itemconfig(l3,state='normal') 
                    canvas.itemconfig(l4,state='normal')
                    canvas.itemconfig(l5,state='hidden') 
                    canvas.itemconfig(l6,state='hidden')
                    canvas.itemconfig(l8,state='hidden')
                    canvas.itemconfig(l10,state='hidden')
                    canvas.itemconfig(arc2,state='hidden')
                    canvas.itemconfig(arc1,state='hidden')
                    canvas.itemconfig(arc3,state='hidden')
                    canvas.itemconfig(box,state='hidden')
                    canvas.itemconfig(backgroundc,state='hidden')
                    #canvas.itemconfig(sc1,state='hidden')
                    #canvas.itemconfig(l9,state='hidden')
                    
#                     if SystemState.value==0:
#                         #canvas.itemconfig(l8, text = 'ERROR')
#                         
#                     if SystemState.value==21:
#                         #canvas.itemconfig(errorpage, state = 'normal')
#                         canvas.itemconfig(l8, text = 'ERROR')    
#                     if SystemState.value==13:
#                         #canvas.itemconfig(l8, text = 'ClearErrors')
#                         canvas.itemconfig(errorpage, state = 'normal')

                else:
#                     print('system state is not error')

                  
                    canvas.itemconfig(backgroundc,state='normal')

                    #LeftVirtualClutch.value=0
                    #LeftLoadCell.value = 0.11
                    
                    
                    print("774")
                    if LeftConstWrist.value==1:
                        print("776")
                        canvas.itemconfig(BrectangleDL,state='hidden')
                        canvas.itemconfig(RrectangleDL,state='normal') 
                        canvas.itemconfig(Left_Wrist, text = ' Wrist is Locked ')
#                         print("line1185")
                    else:
                        print("782")
                        canvas.itemconfig(RrectangleDL,state='hidden')
                        canvas.itemconfig(BrectangleDL,state='normal') 
                        canvas.itemconfig(Left_Wrist, text = '  Flexible Wrist  ')
#                         print("line1190")
                        
                    if RightConstWrist.value==1:
                        canvas.itemconfig(BrectangleDR,state='hidden')
                        canvas.itemconfig(RrectangleDR,state='normal') 
                        canvas.itemconfig(Right_Wrist, text = ' Wrist is Locked ')
                    else:
                        canvas.itemconfig(RrectangleDR,state='hidden')
                        canvas.itemconfig(BrectangleDR,state='normal')
                        canvas.itemconfig(Right_Wrist, text = '  Flexible Wrist  ')
                    
                    #canvas.itemconfig(l7, text = str(math.floor(Distance.value)))
                    
                    canvas.itemconfig(l8, font=("Times New Roman", 16,"bold"))
                    if SystemState.value==-2:
                    
                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                        canvas.itemconfig(errorpage, state = 'hidden')
                        
                    elif SystemState.value==-1:

                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                        canvas.itemconfig(errorpage, state = 'hidden')
 
                    elif SystemState.value==1:
                        
                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                        canvas.itemconfig(errorpage, state = 'hidden')
                    
                    elif SystemState.value==11:
                        
                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                        canvas.itemconfig(errorpage, state = 'hidden')
                    elif SystemState.value==20:
                       
                        canvas.itemconfig(l8, text = 'OPERATION')
                        canvas.itemconfig(errorpage, state = 'hidden')
                    
                    elif SystemState.value==22:
                        canvas.itemconfig(errorpage, state = 'hidden')
                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                    elif SystemState.value==23:
                        canvas.itemconfig(errorpage, state = 'hidden')
                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                    elif SystemState.value==24:
                        canvas.itemconfig(errorpage, state = 'hidden')

                        canvas.itemconfig(l8, text = 'PRE-OPERATION')
                    elif SystemState.value==30:
                        canvas.itemconfig(errorpage, state = 'hidden')

                        canvas.itemconfig(l8, text = 'Changing Instrument')
                    elif SystemState.value==56:
                        canvas.itemconfig(errorpage, state = 'hidden')
                        
                        canvas.itemconfig(l8, text = 'GotoPark')
                    elif SystemState.value==57:
                        canvas.itemconfig(errorpage, state = 'hidden')

                        canvas.itemconfig(l8, text = 'FinishOperation')
                        
                    if connectionstatus.value==1:
                        canvas.itemconfig(l8, text = 'Simulation')
                   

                    #print(LeftLoadCell.value)
        
                    if LeftLoadCell.value > 1:
                        LeftLoadCell.value = 1
                    if LeftLoadCell.value < 0:
                        LeftLoadCell.value = 0
                    if RightLoadCell.value > 1:
                        RightLoadCell.value = 1
                    if RightLoadCell.value < 0:
                        RightLoadCell.value = 0
#                     print("line1268")

                    round_value1 = math.floor((LeftLoadCell.value * 100)/5)*5
                    round_value2 = math.floor((RightLoadCell.value * 100)/5)*5
#                     print("line1272") 
                    #print(RightVirtualClutch.value)
                    connectionstatus.value=0
                    if connectionstatus.value==0:
                        if SlvCntrl.value==1:
                            canvas.itemconfig(connection,text="Slave control")
                        
                        else:
                        
                            canvas.itemconfig(connection,text="Lenz control")
                    else:
                        canvas.itemconfig(connection,text=" ")
                    

                    if Clutch.value==1:
                        #pass    
                        
                        while s:
                            canvas.itemconfig(l9, state = 'hidden')
                            sc1=Scale(root,from_=1,to=10,orient='horizontal',resolution=0.5,bg=rgb_hack((42,45,80)),highlightbackground=rgb_hack((42,45,80)), fg='white', troughcolor='#73B5FA', activebackground='#1065BF' ,font='mitra' ,length=200,width=20)#,lenght=200
                            sc1.place(x=w/2-90,y=h/2+250)
                            sc1.set(scale.value) 
                            s=s-1
                        root.update()
                        a.value=float(sc1.get())
                        #send(str(a.value))
                        #print(str(scale.value))
                        #print(sc1.value)
                    else:
  
                        sc1.destroy()
                        s=1
                        canvas.itemconfig(l9, state = 'normal')
                        canvas.itemconfig(l9, text = str((scale.value)))
                    #send("5")
                    
                   
                    #print(yl.value-350)
#                     print("line1315")
                    
                     # Smaller Circle
                    if LGraspLck.value==1:
                         canvas.itemconfig(BrectangleUL,state='hidden')
                         canvas.itemconfig(RrectangleUL,state='normal') 
                         canvas.itemconfig(LeftGrasp,text='Grasp is locked')
                    else:
                         canvas.itemconfig(RrectangleUL,state='hidden')
                         canvas.itemconfig(BrectangleUL,state='normal') 
                         canvas.itemconfig(LeftGrasp,text='Grasp is free')
                         
                    if RGraspLck.value==1:
                         canvas.itemconfig(BrectangleUR,state='hidden')
                         canvas.itemconfig(RrectangleUR,state='normal') 
                         canvas.itemconfig(RightGrasp,text='Grasp is locked')
                    else:
                         canvas.itemconfig(RrectangleUR,state='hidden')
                         canvas.itemconfig(BrectangleUR,state='normal') 
                         canvas.itemconfig(RightGrasp,text='Grasp is free')
#                     print("line1350")    
                    if LeftVirtualClutch.value==1:
                     
                        print("926")
                        canvas.itemconfig(img3c,state='normal')
                        canvas.itemconfig(c3lg,state='hidden')
                        canvas.itemconfig(c3l,state='normal')

                        canvas.itemconfig(l3,state='hidden') 
                        canvas.itemconfig(l4,state='hidden')
                    
                        #canvas.itemconfig(c33l,state='hidden')   
                        #canvas.itemconfig(arc1,state='hidden')
                        
                        move(c3l,canvas,w/2-138,round(0.28*h)-35,xl.value,yl.value)
                            
                    else:
#                         print("line1367")
                      
                        canvas.itemconfig(c3l,state='hidden')
                        canvas.itemconfig(c3lg,state='normal')
                        
                        #canvas.itemconfig(c33l,fill=rgb_hack((85, 85, 127)),outline=rgb_hack((85, 85, 127)))   
                        canvas.itemconfig(l3,state='normal') 
                        canvas.itemconfig(l4,state='normal')
                        #canvas.itemconfig(c3l,state='hidden')  
                        canvas.itemconfig(arc1,state='hidden')  
                        #canvas.itemconfig(arc1,extent=-round_value1*3.6)
                        #canvas.itemconfig(arc1,outline=rgb_hack((round((LeftLoadCell.value)*250), 250-round((LeftLoadCell.value)*250), 0)))
                        canvas.itemconfig(c3l,state='hidden')
                        #canvas.itemconfig(arc1,outline=rgb_hack((200, 0, 0)))
                        
                        #extendarc(arc1,canvas,end=90-round_value1*3.6)

                       
                    
                        #canvas.itemconfig(c3l,fill=rgb_hack((85,85,127)))
                        #canvas.itemconfig(c1l,fill=rgb_hack((67,67,84)))
#                     print("line1409")
                    if RightVirtualClutch.value==1:
                        print(963)
                        canvas.itemconfig(img2c,state='normal')
                        canvas.itemconfig(c4rg,state='hidden')
                        canvas.itemconfig(c4r,state='normal')
                        
                        #canvas.itemconfig(c43r,state='hidden')   

                        canvas.itemconfig(l5,state='hidden') 
                        canvas.itemconfig(l6,state='hidden')
                        canvas.itemconfig(arc2,state='hidden')
                        move(c4r,canvas,w/2+128,round(0.28*h)-35,xr.value,yr.value)
                        #move(c4r,canvas,xr.value-(-(w/2+132)),yr.value-(-round(0.28*h)),20)
                        #w/2+132, round(0.28*h)
                            
                            
                    else:
                        print(979)
                        canvas.itemconfig(c4r,state='hidden')
                        print(981)
                        canvas.itemconfig(c4rg,state='normal')
                        
                        #canvas.itemconfig(c43r,fill=rgb_hack((85, 85, 127)),outline=rgb_hack((85, 85, 127)))

                        #canvas.itemconfig(c4r,state='hidden') 
                        canvas.itemconfig(l5,state='normal') 
                        canvas.itemconfig(l6,state='normal')
                        #canvas.itemconfig(c4r,fill=rgb_hack((21,21,46)))
                        #canvas.itemconfig(c2r,fill=rgb_hack((21,21,46)))                    
                        canvas.itemconfig(arc2,state='hidden')  

                        #canvas.itemconfig(arc2,extent=-round_value2*3.6)
                       # canvas.itemconfig(arc2,outline=rgb_hack((round((RightLoadCell.value)*250), 250-round((RightLoadCell.value)*250), 0)))
                        #canvas.itemconfig(arc2,outline=rgb_hack((round_value2*250/100, 250-round_value2*250/100, 0)))
                        #extendarc(arc2,canvas,end=90-round_value2*3.6)
                        canvas.itemconfig(c4r,state='hidden')
#                         print("line1466")
    
        except:
            #print(6)
            error1.value=1
            #break
            
    return
    root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------------
#multiprosess
if __name__=='__main__':
#globl value------------------------------------------------------------------------------------------------------------------
    xr=Value('d',0.0)
    yr=Value('d',0.0)
    zr=Value('d',0.0)
    xl=Value('d',0.0)
    yl=Value('d',0.0)
    zl=Value('d',0.0)
    Clutch=Value('d',0.0)
    error=Value('d',0.0)
    error1=Value('d',0.0)
    a=Value('d',0.0)
    connectionstatus=Value('d',0.0)
    SlvCntrl=Value('d',0.0)
    roboterror=Value('d',0.0)
    checkerrorvar=Value('d',0.0)
    LeftLoadCell=Value('d',0.)
    RightLoadCell=Value('d',0.2)
    SystemState=Value('d',-30.0)
    LeftVirtualClutch=Value('d',0.0)
    RightVirtualClutch=Value('d',1.0)
    LeftConstWrist=Value('d',0.0)
    RightConstWrist=Value('d',0.0)
    pre_connectionstatus=Value('d',0.0)
    prerightcirclevis=Value('d',0.0)
    preleftcirclevis=Value('d',0.0)
    Distance=Value('d',0.0)
    scale=Value('d',1.0)
    timer=Value('d',0.0)
    prevtimer=Value('d',0.0)
    prevtimer2=Value('d',0.0)

    PositionSound=Value('d',0.0)
    show=Value('d',0.0)
    VoiceCheck=100
    LGraspLck=Value('d',1.0)
    RGraspLck=Value('d',0.0)
    ArmsAreClosToEachother=Value('d',0.0)
    RightArmIsCloseToLens=Value('d',0.0)
    LeftArmIsCloseToLens=Value('d',0.0)
   
#-----------------------------------------------------------------------------------------------------------------------------
    p3=Process(target=recivedata,args=(xr,yr,xl,yl,error,error1,Clutch,a,roboterror,checkerrorvar,pre_connectionstatus,connectionstatus,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance,scale,timer,prevtimer,PositionSound,LGraspLck,RGraspLck,ArmsAreClosToEachother,RightArmIsCloseToLens,LeftArmIsCloseToLens))
    p1=Process(target=recivedata2,args=(xr,yr,xl,yl,error,error1,Clutch,a,roboterror,checkerrorvar,pre_connectionstatus,connectionstatus,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance,scale,timer,prevtimer2,PositionSound,LGraspLck,RGraspLck,ArmsAreClosToEachother,RightArmIsCloseToLens,LeftArmIsCloseToLens))

    p2=Process(target=gui,args=(show,xr,yr,xl,yl,error,error1,Clutch,a,roboterror,checkerrorvar,connectionstatus,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance,scale,timer,prevtimer,prevtimer2,VoiceCheck,PositionSound,LGraspLck,RGraspLck,ArmsAreClosToEachother,RightArmIsCloseToLens,LeftArmIsCloseToLens))
    
    #p3=Process(target=sendmsg,args=(xr,yr,xl,yl,Clutch,a,SlvCntrl,LeftLoadCell,RightLoadCell,SystemState,LeftConstWrist,RightConstWrist,LeftVirtualClutch,RightVirtualClutch,Distance))
    p1.start()
    p3.start()
    p2.start()
    p3.join()
    p1.join()
    p2.join()
    print("Everything is OK")
   






