from tkinter import *

# GUI -> Graphical User Interface

window = Tk()
window.geometry("1000x720")
window.title("Tkinter Window")


# * Label

# Create the label widget with all options
lbl = Label(
    window,
    text='Hello my label',
    anchor=CENTER,
    bg="black",
    height=3,
    width=30,
    bd=4,
    borderwidth=10,
    font=("Arial", 20, "bold"),
    cursor="hand2",
    fg="lime",
    padx=1,
    pady=1,
    justify=CENTER,
    relief=SUNKEN,
    underline=10,
    wraplength=250,
)
lbl.pack(pady=10)

lbl2 = Label(
    window,
    text='Label 2',
    anchor=CENTER,
    bg="black",
    height=3,
    width=30,
    bd=4,
    borderwidth=10,
    font=("Arial", 20, "bold"),
    cursor="hand2",
    fg="lime",
    padx=1,
    pady=1,
    justify=CENTER,
    relief=RAISED,
    underline=10,
    wraplength=250,
)
lbl2.pack(padx=10, pady=10)

"""
everything else go here
"""

button = Button(
    window,
    text="Click Me",
    command=window.destroy,
    activebackground="black",
    activeforeground="lime",
    anchor="center",
    bd=3,
    bg="lightgray",
    cursor="hand2",
    disabledforeground="gray",
    fg="black",
    font=("Arial", 12,'bold'),
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
# creating a simple canvas
c = Canvas(window, bg="black", height="800", width='1000')

arc = c.create_arc((100, 200, 300, 400), start=0, extent=270, fill="purple")
arc = c.create_arc((50, 100, 150, 200), start=0, extent=270, fill="purple")
arc = c.create_arc((25, 50, 100, 150), start=0, extent=270, fill="purple")



c.pack()

window.mainloop()
