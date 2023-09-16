import tkinter as tk

def convert():
    try:
        input_value = float(entry.get())
        unit = unit_var.get()

        if unit == "Inches to Centimeters":
            result = input_value * 2.54
        elif unit == "Centimeters to Inches":
            result = input_value / 2.54
        elif unit == "Miles to Kilometers":
            result = input_value * 1.60934
        elif unit == "Kilometers to Miles":
            result = input_value / 1.60934
        elif unit == "Liters to Gallons":
            result = input_value * 0.264172
        elif unit == "Gallons to Liters":
            result = input_value / 0.264172
        else:
            result = "Invalid Conversion"

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Unit Conversion")

# Create an entry field for user input
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a variable to store the selected conversion unit
unit_var = tk.StringVar(root)
unit_var.set("Inches to Centimeters")

# Create a dropdown menu for selecting the conversion unit
unit_menu = tk.OptionMenu(root, unit_var, "Inches to Centimeters", "Centimeters to Inches",
                          "Miles to Kilometers", "Kilometers to Miles",
                          "Liters to Gallons", "Gallons to Liters")
unit_menu.pack(pady=10)

# Create a button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
