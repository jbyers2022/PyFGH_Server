import requests
import csv
import json

# Read the contents of the first CSV file
equil = []
with open("water-equil.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        equil.append(row)

# Read the contents of the second CSV file and add it to the data list
potential = []
with open("water-potential.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        potential.append(row)

# Convert the data list to JSON format
payload_equil = json.dumps(equil)

# Convert the data list to JSON format
payload_potential = json.dumps(potential)


# todo this api call is what will do most of the heavy lifting, and shouldn't have to deal with ensuring data is correct. That should be done client side.
# api call
api_call = requests.post('http://localhost:5000/api', json={'session_token': 'no u', 'n_list': "[11,11,11]", 'l_list': "[1.1, 1.1, 1.65]", 'd_var': '3', 'eigenvalue_method': 'False', 'set_calculation': 'Full Matrix', 'num_of_eigenvalues': '10', 'equil': payload_equil, 'potential': payload_potential})
api_call = api_call.json()
print(api_call)