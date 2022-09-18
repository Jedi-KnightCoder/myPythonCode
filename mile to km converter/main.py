from tkinter import *
import turtle

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))  #creates the label
# my_label.pack(side="left")
my_label["text"] = "new text"
my_label.config(text="Label")
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)



def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

#command=button_clicked
button = Button(text="Button") #creates a click button that calls the button_clicked function
button.grid(column=1, row=1)
# button = Button(text="Click Me", command=button_clicked)
# button.pack() #makes the text stay on the screen

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry..Using the Entry class
input = Entry(width=10, background="black")
input.grid(column=3, row=2)


class Car:


    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Toyota", model="Tundra")
print(my_car.model)



# tim = turtle.Turtle()
# tim.write("Some Text", font=("Times New Roman", 32, "bold"))




window.mainloop()