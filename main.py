from tkinter import *
window = Tk()
window.title("Mile to KM Converter")
window.config(padx=25,pady=25)
#window.minsize(width=300, height=200)
#Text box for miles
miles = Entry(width=5)
miles.insert(END,string="0")
miles.grid(column=0,row=0)
#Conversion Label
def calculate():
  km = int(miles.get()) * 1.609
  km_label.config(text=f"{round(km)} Km")
conv_label = Label(text="Miles is equal to")
conv_label.grid(column=1,row=0)
km_label = Label(text="0 Km")
km_label.grid(column=1,row=1)
#Button to calculate km
calc = Button(text="Calculate",command=calculate)
calc.grid(column=1,row=2)

window.mainloop()