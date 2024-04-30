import tkinter

# Create a tkinter window 
tk_inter = tkinter.Tk("Tkinter")
tk_inter.title("Miles to Kilometer Converter")

# Padding
tk_inter.config(padx=250, pady=250)
# Window Size
tk_inter.minsize(500, 500)



def button_clicked():
    data = int(take_input.get())
    data *= 1.6
    data = round(data)
    kilo.config(text=f"{data}")



# button2 = tkinter.Button(text="click me",command=button_clicked)
# button2.grid(column=2, row=0)


# Take inputs by creating Entry object
# It's better to use grid to specify the object's placement in the window
take_input = tkinter.Entry(width=20)
take_input.grid(column=10, row=10)

label = tkinter.Label(text="Miles")
label.grid(column=11, row=10)

kilo = tkinter.Label(text="0")
kilo.grid(column=10, row=13)

label2 = tkinter.Label(text="Km")
label2.grid(column=11, row=13)

button = tkinter.Button(text="Convert",command=button_clicked)
button.grid(column=10, row=15)

# To keep the screen still
tk_inter.mainloop()