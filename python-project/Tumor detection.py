
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import os
from skimage.util import random_noise



img = ""

def browseimg():
    global img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Browse Image File", filetypes=(("JPG Image","*.jpg"), ("PNG Image","*.png"), ("All Files","*.*")))
    t1.set(filename)
    img=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    m.set(img.shape[0])
    n.set(img.shape[1])
    
def display():
    cv2.imshow("Original Image",img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
  
def noise():
    N = random_noise(img, mode= 'gaussian', seed= None, clip= True)
    cv2.imshow("Noisy Image",N)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def gauss():
    G_blur = cv2.GaussianBlur(img,(3,3),5)
    cv2.imshow("Gaussian filter",G_blur)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def median():
    median = cv2.medianBlur(img,9)
    cv2.imshow("Median filter",median)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def average():
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    cv2.imshow("Average filter",dst)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def blur():
    blur = cv2.blur(img,(9,9))
    cv2.imshow("Blurring filter",blur)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def hist():
    img_enhanced = cv2.medianBlur(img,9)
    h = plt.hist(img_enhanced.ravel(),256,[0,256])
    plt.show()
    
def equalized():
    img_enhanced = cv2.medianBlur(img,9)
    eq = cv2.equalizeHist(img_enhanced)
    cv2.imshow("Equalized Image",eq)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def eqhist():
    img_enhanced = cv2.medianBlur(img,9)
    eq = cv2.equalizeHist(img_enhanced)
    hh = plt.hist(eq.ravel(),256,[0,256])
    plt.show()

def zoomin():
    img_enhanced = cv2.medianBlur(img,9)
    scaleX = 0.6
    scaleY = 0.6
    scaleUp = cv2.resize(img_enhanced, None, fx= scaleX*3, fy= scaleY*3, interpolation= cv2.INTER_LINEAR)
    cv2.imshow("Zoomed In Image", scaleUp)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def zoomout():
    img_enhanced = cv2.medianBlur(img,9)
    scaleX = 0.6
    scaleY = 0.6
    scaleDown = cv2.resize(img_enhanced, None, fx= scaleX, fy= scaleY, interpolation= cv2.INTER_LINEAR)
    cv2.imshow("Zoomed out Image", scaleDown)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def rotate90():
    img_enhanced = cv2.medianBlur(img,9)
    rotated90 = cv2.rotate(img_enhanced, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Rotated by 90 Degrees", rotated90)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def rotate180():
    img_enhanced = cv2.medianBlur(img,9)
    rotated180 = cv2.rotate(img_enhanced, cv2.ROTATE_180)
    cv2.imshow("Rotated by 180 Degrees", rotated180)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def rotate270():
    img_enhanced = cv2.medianBlur(img,9)
    rotated270 = cv2.rotate(img_enhanced, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Rotated by 270 Degrees", rotated270)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

root = Tk()


t1 = StringVar()
m = StringVar()
n = StringVar()

wrapper = LabelFrame(root, text="Source File")
wrapper.pack(fill="both", padx=10, pady=10)

lbl1 = Label(wrapper, text="Source File")    
lbl1.pack(side=tk.LEFT, padx=50, pady=50)

ent= Entry(wrapper, textvariable=t1)
ent.pack(side=tk.LEFT)


btn = Button(wrapper, text="Browse image", command=browseimg)
btn.pack(side=tk.LEFT, padx=40, pady=40)

btn2 = Button(wrapper, text="Display image", command=display)
btn2.pack(side=tk.LEFT, padx=40, pady=40)

wrapper2 = LabelFrame(root, text="Image Details")
wrapper2.pack(fill="both", padx=10, pady=10)

lbl2 = Label(wrapper2, text="Dimension")
lbl2.pack(side=tk.LEFT, padx=50, pady=50)

ent2= Entry(wrapper2, textvariable=m)
ent2.pack(side=tk.LEFT, padx=40, pady=40)

lbl3 = Label(wrapper2, text="X")
lbl3.pack(side=tk.LEFT, padx=50, pady=50)

ent2= Entry(wrapper2, textvariable=n)
ent2.pack(side=tk.LEFT, padx=40, pady=40)
###############################################################################

wrapper3 = LabelFrame(root, text="Smoothing Filters")
wrapper3.pack(fill="both", padx=10, pady=10)

btn3 = Button(wrapper3, text="Add Noise", command=noise)
btn3.pack(side=tk.LEFT, padx=60, pady=60)

btn4 = Button(wrapper3, text="Gaussian Filter", command=gauss)
btn4.pack(side=tk.LEFT, padx=60, pady=60)

btn5 = Button(wrapper3, text="Median Filter", command=median)
btn5.pack(side=tk.LEFT, padx=40, pady=40)

btn6 = Button(wrapper3, text="Average Filter", command=average)
btn6.pack(side=tk.LEFT, padx=40, pady=40)

btn7 = Button(wrapper3, text="Blurring Filter", command=blur)
btn7.pack(side=tk.LEFT, padx=40, pady=40)

###############################################################################

wrapper4 = LabelFrame(root, text="Histogram")
wrapper4.pack(fill="both", expand="yes", padx=10, pady=10)

btn8 = Button(wrapper4, text="Histogram", command=hist)
btn8.pack(side=tk.LEFT, padx=40, pady=40)

btn9 = Button(wrapper4, text="Equalized Image", command=equalized)
btn9.pack(side=tk.LEFT, padx=40, pady=40)

btn10 = Button(wrapper4, text="Equalized Histogram", command=eqhist)
btn10.pack(side=tk.LEFT, padx=40, pady=40)

wrapper5 = LabelFrame(root, text="Zooming and Rotate")
wrapper5.pack(fill="both", expand="yes", padx=10, pady=10)

btn11 = Button(wrapper5, text="Zoom In", command=zoomin)
btn11.pack(side=tk.LEFT, padx=40, pady=40)

btn12 = Button(wrapper5, text="Zoom Out", command=zoomout)
btn12.pack(side=tk.LEFT, padx=40, pady=40)

btn13 = Button(wrapper5, text="Angle 90", command=rotate90)
btn13.pack(side=tk.LEFT, padx=40, pady=40)

btn14 = Button(wrapper5, text="Angle 180", command=rotate180)
btn14.pack(side=tk.LEFT, padx=40, pady=40)

btn15 = Button(wrapper5, text="Angle 270", command=rotate270)
btn15.pack(side=tk.LEFT, padx=40, pady=40)


wrapper6 = LabelFrame(root, text="Object Detection")
wrapper6.pack(fill="both", expand="yes", padx=10, pady=10)






root.title("Image Processing Project")

root.geometry("900x800")

root.mainloop()



