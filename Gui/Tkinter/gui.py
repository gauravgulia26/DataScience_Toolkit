from tkinter import *
from tkinter import font

window = Tk()
window.geometry("1000x500")
window.configure(bg="#f6b71c")
window.title("Registration Form")

custom_font = font.Font(family="Arial", size=80, weight="bold")


vl = []


def submit():
    try:
        op = int(mobile.get())
    except Exception as e:
        print(e)
    else:
        if len(str(op)) == 10:
            vl.append(u_name.get())
            vl.append(mobile.get())
            vl.append(zipcode.get())
            vl.append(city.get())
            if var.get() == 1:
                vl.append("Male")
            else:
                vl.append("Female")
            u_name.config(state=DISABLED)
            mobile.config(state=DISABLED)
            zipcode.config(state=DISABLED)
            city.config(state=DISABLED)
            male.config(state=DISABLED)
            fmale.config(state=DISABLED)
            print(" ".join(vl))
        else:
            raise Exception("Mobile Number should be of 10 digit only !!!")


lbl = Label(
    text="Welcome to the Registration Window !!",
    bg="#876d2b",
    bd=1.5,
    relief=RAISED,
    font=custom_font,
    width=100,
    padx=5,
    pady=5,
    fg="white",
)
lbl_name = Label(
    text="Name",
    bg="#876d2b",
    bd=1,
    relief=RAISED,
    font=custom_font,
    padx=2.8,
    pady=2.8,
    fg="white",
    width=20,
)
mbl_nmbr = Label(
    text="Mobile Number",
    bg="#876d2b",
    bd=1,
    relief=RAISED,
    font=custom_font,
    padx=2.8,
    pady=2.8,
    fg="white",
    width=20,
)
city_label = Label(
    text="City",
    bg="#876d2b",
    bd=1,
    relief=RAISED,
    font=custom_font,
    padx=2.8,
    pady=2.8,
    fg="white",
    width=20,
)
Zipcode_label = Label(
    text="ZipCode",
    bg="#876d2b",
    bd=1,
    relief=RAISED,
    font=custom_font,
    padx=2.8,
    pady=2.8,
    fg="white",
    width=20,
)
m_label = Label(
    text="Male",
    bg="#876d2b",
    bd=1,
    relief=RAISED,
    font=custom_font,
    padx=2.8,
    pady=2.8,
    fg="white",
    width=20,
)
f_label = Label(
    text="Female",
    bg="#876d2b",
    bd=1,
    relief=RAISED,
    font=custom_font,
    padx=2.8,
    pady=2.8,
    fg="white",
    width=20,
)


u_name = Entry(
    window, width=30, font=custom_font, bg="#876d2b", fg="white", bd=1, relief=SUNKEN
)
mobile = Entry(
    window, width=30, font=custom_font, bg="#876d2b", fg="white", bd=1, relief=SUNKEN
)
city = Entry(
    window, width=30, font=custom_font, bg="#876d2b", fg="white", bd=1, relief=SUNKEN
)
zipcode = Entry(
    window, width=30, font=custom_font, bg="#876d2b", fg="white", bd=1, relief=SUNKEN
)

var = IntVar()
male = Radiobutton(window, bg="#f6b71c", variable=var, value=1)
fmale = Radiobutton(window, bg="#f6b71c", variable=var, value=2)


btn = Button(
    window,
    text="Submit",
    bg="lime",
    fg="black",
    padx=4,
    pady=4,
    width=60,
    font=custom_font,
    activebackground="#2db109",
    activeforeground="black",
    bd=5,
    relief=RAISED,
    command=submit,
)

lbl.grid(row=0, column=2, padx=20, pady=20)
lbl_name.grid(row=1, column=0, padx=4, pady=8)

u_name.grid(row=1, column=1, padx=4, pady=8)
mbl_nmbr.grid(row=2, column=0, padx=4, pady=8)

mobile.grid(row=2, column=1, padx=4, pady=8)
city_label.grid(row=3, column=0, padx=4, pady=8)

city.grid(row=3, column=1, padx=4, pady=8)
Zipcode_label.grid(row=4, column=0, padx=4, pady=8)

zipcode.grid(row=4, column=1, padx=4, pady=8)
m_label.grid(row=5, column=0, padx=4, pady=8)

f_label.grid(row=5, column=1, padx=4, pady=8)
male.grid(row=6, column=0)

fmale.grid(row=6, column=1)
btn.grid(row=8, column=2, padx=10, pady=10)

window.mainloop()