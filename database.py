from tkinter import *
import sqlite3
# setting basic setup
window = Tk()
window.title('A form powered with SQlite')

# database connection 


# create a databse table 
# cursor.execute(''' CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#         )''')


# making the entry parts and shove them into screen.
first_name = Entry(window)
first_name.grid(row=0, column=1, columnspan=2)


last_name = Entry(window)
last_name.grid(row=1, column=1, columnspan=2)

address = Entry(window)
address.grid(row=2, column=1, columnspan=2)

city = Entry(window)
city.grid(row=3, column=1, columnspan=2)

state = Entry(window)
state.grid(row=4, column=1, columnspan=2)


zipcode = Entry(window)
zipcode.grid(row=5, column=1, columnspan=2)

# making labels for each entry 
firstnamelabel = Label(window, text="Firstname")
firstnamelabel.grid(row=0 , column=0)

lastnamelabel = Label(window, text="Lastname")
lastnamelabel.grid(row=1 , column=0)

addresslabel = Label(window, text="Address")
addresslabel.grid(row=2 , column=0)

citylabel = Label(window, text="City")
citylabel.grid(row=3 , column=0)

statelabel = Label(window, text="State")
statelabel.grid(row=4 , column=0)

zipcodelabel = Label(window, text="Zipcode")
zipcodelabel.grid(row=5 , column=0)

connection = sqlite3.connect('entryform.db')
cursor = connection.cursor()


def submit():
    data = {
            'f_name': first_name.get(),
            'l_name': last_name.get(),
            'address': address.get(),
            'state':state.get(),
            'city': city.get(),
            'zipcode': zipcode.get()
        }
    
    for v in data.values():
        if v == '' or None:
            error_label = Label(window, text="Not allowed to leave entry empty.").grid()
            return None
    else:
        cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :state,:city, :zipcode)"
                ,{
                    'f_name': first_name.get(),
                    'l_name': last_name.get(),
                    'address': address.get(),
                    'state':state.get(),
                    'city': city.get(),
                    'zipcode': zipcode.get()
                }
                )
     
    succesful_label = Label(window, text="data is saved succesfully").grid()
    
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
  



def query():
    cursor.execute("SELECT *, oid from addresses")
    records = cursor.fetchall()
    
    Toplevel = Tk()
    for element in records:
        lbl = Label(Toplevel, text=f"{element}").grid()


# buttons
button = Button(window, text="Add Record to Database", command=submit).grid(row=6, columnspan=3, column=0, ipadx=80, ipady=5)
query_btn =Button(window , text='Show Records', padx=10, pady=10, command=query ).grid(row=7, column=0, columnspan=2, ipadx= 100, ipady=15)


# commit changes into database
connection.commit()
.

# close the connection
cursor.close()
window.mainloop()
