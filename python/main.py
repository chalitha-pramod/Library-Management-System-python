from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")
root = Tk()
root.title("Library Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()
indexno = StringVar()
enddate = StringVar()
startdate = StringVar()
faculty = StringVar()
code = StringVar()


# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Library Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

#name
lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

#nid
lblAge = Label(entries_frame, text="NID", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

#indexno
lbldoj = Label(entries_frame, text="Index No", font=("Calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

#email
lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

#gender
lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

#faculty

lblFaculty = Label(entries_frame, text="Faculty", font=("Calibri", 16), bg="#535c68", fg="white")
lblFaculty.grid(row=3, column=2, padx=10, pady=10, sticky="w")
comboFaculty = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=faculty, state="readonly")
comboFaculty['values'] = ("FAS", "FE","FMC","FA","FT","FM")
comboFaculty.grid(row=3, column=3, padx=10, sticky="w")

#contact
lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblContact.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=4, column=1, padx=10, sticky="w")

#bookcode
lblCode = Label(entries_frame, text="Book Code", font=("Calibri", 16), bg="#535c68", fg="white")
lblCode.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtCode = Entry(entries_frame, textvariable=code, font=("Calibri", 16), width=30)
txtCode.grid(row=4, column=3, padx=10, sticky="w")


#address
lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=6, column=0, padx=10, pady=10, sticky="w")
txtAddress = Text(entries_frame, width=99, height=1, font=("Calibri", 16))
txtAddress.grid(row=6, column=1, columnspan=4, padx=10, sticky="w")


#startdate
lblStartDate = Label(entries_frame, text="Start Date", font=("Calibri", 16), bg="#535c68", fg="white")
lblStartDate.grid(row=5, column=0, padx=10, pady=10, sticky="w")
txtStartDate = Entry(entries_frame, textvariable=startdate, font=("Calibri", 16), width=30)
txtStartDate.grid(row=5, column=1, padx=10, sticky="w")

#enddate
lblEndDate = Label(entries_frame, text="End Date", font=("Calibri", 16), bg="#535c68", fg="white")
lblEndDate.grid(row=5, column=2, padx=10, pady=10, sticky="w")
txtEndDate = Entry(entries_frame, textvariable=enddate, font=("Calibri", 16), width=30)
txtEndDate.grid(row=5, column=3, padx=10, sticky="w")



def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    startdate.set(row[7])
    enddate.set(row[8])
    faculty.set(row[9])
    code.set(row[10])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[11])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtStartDate.get() == "" or txtEndDate.get() == "" or comboFaculty.get() == "" or txtCode.get() == "" or  txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(),txtStartDate.get(),txtEndDate.get(),comboFaculty.get(),txtCode.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtStartDate.get() == "" or txtEndDate.get() == "" or comboFaculty.get() == "" or txtCode.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),txtStartDate.get(),txtEndDate.get(),comboFaculty.get(),txtCode.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    startdate.set("")
    enddate.set("")
    faculty.set("")
    code.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=32, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=32, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=32, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=32, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=2)
tv.heading("2", text="Name")
tv.heading("3", text="NID")
tv.column("3", width=1)
tv.heading("4", text="Index")
tv.column("4", width=1)
tv.heading("5", text="Gen")
tv.column("5", width=2)
tv.heading("6", text="Faculty")
tv.column("6", width=1)
tv.heading("7", text="BookCode")
tv.column("7", width=2)
tv.heading("8", text="StartDate")
tv.column("8", width=1)
tv.heading("9", text="EndDate")
tv.column("9", width=3)
tv.heading("10", text="Email")
tv.column("10", width=1)
tv.heading("11", text="Contact")
tv.column("11", width=1)
tv.heading("12", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()