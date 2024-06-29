from tkinter import *

window = Tk()

window.title("BMI Index Calculator")
window.minsize(450, 300)


def check_input():
    user_input = first_entry.get()
    user_input2 = second_entry.get()
    if user_input == "":
        label.config(text="Please Enter Weight Value")
        return False
    elif user_input2 == "":
        label.config(text="Please Enter Height Value")
        return False

    try:
        weight = int(user_input)
        height = int(user_input2)
    except ValueError:
        label.config(text="Please Enter Valid Numbers")
        return False

    return True


def bmi_calc():
    try:
        t1 = int(first_entry.get())
        t2 = int(second_entry.get())
        avg = round((t1 / ((t2 / 100) ** 2)),2)
        if avg <0:
            label.config(text="Error in calculation. Check input values.",font=('Lalezar', 15))
        elif 0 <avg < 18.5:
            label.config(text=f'Your BMI is {avg}. You are Underweight',font=('Lalezar', 15))
        elif (18.5 < avg < 24.9):
            label.config(text=f'Your BMI is {avg}. You are Normal', font=('Lalezar', 15))
        elif (25 < avg < 24.9):
            label.config(text=f'Your BMI is {avg}. You are Overweight', font=('Lalezar', 15))
        elif avg > 30:
            label.config(text=f'Your BMI is {avg}. You are Obese', font=('Lalezar', 15))
    except ValueError:
        label.config(text="Error in calculation. Check input values.")


def combined_func():
    if check_input():
        bmi_calc()


first_label = Label(text="Enter Your Weight (kg)", font=('Arial', 15, 'italic'))
first_label.config(padx=10, pady=10)
first_label.pack()

first_entry = Entry(width=20)
first_entry.pack()

second_label = Label(text="Enter Your Height (cm) ", font=('Arial', 15, 'italic'))
second_label.config(padx=10, pady=10)
second_label.pack()

second_entry = Entry(width=20)
second_entry.pack()

label = Label(text="")
label.pack(pady=8)

click_button = Button(text="Calculate", command=combined_func)
click_button.pack()

window.mainloop()
