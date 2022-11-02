#calculate your age desktop app

from tkinter import*
from tkinter import messagebox
#create the main app window
age_app = Tk()
age_app.title ("calculate the age")
#set dimenssions
age_app.geometry("400x200")

#write label
the_text=Label(age_app, text="enter your age ya suker",height=2,font=("Arial",20) )

the_text.pack() #place the text in window
#create the input for age
#age variable

age =StringVar()
#default value of age
age.set("00")

age_input=Entry(age_app,width=2,font=("arial",30),textvariable=age)
age_input.pack()
def calc():
    the_age_value=age.get()
    print(the_age_value)
    #get time unite
    months=int(the_age_value)*12
    weeks=months*4
    days=int(the_age_value)*365
    line_one=f"your age in months is:{months}"
    line_two=f"your age in weeks is:{weeks}"
    line_three=f"your age in days is:{days}"
    all_lines={line_one,line_two,line_three}
    messagebox.showinfo("your age in all time unite","\n".join(all_lines))
    print(line_one)
    print(line_two)
    print(line_three)

    
# create the calculate  button
btn=Button(age_app,text="calculate the age",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,command=calc)
btn.pack()


#run app infinitely
age_app.mainloop()