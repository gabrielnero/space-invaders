import tkinter
from tkinter import messagebox

def login():

        user = username_entry.get()
        email = email_entry.get()

        if len(user) == 0 or len(email) == 0:
            messagebox.showerror(title="Opa!", message="Tá faltando informação ae!")
        else:
            is_ok = messagebox.askokcancel(title=user, message=f"Nome: {user}"
                                                                  f"\nEmail: {email}\nSalvar?")
            if is_ok:
                with open("login.txt", "a") as data_file:
                    data_file.write(f"{user} | {email}\n")
                    window.destroy()
window = tkinter.Tk()
window.title("Login Space Invaders")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
email_label = tkinter.Label(
    frame, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
email_entry = tkinter.Entry(frame, font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()