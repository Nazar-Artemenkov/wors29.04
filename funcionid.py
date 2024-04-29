from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def Vaal():

    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1**2-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2**2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=-0.75*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=-0.5*(x8+13)**2+3
    x9=np.arange(-15,-9.5,0.5) 
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,"b-",x2,y2,"b-",x3,y3,"b-",x4,y4,"b-",x5,y5,"r-",x6,y6,"r-",x7,y7,"b-",x8,y8,"b-",x9,y9,"b-",x10,y10,"k-")
    plt.title("Vaal")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()
def Prillid():
    x1=np.arange(-9,-0.5,0.5)
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-0.5,0.5)
    y3=(1/4)*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=(1/4)*(x4-5)**2-3
    x5=np.arange(-9,-6,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=-0.5*x7**2+1.5
    plt.figure()
    plt.plot(x1,y1,"g-",x2,y2,"g-",x3,y3,"g-",x4,y4,"g-",x5,y5,"g-",x6,y6,"g-",x7,y7,"g-")
    plt.title("Prillid")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()
def Vihmavari():
    x1=np.arange(-12,12,0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4,4.5,0.5)
    y2=(-1/8)*x2**2+6
    x3=np.arange(-12,-3.5,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,12,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,0.5,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,1,0.5)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    plt.plot(x1,y1,"r-",x2,y2,"m-",x3,y3,"y-",x4,y4,"y-",x5,y5,"g-",x6,y6,"g-")
    plt.title("Vihmavari")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()
def Liblikas():
    x1=np.arange(-9,-0.5,0.5)
    y1=(-1/8)*(x1+9)**2+8
    x2=np.arange(1,9,0.5)
    y2=(-1/8)*(x2-9)**2+8
    x3=np.arange(-9,-7.5,0.5)
    y3=7*(x3+8)**2+1
    x4=np.arange(8,9.5,0.5)
    y4=7*(x4-8)**2+1
    x5=np.arange(-8,-1,0.5)
    y5=(1/49)*(x5+1)**2
    x6=np.arange(1,8,0.5)
    y6=(1/49)*(x6-1)**2
    x7=np.arange(-8,-0.5,0.5)
    y7=(-4/49)*(x7+1)**2
    x8=np.arange(1,8.5,0.5)
    y8=(-4/49)*(x8-1)**2
    x9=np.arange(-8,-1.5,0.5) 
    y9=(1/3)*(x9+5)**2-7
    x10=np.arange(2,8.5,0.5)
    y10=(1/3)*(x10-5)**2-7
    x11=np.arange(-2,-0.5,0.5)
    y11=-2*(x11+1)**2-2
    x12=np.arange(1,2.5,0.5)
    y12=-2*(x12-1)**2-2
    x13=np.arange(-1,1.5,0.5)
    y13=-4*x13**2+2
    x14=np.arange(-1,1.5,0.5)
    y14=4*x14**2-6
    x15=np.arange(-2,0.5,0.5)
    y15=-1.5*x15+2
    x16=np.arange(0,2.5,0.5)
    y16=1.5*x16+2
    plt.figure()
    plt.plot(x1,y1,"m-s",x2,y2,"m-s",x3,y3,"m-s",x4,y4,"m-s",x5,y5,"m:s",x6,y6,"m:s",x7,y7,"m-s",x8,y8,"m-s",x9,y9,"m-s",x10,y10,"m-s",x11,y11,"m-s",x12,y12,"m-s",x13,y13,"r-.*",x14,y14,"r-.*",x15,y15,"b-",x16,y16,"b-")
    plt.title("Liblikas")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()
def Kilpkonn():
    x1=np.arange(-7,7,0.5)
    y1=(-3/49)*x1**2+8
    x2=np.arange(-7,7,0.5)
    y2=(4/49)*x2**2+1
    x3=np.arange(-6.8,-2,0.5)
    y3=-0.75*(x3+4)**2+11
    x4=np.arange(2,6.8,0.5)
    y4=-0.75*(x4-4)**2+11
    x5=np.arange(-5.8,-2.8,0.5)
    y5=-(x5+4)**2+9 
    x6=np.arange(2.8,5.8,0.5)
    y6=-(x6-4)**2+9 
    x7=np.arange(-4,4.5,0.5)
    y7=(4/9)*x7**2-5
    x8=np.arange(-5.2,5.5,0.5)
    y8=(4/9)*x8**2-9
    x9=np.arange(-7,-2.8,0.5)
    y9=(-1/16)*(x9+3)**2-6
    x10=np.arange(2.8,7,0.5)
    y10=(-1/16)*(x10-3)**2-6
    x11=np.arange(-7,0,0.5)
    y11=(1/9)*(x11+4)**2-11
    x12=np.arange(0,7,0.5)
    y12=(1/9)*(x12-4)**2-11
    x13=np.arange(-7,-4,0.5)
    y13=-(x13+5)**2
    x14=np.arange(4.5,7.5,0.5)
    y14=-(x14-5)**2
    x15=np.arange(-3,3,0.5)
    y15=(2/9)*x15**2+2
    plt.figure()
    plt.plot(x1,y1,"m-s",x2,y2,"m-s",x3,y3,"m-s",x4,y4,"m-s",x5,y5,"m-s",x6,y6,"m-s",x7,y7,"m-s",x8,y8,"m-s",x9,y9,"m-s",x10,y10,"m-s",x11,y11,"m-s",x12,y12,"m-s",x13,y13,"r-s",x14,y14,"r-s",x15,y15,"r-s")
    plt.title("Kilpkonn")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()


def valik(event):
    selected_item = loetelu.get(loetelu.curselection())
    ask_to_show(selected_item)
def ask_to_show(name):
    response = messagebox.askyesno("jah", f"tahate et ma tegin lahti pilti? '{name}'?")
    if response:
        eval(f"{name}()")
aken = Tk()
aken.geometry("400x500")
aken.title("vali figuur")
aken.configure(bg="#4b09d9")
Label(aken, text="Vali figuur", font=("Arial", 20), bg="#4b09d9", fg="white").pack(pady=10)
l = ["Vaal", "Vihmavari", "Liblikas", "Prillid", "Kilpkonn"]
loetelu = Listbox(aken, font="Arial 20", fg="black", bg="#f0f0f0", selectborderwidth=3, selectbackground="#66ccff", justify=CENTER)
for i in l:
    loetelu.insert(END, i)
loetelu.pack(pady=20)
loetelu.bind("<Double-1>", valik)
aken.mainloop()


