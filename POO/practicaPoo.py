import tkinter
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("system")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")


def button_function():
    print("Hello World!")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(
    master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
