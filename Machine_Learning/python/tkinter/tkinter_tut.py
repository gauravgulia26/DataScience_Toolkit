from tkinter import *

window = Tk()
window.geometry("1000x800")
window.title("This is my first tkinter title !!")

text_var = StringVar()
text_var.set("Hello, World!")


# Create the label widget with all options
lbl = Label(
    window,
    textvariable=text_var,
    anchor=CENTER,
    bg="black",
    height=3,
    width=30,
    bd=4,
    borderwidth=10,
    font=("Arial", 20, "bold"),
    cursor="hand2",
    fg="lime",
    padx=15,
    pady=15,
    justify=CENTER,
    relief=RAISED,
    underline=10,
    wraplength=250,
)
lbl2 = Label(
    window,
    text="Hey this is my second label",
    anchor=CENTER,
    bg="black",
    height=3,
    width=30,
    bd=4,
    borderwidth=10,
    font=("Arial", 20, "bold"),
    cursor="hand2",
    fg="lime",
    padx=15,
    pady=15,
    justify=CENTER,
    relief=SUNKEN,
    underline=10,
    wraplength=250,
)
lbl.pack(pady=20)
lbl2.pack(pady=20)


"everything else goes here widgets, labels, inputs"


def button_clicked():
    print("Button clicked!")


# Creating a button with specified options
button = Button(
    window,
    text="Click Me !!",
    command=button_clicked,
    activebackground="blue",
    activeforeground="white",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12),
    height=2,
    highlightbackground="black",
    highlightcolor="green",
    highlightthickness=2,
    justify="center",
    overrelief="raised",
    padx=10,
    pady=5,
    width=15,
    wraplength=100,
)

button.pack(padx=20, pady=20)


window.mainloop()
