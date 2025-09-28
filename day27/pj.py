from tkinter import *

def calculate_km():
    miles = float(input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

input = Entry(width=10)
input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=3, row=1)

equal_label = Label(text="is equal to", font=("Arial", 15))
equal_label.grid(column=1, row=2)

result_label = Label(font=("Arial", 15))
result_label.grid(column=2, row=2)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(column=3, row=2)

button = Button(text="Calculate", command=calculate_km)
button.grid(column=2, row=3)





window.mainloop()