import tkinter as tk
import requests
from tkinter import filedialog
import csv, json
import tkinter.messagebox

def make_api_call():
    # Read the contents of the first CSV file
    equil = []
    with open(equil_entry.get(), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            equil.append(row)

    # Read the contents of the second CSV file and add it to the data list
    potential = []
    with open(potential_entry.get(), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            potential.append(row)

    # Convert the data list to JSON format
    payload_equil = json.dumps(equil)

    # Convert the data list to JSON format
    payload_potential = json.dumps(potential)

    # get input from GUI
    data = {
        'session_token': "session_token_entry.get()",
        'n_list': n_list_entry.get(),
        'l_list': l_list_entry.get(),
        'd_var': d_var_entry.get(),
        'eigenvalue_method': eigenvalue_method_entry.get(),
        'set_calculation': set_calculation_entry.get(),
        'num_of_eigenvalues': num_of_eigenvalues_entry.get(),
        'equil': payload_equil,
        'potential': payload_potential
    }

    # make API call
    api_call = requests.post('http://localhost:5000/api', json=data)
    api_call = api_call.json()
    print(api_call)

    # display values in pop-up window
    tkinter.messagebox.showinfo("Values", "Values: " + str(api_call['data']))

    # todo display saved to file

    # todo save to file.... you know like you said you would

def select_equil_file():
    # open file dialog to select CSV file
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Equil CSV File", filetypes=[("CSV Files", "*.csv")])
    equil_entry.delete(0, tk.END) # clear current entry
    equil_entry.insert(0, file_path) # insert selected file path into entry

def select_potential_file():
    # open file dialog to select CSV file
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Potential CSV File", filetypes=[("CSV Files", "*.csv")])
    potential_entry.delete(0, tk.END) # clear current entry
    potential_entry.insert(0, file_path) # insert selected file path into entry

def open_settings():
    # code to open settings page goes here
    pass

# create GUI
root = tk.Tk()
root.title("API Call GUI")

n_list_label = tk.Label(root, text="N List:")
n_list_entry = tk.Entry(root)

l_list_label = tk.Label(root, text="L List:")
l_list_entry = tk.Entry(root)

d_var_label = tk.Label(root, text="D Var:")
d_var_entry = tk.Entry(root)

eigenvalue_method_label = tk.Label(root, text="Eigenvalue Method:")
eigenvalue_method_entry = tk.Entry(root)

set_calculation_label = tk.Label(root, text="Set Calculation:")
set_calculation_entry = tk.Entry(root)

num_of_eigenvalues_label = tk.Label(root, text="Num of Eigenvalues:")
num_of_eigenvalues_entry = tk.Entry(root)

equil_label = tk.Label(root, text="Equil:")
equil_entry = tk.Entry(root)

potential_label = tk.Label(root, text="Potential:")
potential_entry = tk.Entry(root)

# create buttons
equil_select_button = tk.Button(root, text="   Select Equil File   ", command=select_equil_file)
potential_select_button = tk.Button(root, text="Select Potential File", command=select_potential_file)
api_button = tk.Button(root, text="Make API Call", command=make_api_call)
settings_button = tk.Button(root, text="Settings", command=open_settings)

n_list_label.grid(row=1, column=0, padx=10, pady=10)
n_list_entry.grid(row=1, column=1, padx=10, pady=10)

l_list_label.grid(row=2, column=0, padx=10, pady=10)
l_list_entry.grid(row=2, column=1, padx=10, pady=10)

d_var_label.grid(row=3, column=0, padx=10, pady=10)
d_var_entry.grid(row=3, column=1, padx=10, pady=10)

eigenvalue_method_label.grid(row=4, column=0, padx=10, pady=10)
eigenvalue_method_entry.grid(row=4, column=1, padx=10, pady=10)

# place input fields and buttons in GUI
set_calculation_label.grid(row=5, column=0, padx=10, pady=10)
set_calculation_entry.grid(row=5, column=1, padx=10, pady=10)

num_of_eigenvalues_label.grid(row=6, column=0, padx=10, pady=10)
num_of_eigenvalues_entry.grid(row=6, column=1, padx=10, pady=10)

equil_label.grid(row=7, column=0, padx=10, pady=10)
equil_entry.grid(row=7, column=1, padx=10, pady=10)
equil_select_button.grid(row=7, column=2, padx=10, pady=10)

potential_label.grid(row=8, column=0, padx=10, pady=10)
potential_entry.grid(row=8, column=1, padx=10, pady=10)
potential_select_button.grid(row=8, column=2, padx=10, pady=10)

api_button.grid(row=9, column=0, columnspan=3, padx=10, pady=10)
settings_button.grid(row=9, column=2, padx=10, pady=10)

root.geometry("550x440") # increase size of window

root.mainloop()




