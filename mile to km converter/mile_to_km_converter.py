from tkinter import *
import turtle

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


entry = Entry(width=20, font=("Arial", 14, "bold"))  #box that takes the number of miles you want to convert
#Gets text in entry
entry.grid(column=1, row=0)



miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 14, "bold"))
is_equal_to.grid(column=0, row=1)

def conversion():
    get_text = entry.get()
    miles_to_km_conversion = round(float(get_text) * 1.60934)
    km_number.config(text=miles_to_km_conversion)


km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

km_number = Label(text="0", font=("Arial", 14, "bold"))
km_number.grid(column=1, row=1)
km_number.config(pady=10, padx=10)

calculate_button = Button(text="Calculate", command=conversion) #creates a click button that calls the button_clicked function
calculate_button.config(width=20)
# button.grid(column=1, row=1)
calculate_button.grid(column=1, row=2)




window.mainloop()