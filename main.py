from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def search():
    web = web_entry.get()
    if len(web) == 0:
        messagebox.showinfo(title='Empty Search', message='What are you looking for?')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title='ERROR', message='No Data File Found')
        else:
            if web in data:
                email = data[web]['email']
                password = data[web]['password']
                messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title='ERROR', message=f'No Data found for {web}')


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web:{
            "email": email,
            "password": password
        }
    }

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Empty Fields', message='Populate All Fields')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            print('FIle NOt Found')
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        web_entry.delete(0, END)
        pass_entry.delete(0, END)


window = Tk()
window.title('Password Generator')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg='white')
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0, columnspan=2)

#LABELS
web_label = Label(text='Website')
web_label.grid(column=0, row=1)
email_label = Label(text='Email')
email_label.grid(column=0, row=2)
pass_label = Label(text='Password')
pass_label.grid(column=0, row=3)

#ENTRIES
web_entry = Entry(width=32)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,'example@gmail.com')
pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)

#BUTTONS
search_btn = Button(text='Search', width=15, command=search)
search_btn.grid(column=2, row=1)
gen_btn = Button(text='Generate Password', width=15, command=generate)
gen_btn.grid(column=2, row=3)
add_btn = Button(text='Add', width=44, command=save)
add_btn.grid(column=1, row=4, columnspan=2)




window.mainloop()