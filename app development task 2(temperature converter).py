import tkinter as tk

def convert():
    try:
        temperature = float(entry.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            result = (temperature * 9/5) + 32
            output_label.config(text=f"Result: {result:.2f} °F")
        elif var.get() == 2:  # Fahrenheit to Celsius
            result = (temperature - 32) * 5/9
            output_label.config(text=f"Result: {result:.2f} °C")
    except ValueError:
        output_label.config(text="Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Create label and entry for input temperature
label = tk.Label(root, text="Enter Temperature:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Create radio buttons for unit selection
var = tk.IntVar(value=1)  # Default is Celsius to Fahrenheit

c_to_f_radio = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value=1)
c_to_f_radio.pack()

f_to_c_radio = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value=2)
f_to_c_radio.pack()

# Create conversion button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create label for output
output_label = tk.Label(root, text="")
output_label.pack()

# Run the application
root.mainloop()
