# make a scripting app in python using tkinter that has all these fitures


# scripting app where you can make a script of actions to be done in a certain order and then run it
# the script is saved in a text file and can be loaded later
# you can also record a script by clicking the record button and then doing the actions you want to be recorded
# you can select the date and time you want the script to be run
# you can also set the script to run every day or every week or every month or every year
# you can also set the script to run multiple times in a row
# you can also set the script to run multiple times in a row with a delay between each run
# you can set the script to run in a loop until you stop it
# you can also set the script to run in a loop until you stop it with a delay between each run
# you can also set a delay between each action in the script
# you can also make a script by writing the order of actions and the delay between them in the script text box

import tkinter as tk

# create main window
window = tk.Tk()
window.title("Scripting App")

# add widgets and layout
script_text = tk.Text(window, width=50, height=20)
script_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

run_button = tk.Button(window, text="Run Script")
run_button.grid(row=1, column=0, padx=10, pady=10)

record_button = tk.Button(window, text="Record Script")
record_button.grid(row=2, column=0, padx=10, pady=10)

save_button = tk.Button(window, text="Save Script")
save_button.grid(row=3, column=0, padx=10, pady=10)

load_button = tk.Button(window, text="Load Script")
load_button.grid(row=4, column=0, padx=10, pady=10)

schedule_label = tk.Label(window, text="Schedule:")
schedule_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

date_label = tk.Label(window, text="Date:")
date_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")

date_entry = tk.Entry(window)
date_entry.grid(row=1, column=2, padx=5, pady=5, sticky="w")

time_label = tk.Label(window, text="Time:")
time_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

time_entry = tk.Entry(window)
time_entry.grid(row=2, column=2, padx=5, pady=5, sticky="w")

repeat_label = tk.Label(window, text="Repeat:")
repeat_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

repeat_var = tk.StringVar(window)
repeat_choices = ["None", "Every day", "Every week", "Every month", "Every year"]
repeat_dropdown = tk.OptionMenu(window, repeat_var, *repeat_choices)
repeat_dropdown.grid(row=3, column=2, padx=5, pady=5, sticky="w")

times_label = tk.Label(window, text="Times:")
times_label.grid(row=4, column=1, padx=10, pady=5, sticky="e")

times_entry = tk.Entry(window)
times_entry.grid(row=4, column=2, padx=5, pady=5, sticky="w")

delay_label = tk.Label(window, text="Delay:")
delay_label.grid(row=5, column=1, padx=10, pady=5, sticky="e")

delay_entry = tk.Entry(window)
delay_entry.grid(row=5, column=2, padx=5, pady=5, sticky="w")

loop_var = tk.BooleanVar(window)
loop_checkbox = tk.Checkbutton(window, text="Loop", variable=loop_var)
loop_checkbox.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# start the GUI event loop
window.mainloop()
