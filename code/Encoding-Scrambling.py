import matplotlib.pyplot as plt
import numpy as np

def display(raw_code,title,time_interval=10,time_type=None):
    code=[]
    time=[]
    new_code=[]
    new_time=[]
    beg=1
    end=beg+time_interval
    
    for i in range(len(raw_code)):
        time.append(np.arange(beg,end))
        if i==0:
            code.append(np.array([raw_code[i]]*time_interval))
        else:
            code.append(np.array([raw_code[i]]*(time_interval+1)))

        beg=end-1
        end+=time_interval
        
        
    time=np.array(time)
    code=np.array(code)

    for i in range(len(raw_code)):
        for j,k in zip(code[i],time[i]):
            new_code.append(j)
            new_time.append(k)
            
    if time_type=='half':
        length=len(raw_code)//2
    else:
        length=len(raw_code)
        
    for i in range(length):
        plt.plot([(i+1)*10,(i+1)*10],[-1.5,1.5],linestyle=':',color='k')
        
    
    plt.plot([1,1],[-2,2],color = 'k')
    plt.plot([1,len(new_time)],[0,0],color ='k')
    plt.plot(new_time,new_code,color = 'r')
    plt.title(title)
    plt.show()
    
def unipolar(code_string):
    code=np.array(list(code_string),dtype=np.int)
    display(code,title='Unipolar')
    
def polar_NRZ_L(code_string):
    code=np.array(list(code_string),dtype=np.int)
    code[code==0]=-1
    display(code,title='Polar NRZ-L')
    
def polar_NRZ_I(code_string):
    code=np.array(list(code_string),dtype=np.int)
    
    for i in range(1,len(code)):
        if (code[0]=='0'or code[0]==0):
            code[0]=-1        
                        
        if code[i]==0:
            code[i]=code[i-1]
        else:
            if code[i-1]==-1:
                code[i]=1
            else:
                code[i]=-1
    display(code,title='Polar NRZ-I')
    
def AMI(code_string):
    code=np.array(list(code_string),dtype=np.int)
    temp=[]
    flag=1
    for i in range(len(code)):
        if code[i]==1:
            temp.append(flag)
            #temp.append(0)
            flag=-1*flag
        else:
            temp.append(0)
            #temp.append(0)
    code=temp
    display(code,title='AMI')
    

def B8ZS(code_string):
    s1=code_string.replace("00000000","000vb0vb")
    #print(s1)
    code=np.array(list(s1))
    #print(code)
    temp=[]
    flag=1
    for i in range(len(code)):
        if code[i]=='1'or code[i]=='b' :
            temp.append(flag)
            m = flag
            flag=-1*flag
            
        elif code[i]=='v':
            temp.append(m)
            
            
            
        else:
            temp.append(0)
            
    code=temp
    display(code,title='B8ZS')
    
def HDB3(code_string):
    s=code_string.replace("0000","xxxx")
    code1=np.array(list(s))
    
    m=0
    for i in range(len(code1)):
        if code1[i]=='1':
            m=m+1
            
        elif code1[i]=='x':
            if m%2 == 0:
                code1[i]='b'
                code1[i+1]='0'
                code1[i+2]='0'
                code1[i+3]='v'
                m=m+2
            else :
                code1[i]='0'
                code1[i+1]='0'
                code1[i+2]='0'
                code1[i+3]='v'
                m=m+1
        else:
            continue
        #print(code1)
        code = code1
        #s1=s        
                
        #breaks after counting the no of ones before 1st set 
    
    #code=np.array(list(s1))
    #print(code)
    temp=[]
    flag=1
    for i in range(len(code)):
            if code[i]=='1' or code[i]=='b' :
                temp.append(flag)
                m = flag
                flag=-1*flag
            
            elif code[i]=='v':
                temp.append(m)
                
            
            
            else:
                temp.append(0)
                
    code=temp
        
    display(code,title='HDB3')    


def manchester(code_string):
    code=np.array(list(code_string),dtype=np.int)
    temp=[]
    
    for i in range(len(code)):
        if code[i]==1:
            temp.append(-1)
            temp.append(1)
        else:
            temp.append(1)
            temp.append(-1)
    code=temp
    display(code,title='Manchester',time_interval=5,time_type='half')

def differential_manchester(code_string):
    code=np.array(list(code_string),dtype=np.int)
    temp=[]
    flag1=1
    flag2=-1
    for i in range(len(code)):
        
        if i==0 and code[0]==0:
            flag1=1
            flag2=-1
            temp.append(flag1)
            temp.append(flag2)
            i=i+1
        
        elif i==0 and code[0]==1:
            flag1=-1
            flag2=1
            temp.append(flag1)
            temp.append(flag2)
            i=i+1
                          
        elif code[i]==1:
                flag1 = -1*flag1
                flag2 = -1*flag2
                temp.append(flag1)
                temp.append(flag2)
                
        elif code[i]==0:
                temp.append(flag1)
                temp.append(flag2)
               
                
       
    
    code=temp
    display(code,title='Differential Manchester',time_interval=5,time_type='half')

   
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import keras
import numpy as np
from sklearn.preprocessing import StandardScaler

root = Tk()
root.geometry('1500x1500')
root.title("Prediction Form")

label = Label(root, text="Line Coding",width=20,font=("bold", 30))
label.place(x=375,y=20)


label_1 = Label(root, text="DATA BITS: ",width=20,font=("bold", 12))
label_1.place(x=350,y=100)
entry_1 = Entry(root)
entry_1.place(x=550,y=100)



label_5 = Label(root, text="Type of Encoding",width=20,font=("bold", 12))
label_5.place(x=350,y=170)
global var5
var5 = IntVar()
Radiobutton(root, text="Unipolar NRZ",padx = 5, variable=var5, value=0).place(x=650,y=170)
Radiobutton(root, text="NRZ-I",padx = 5, variable=var5, value=1).place(x=650,y=200)
Radiobutton(root, text="NRZ-L",padx = 20, variable=var5, value=2).place(x=635,y=230)
Radiobutton(root, text="Manchester",padx = 5, variable=var5, value=3).place(x=650,y=260)
Radiobutton(root, text="Differential Manchester",padx = 20, variable=var5, value=4).place(x=635,y=290)
Radiobutton(root, text="AMI",padx = 20, variable=var5, value=5).place(x=635,y=320)



label_9 = Label(root, text="Scrambling Schemes(For AMI):",width=24,font=("bold", 12))
label_9.place(x=350,y=370)
global var9
var9 = IntVar()
Radiobutton(root, text="None",padx = 5, variable=var9, value=0).place(x=650,y=370)
Radiobutton(root, text="B8ZS",padx = 20, variable=var9, value=1).place(x=635,y=400)
Radiobutton(root, text="HDB3",padx = 5, variable=var9, value=2).place(x=650,y=430)

def client_exit():
        root.destroy()

def show_result():
    
        i1 = str(entry_1.get())
        i5 = int(var5.get())
        i9 = int(var9.get())
        print(i1)
        if i5 == 1:
            polar_NRZ_I(i1)
        elif i5 == 2:
            polar_NRZ_L(i1)
        elif i5 == 3:
            manchester(i1)
        elif i5 == 4:
            differential_manchester(i1)
        elif i5 == 5:
            if i9 == 0:
                AMI(i1)
            elif i9 == 1:
                B8ZS(i1)
            elif i9 == 2:
                HDB3(i1)
        elif i5 == 0:
            unipolar(i1)
        root.destroy()
                
            
        
        #tk.messagebox.showinfo( "Prediction", pred )
        #tk.graph.showgraph( polar_NRZ_I(i1))
    
Button(root, text='Submit',width=20,bg='brown',fg='white', command = show_result).place(x=550,y=550)
#Button(root, text='EXIT',width=20,bg='brown',fg='white', command = client_exit).place(x=550,y=600)



root.mainloop()
