import tkinter as tk
from tkinter import *
# import numpy as np 
import math 
# from matplotlib import pyplot as plt
# from PIL import ImageTk, Image

# Create a main app
root = Tk()
root.title('Design your barriers')
root.resizable(width=True,height=True)
main=Frame(root)
root.geometry("1310x700")
#################################################
# global p , w , d 
g=StringVar()
g1=StringVar()
g2=StringVar()
g3=StringVar()
def enter():
   global ncrp ,Energy , Material , angle
   ncrp=clicked.get()
 
   if ncrp=="floor":
       u=1
   elif ncrp=="ceiling":
       u=0.25
   else:
       u=0.25
   
   Energy=clicked1.get()
   Material=clicked2.get()
   
   if Energy=="6" and Material=="Concrete":
       tvl=0.35
       tve=0.35 
   elif Energy=="6" and Material=="Steel":
       tvl=0.099
       tve=0.099
   elif Energy=="6" and Material=="Leed":
       tvl=0.055
       tve=0.57
   elif Energy=="18" and Material=="Concrete":
       tvl=0.47
       tve=0.43
   elif Energy=="6" and Material=="Steel":
       tvl=0.108
       tve=0.108
   elif Energy=="6" and Material=="Leed":
       tvl=0
       tve=0
   elif Energy=="24" and Material=="Concrete":
       tvl=0.51
       tve=0.46
   elif Energy=="24"and Material=="Steel":
       tvl=0.109
       tve=0.019  
   elif  Energy=="24" and Material=="Leed":
       tvl=0
       tve=0  
  
   angle=clicked3.get()

   if angle=="10"and Energy=="6":
       a=1.04
   elif angle=="30"and Energy=="6":
       a=2.77
   elif angle=="60"and Energy=="6":
       a=8.24
   elif angle=="150"and Energy=="6":
       a=2.87  
   elif angle=="10"and Energy=="18":
       a=1.42
   elif angle=="30"and Energy=="18":
       a=2.53
   elif angle=="60"and Energy=="18":
       a=4.24
   elif angle=="150"and Energy=="18":
       a=1.20
   elif angle=="10"and Energy=="24":
       a=1.73
   elif angle=="30"and Energy=="24":
       a=2.71
   elif angle=="60"and Energy=="24":
       a=3.91
   elif angle=="150"and Energy=="24":
       a=1.14
   
   return u , tvl , tve , a


def calc():
   global p , w , d
   e=enter()
   u=float(e[0])
   tvl=float(e[1])
   tve=float(e[2])
   a=float(e[3])

   p=float(ent1.get())
   w=float(ent.get())
   d=float(ent3.get())
   x=((p)*(d)*(d))
   y=(((w)*2*270*1000)*(u)*(1))
   B=float(x)*float(y)
   x=1/(B)
   half_distance=0.5*(d)+0.61
   n=(-1*(math.log(x, 10)))
   s=(((tvl)+((n-1))*(tve))-0.14)


   dl=float(ent3.get())
   dsec=float(ent3.get())
   dsca=(float(ent3.get())-0.3)
   
   f=5
   q=((p)/((a)*(w)*1))
   e=int(dsca)*int(dsca)
   c=int(dsec)*int(dsec)
   xx=e*c
   z=400/int(f)
   Bps=q*xx*z
   m=((p)*((dl)*(dl)))
   cc=(10^-3)*int(w)*(1)
   Bl=int(m)/int(cc)
   B1=Bps+Bl
   # print(B)
   n1=(-1*math.log10(1/(B1)))
   s1=((float(tvl)+int((n1-1))*float(tve))+1)

   dw=s1-0.2
   
   global g
   g.set(s)

   global g1
   g1.set(s1)

   global g2
   g2.set(half_distance)

   global g3
   g3.set(dw)



   

   



################################################################################################    
#GiUI
wrap1 = LabelFrame(main, text="Select your parameters")
wrap1.pack(fill="both", padx=5, pady=1)

lbl1 = Label(wrap1, text="Number of patients per day", font=('Helvatical bold',10))
lbl1.grid(row=0, column=0, padx=10, pady=5)

ent=Entry(wrap1, borderwidth=5, width=15)  
ent.grid(row=0, column=1, padx=10, pady=5)

lbl5 = Label(wrap1, text="Enter the dose in mSv", font=('Helvatical bold',10))
lbl5.grid(row=0, column=2, padx=10, pady=5)

ent1=Entry(wrap1, borderwidth=5, width=15)  
ent1.grid(row=0, column=3, padx=10, pady=5)

lbl7 = Label(wrap1, text="Angle of Secondry barrier ", font=('Helvatical bold',10))
lbl7.grid(row=1, column=0, padx=10, pady=5)

clicked3= StringVar()
clicked3.set("Angle ")
drop = OptionMenu(wrap1,clicked3, "10","30","60","150")
drop.config(width=20, height=2)
drop.grid(row=1, column=1, padx=20, pady=5)

lbl9 = Label(wrap1, text="Distance between source & interest", font=('Helvatical bold',10))
lbl9.grid(row=0, column=4, padx=10, pady=5)

ent3=Entry(wrap1, borderwidth=5, width=15)  
ent3.grid(row=0, column=5, padx=10, pady=5)

lbl2 = Label(wrap1, text="Choose your use factor according to the position", font=('Helvatical bold',10))
lbl2.grid(row=1, column=2, padx=10, pady=5)

clicked= StringVar()
clicked.set("Use Factors ")
drop = OptionMenu(wrap1,clicked, "Floor","Ceiling","Walls")
drop.config(width=20, height=2)
drop.grid(row=1, column=3, padx=20, pady=5)

lbl3 = Label(wrap1, text="Choose Energy dose", font=('Helvatical bold',10))
lbl3.grid(row=2, column=0, padx=10, pady=5)

clicked1= StringVar()
clicked1.set("Energy ")
drop1 = OptionMenu(wrap1,clicked1, "6","18","24")
drop1.config(width=20, height=2)
drop1.grid(row=2, column=1, padx=10, pady=5)

lbl4 = Label(wrap1, text="Choose desired material", font=('Helvatical bold',10))
lbl4.grid(row=2, column=2, padx=10, pady=5)

clicked2= StringVar()
clicked2.set("Materials ")
drop1 = OptionMenu(wrap1,clicked2, "Concrete","Steel","Leed")
drop1.config(width=20, height=2)
drop1.grid(row=2, column=3, padx=10, pady=5)
####################################################################################################
wrap3 = LabelFrame(main)
wrap3.pack( padx=10, pady=1)

btn1=Button(wrap3, text="Enter", command=enter, width=20 , height=2, font=('Helvatical bold',12))
btn1.pack( side=LEFT ,padx=50, pady=10)
btn1=Button(wrap3, text="Calculate", command=calc, width=20 , height=2, font=('Helvatical bold',12))
btn1.pack(side=LEFT, padx=50, pady=10)
####################################################################################################
wrap2 = LabelFrame(main, text="Design Outputs")
wrap2.pack(fill="both", padx=10, pady=1)

lbl1 = Label(wrap2, text="Thickness of primary barriers", font=('Helvatical bold',12))
lbl1.grid(row=0, column=0, padx=20, pady=5)

ent2 = Entry(wrap2, textvariable= g, width=30)
ent2.grid(row=0, column=1, padx=20, pady=5)


lbl5 = Label(wrap2, text="Width of primary barriers", font=('Helvatical bold',12))
lbl5.grid(row=1, column=0, padx=20, pady=5)

ent5 = Entry(wrap2, textvariable=g2, width=30)
ent5.grid(row=1, column=1, padx=20, pady=5)

lbl3 = Label(wrap2, text="Thickness of Secondry barriers", font=('Helvatical bold',12))
lbl3.grid(row=2, column=0, padx=50, pady=5)

ent4 = Entry(wrap2, textvariable=g1, width=30)
ent4.grid(row=2, column=1, padx=50, pady=5)

lbl4 = Label(wrap2, text="Width of door", font=('Helvatical bold',12))
lbl4.grid(row=3, column=0, padx=50, pady=5)

ent4 = Entry(wrap2, textvariable=g3, width=30)
ent4.grid(row=3, column=1, padx=50, pady=5)
######################################################################################################
# img= (Image.open("E:\python\programs\image.jpeg"))
# resized_image= img.resize((400,205), Image.ANTIALIAS)
# new_image= ImageTk.PhotoImage(resized_image)
my_canvas=Canvas(root)
my_canvas.grid(row=1, column=0)
# my_canvas.create_image(0,0 , image=new_image ,anchor='nw')
######################################################################################################
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)
main.grid(row = 0, column = 0, sticky = "nesw")
#####################################################################################
root.mainloop()