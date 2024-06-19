from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 1)
    label_3.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# Miles input object
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# Miles label
label_1 = Label(text="Miles", font=("Arial", 12, "normal"))
label_1.grid(column=2, row=0)
label_1.config(padx=5, pady=5)

# equal label
label_2 = Label(text="is equal to", font=("Arial", 12, "normal"))
label_2.grid(column=0, row=1)
label_2.config(padx=5, pady=5)

# Output label
label_3 = Label(text="0", font=("Arial", 12, "normal"))
label_3.grid(column=1, row=1)
label_3.config(padx=5, pady=5)

# Km label
label_4 = Label(text="Km", font=("Arial", 12, "normal"))
label_4.grid(column=2, row=1)
label_4.config(padx=5, pady=5)

# Calculate Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)





window.mainloop()
