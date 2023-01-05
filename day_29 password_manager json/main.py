from tkinter import*
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    #MY CODE --One Example of how to create Password List
    # password_list += [random.choice(letters) for letter in range(nr_letters)]
    # password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    # password_list += [random.choice(numbers) for number in range(nr_numbers)]
    # print(password_list)

    #ALTERNATIVE WAY TO CREATE PASSWORD LIST
    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    # ADDS ALL LISTS, LISTED ABOVE INTO ONE LIST LISTED BELOW
    password_list = password_letters + password_numbers + password_symbols
    print(password_list)
    random.shuffle(password_list)
    password = "".join(password_list) #THE Join Method Joins all the strings in the list as one string
                                      # "" represents an empty string so there's no space in between
                                      #characters

    print(f"Your password is: {password}")
    password_entry.insert(0, string=password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info(*args):
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }
    print(type(website))
    print(len(website))
    print(len(password))
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="No Empty Fields", message="Please don't leave any fields empty")


    # elif web_text and password:
    else:
        # is_ok = messagebox.askokcancel(title=website_entry, message=f"These are the details you entered: "
        #                                                             f"\n {web_text}\n {email_text}\n {password}\n"
        #                                                             f" Is it ok to Save?")
        # if is_ok:
        try: #tries to execute the code listed below
            # when you use the "r" for write you use json.load()
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                #reading old data
                data = json.load(data_file)
                #Updating old data with new data to the new_data dictionary

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            #when you use the "w" for write you use json.dump()
            with open("data.json", "w") as data_file:
                #saving the updated data
                json.dump(data, data_file, indent=4)


        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # with open("data.json", "w") as data_file:
            #     #data.update(new_data)
            #     json.dump(new_data, data_file, indent=4)

            # with open("data.json", "r") as data_file:
            #     #data.update(new_data)
            #     data = json.load(data_file)
            #     data.update(new_data)


            # with open("data.json", "w") as data_file:
            #     data = json.load(data_file)
            #     # Updating old data with new data to the new_data dictionary
            #     data.update(new_data)


            #CREATES A TEXT FILE --> with open("new_file.txt", mode="a") as new_file:
            # print(web_text)
            # new_file.write(f"{website} | {email} | {password} \n")

#------------------------------SEARCH FUNCTION--------------####
def find_password():
    website = website_entry.get()
    email = email_username_entry.get()
    # password = password_entry.get()

    with open("data.json", "r") as data_file:
        # json.dump(new_data, data_file, indent=4)
        # reading old data
        data = json.load(data_file)
    if website in data or email in data:
        messagebox.showwarning(title=f"{website}",
                               message=f"Email:{data['Facebook']['email']}\nPassword:{data['Facebook']['password']}")
        print("data is present")
        print(data["Facebook"]["password"])
    else:
        print("do another search")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="black")
#window.minsize(width=500, height=500)


#image picture
canvas = Canvas(width=200, height=200, bg="white")
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

#Website Label
website_label = Label(text="Website")
website_label.grid(column=0, row=1)



#Email Label
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

#Password Label
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

#____________________________________________
#the sticky function/command tells the edge where to stick.
# "E" stands for East which is Right
# "W" stands for left which is "Left
# "EW stretches the button or entry to both ends

#website Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="W")
website_entry.focus()

# website_entry.place(x=90, y=200)

#email/username entry
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_entry.insert(0, "gaylon@yahoo.com")
# email_ = email_username_entry.grid(column=1, row=2)


#password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="W")



#generate password button
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

#search button searces the json file
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

add_button = Button(text="Add", width=36, command=add_info)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")



# messagebox.showinfo(title="Title", message="Your data has been Entered")
    # messagebox.showwarning(title="Response", message="try again Since You're so Smart!")
    # messagebox.askokcancel(title=web_text, message=f"These are the details you entered:\n"
    #                                                f"Email: {email_text} \nPassword: {password_data}\n"
    #                                                f"Is it ok to save?")
    #
    # with open("new_file.txt", mode="a") as new_file:
    #     print(web_text)
    #     new_file.write(f"{web_text} | {email_text} | {password_data} \n")
    #
    #     website_entry.delete(0, END)
    #     website_entry.insert(0, "")
    #     password_entry.delete(0, END)
    #     password_entry.insert(0, "")

window.mainloop()