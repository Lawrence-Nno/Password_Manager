#!/usr/bin/python3

import tkinter
from tkinter import messagebox
import random
import pyperclip

YELLOW = "#F5F0BB"
LIGHT_GREEN = "#C3EDC0"
DARK_GREEN = "#557A46"
RED = "#8C3333"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for num in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for nam in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for nim in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_details():
    web_data = (website_entry.get()).lower()
    email_data = email_entry.get()
    pass_data = pass_entry.get()

    if web_data == "" or pass_data == "":
        messagebox.showwarning(title="Warning", message="Some fields are empty:\n"
                                                        "Please kindly fill all fields to proceed")
    else:
        confirmed = messagebox.askokcancel(title=web_data, message=f"Please check the details entered below:\n"
                                                                   f"Email:{email_data}\nPassword: {pass_data}\n"
                                                                   f"Is it ok to save?")
        if confirmed:
            with open("data.txt", mode="a") as data:
                data.write(f"Website: {web_data}\nEmail: {email_data}\nPassword: {pass_data}\n--------\n")
            website_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')
            with open("data.txt") as data:
                print(data.read())


# ---------------------------- RETRIEVE PASSWORD ------------------------------- #


def retrieve_password():
    if website_entry.get() == "":
        messagebox.showwarning(title="Warning", message="Enter the website whose password you want to retrieve.")
    with open("data.txt") as data:
        saved_data = data.readlines()
        web_name = (website_entry.get()).lower()
        for string in saved_data:
            if web_name in string:
                print((saved_data[saved_data.index(f"Website: {web_name}\n") + 2]).replace("Password: ", ""))
                password = (saved_data[saved_data.index(f"Website: {web_name}\n") + 2]).replace("Password: ", "")
                password = password.replace("\n", "")
                pass_entry.insert(0, password)
                pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="pass.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:", bg=YELLOW, fg=DARK_GREEN, font=("Courier", 12, "bold"))
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:", bg=YELLOW, fg=DARK_GREEN, font=("Courier", 12, "bold"))
email_label.grid(column=0, row=2)

pass_label = tkinter.Label(text="Password:", bg=YELLOW, fg=DARK_GREEN, font=("Courier", 12, "bold"))
pass_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=53, bg=LIGHT_GREEN)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=53, bg=LIGHT_GREEN)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, string="lawrence@gmail.com")

pass_entry = tkinter.Entry(show="*", width=34, bg=LIGHT_GREEN)
pass_entry.grid(column=1, row=3)

generate_pass_button = tkinter.Button(text="Generate Password", command=generate_pass, fg=RED)
generate_pass_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=45, command=save_details, fg=RED)
add_button.grid(column=1, row=4, columnspan=2)

retrieve_button = tkinter.Button(text="Retrieve", width=45, command=retrieve_password, fg=RED)
retrieve_button.grid(column=1, row=5, columnspan=2)


window.mainloop()
