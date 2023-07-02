from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

def login():
    username = username_entry.get()
    password = password_entry.get()

#sifre fln burdan degisiliyo

    if username == "arda" and password == "3131":
        login_screen.destroy()
        main_screen()
    else:
        error_label.config(text="Geçersiz kullanıcı adı veya şifre!")

def main_screen():
    main_screen = Tk()
    main_screen.title("Ana Ekran")
    main_screen.geometry("300x150")
    main_screen.config(bg="lightgray")

    welcome_label = Label(main_screen, text="Hoş geldiniz!", font=("Arial", 16), bg="lightgray", fg="black")
    welcome_label.pack(pady=10)

    global time_label
    time_label = Label(main_screen, text="", font=("Arial", 28, "bold"), bg="lightgray", fg="black")
    time_label.pack(pady=20)
    update_time()

    main_screen.mainloop()

def handle_enter(event):
    login()

login_screen = Tk()
login_screen.title("Giriş Ekranı")
login_screen.geometry("300x200")
login_screen.config(bg="lightgray")

username_label = Label(login_screen, text="Kullanıcı Adı:", font=("Arial", 12), bg="lightgray", fg="black")
username_label.pack(pady=10)
username_entry = Entry(login_screen, font=("Arial", 12))
username_entry.pack()
username_entry.focus()

password_label = Label(login_screen, text="Şifre:", font=("Arial", 12), bg="lightgray", fg="black")
password_label.pack(pady=10)
password_entry = Entry(login_screen, show="*", font=("Arial", 12))
password_entry.pack()

password_entry.bind('<Return>', handle_enter)

login_button = Button(login_screen, text="Giriş", command=login, font=("Arial", 12), bg="lightblue", fg="black")
login_button.pack(pady=10)

error_label = Label(login_screen, text="", font=("Arial", 12), bg="lightgray", fg="red")
error_label.pack()

login_screen.mainloop()
