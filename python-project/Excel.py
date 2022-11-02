from operator import index
from tkinter import N
from turtle import clear
import pandas as pd
import re
# import numpy as np
# import openpyxl as xl
df=pd.read_csv('E:\python\programs\datta.csv')
df.columns=['data']
df.to_csv('E:\python\programs\medata.csv')
df=pd.read_csv('E:\python\programs\medata.csv')
df=df.tail(15)
df.to_csv('E:\python\programs\medata.csv')
print("newdata\n",df)
df[['scanner','tag','rssi']]=df['data'].str.split("_",expand=True)
print(df)
df.to_csv('E:\python\programs\endddataa.csv',index=False)
required_col=['scanner','tag','rssi']
required_Data=df[required_col]
required_Data.to_csv('E:\python\programs\splitdataa.csv',index=False)
x_data=pd.read_csv('E:\python\programs\splitdataa.csv')

reader= pd.read_csv('E:\python\programs\splitdataa.csv')
ind=reader.index[reader['tag'] =='V'].tolist()


R_list=[]
for i in ind:
        RSSI=reader.loc[i].at["rssi"]
        R_list.append(RSSI)



S_list=[]
for i in ind:
    SC=reader.loc[i].at["scanner"]
    S_list.append(SC)

indd=reader.index[reader['tag'] =='M'].tolist()


RR_list=[]

for i in indd:
        RSSI_1=reader.loc[i].at["rssi"]
        RR_list.append(RSSI_1)


SS_list=[]
for i in indd:
    SCC=reader.loc[i].at["scanner"]
    SS_list.append(SCC)


scannerv=S_list
rssiv=R_list
datav={"scanner":scannerv,"rssi":rssiv}
dataframe=pd.DataFrame(datav)
dataframe.to_csv('E:\python\programs\datatagv.csv',index=False)
print("tagv",dataframe)
scannerm=SS_list
rssim=RR_list
datam={"scanner":scannerm,"rssi":rssim}
dataframe=pd.DataFrame(datam)
dataframe.to_csv('E:\python\programs\datatagm.csv',index=False)
print("tagm",dataframe)

def dep_value():
    
    c=x['scanner'] 
    list_1=x.index[x["scanner"]=="A"].tolist()
    print('V_indexA=',list_1)

    z=0
    for i in range(len(c)):
        if c[i]=="A":
           z=list_1[-1]
    
           a=x.loc[z].at["rssi"]
    list_2=x.index[x["scanner"]=="B"].tolist()
    print('V_indexB=',list_2)
    f=0
   
    for i in range(len(c)):
        if c[i]=="B":
           f=list_2[-1]
    
           a2=x.loc[f].at["rssi"]
    list_3=x.index[x["scanner"]=="C"].tolist()
    print('V_indexC=',list_3)
    
    f2=0
 
    for i in range(len(c)):

        if c[i]=="C":
           f2=list_3[-1]
           a3=x.loc[f2].at["rssi"]
    list_4=x.index[x["scanner"]=="D"].tolist()
    print('V_indexD=',list_4)
    f3=0
  
    for i in range(len(c)):

       if c[i]=="D":
          f3=list_4[-1]
          a4=x.loc[f3].at["rssi"]
    list_5=x.index[x["scanner"]=="E"].tolist()
    print('V_indexE=',list_5)
    f4=0
   
    for i in range(len(c)):
        if c[i]=="E":
           f4=list_5[-1]
      
           a5=x.loc[f4].at["rssi"]
    sort_index=z,f,f2,f3,f4
    print("sorted list",sort_index)
    fsrssi=sorted(sort_index)
    print(fsrssi)
    for i in fsrssi:
        if i==0:
           fsrssi.remove(i)
    listt2=fsrssi
    for i in fsrssi:
        if i==0:
           fsrssi.remove(i)
           print(fsrssi)

    print(listt2)

    list_scanner=[]
    
    global scanner1
    global rssi1
    list_rssi=[]

    for i in listt2:
        v=x.loc[i].at["scanner"]
        list_scanner.append(v)
        print("scanner",list_scanner)
    for i in listt2:
        g=x.loc[i].at["rssi"]
        list_rssi.append(g)
        rssi1=list_rssi
        print("rssi",list_rssi)
        scanner1=list_scanner
x=pd.read_csv('E:\python\programs\datatagv.csv')
job1=dep_value()
dataa={"scanner":scanner1,"rssi":rssi1}
dataaframefinal=pd.DataFrame(dataa)
dataaframefinal.to_csv('E:\python\programs\Finaltagv.csv',index=False)
print("VVVVVVVVVVV\n",dataaframefinal)
print("#######done#############")
df=pd.read_csv('E:\python\programs\Finaltagv.csv')
measured_rssi=-59
rssi_now1=df['rssi']
w1=(10)*(2.486)

for i in rssi_now1:
    global y
    y=(-59-(rssi_now1))
    d=(y/w1)
    dis1=10**(d)
print("dis of tag v\n",dis1)
first={"scanner":scanner1,"distance":dis1}
distance=pd.DataFrame(first)
distance.to_csv('E:\python\programs\distance_v.csv',index=False)
print(distance)
x=pd.read_csv('E:\python\programs\datatagm.csv')
job2=dep_value()   
print("scanner1",scanner1) 
dataa={"scanner":scanner1,"rssi":rssi1}
dataaframefinal=pd.DataFrame(dataa)
dataaframefinal.to_csv('E:\python\programs\Finaltagm.csv',index=False)

print("#########done#############")
df=pd.read_csv('E:\python\programs\Finaltagm.csv')
measured_rssi=-59
rssi_now2=df['rssi']
w2=(10)*(2.486)
for i in rssi_now2:
    global f
    f=(-59-(rssi_now2))
    dd=(f/w2)
    dis2=10**(dd)
print("dis of tag M\n",dis2)
second={"scanner":scanner1,"distance":dis2}
distance=pd.DataFrame(second)
distance.to_csv('E:\python\programs\distance_m.csv',index=False)

