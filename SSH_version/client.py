import paramiko

# Set up the SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server using the private key
private_key_path = '/home/pixlflip/.ssh/id_rsa'

# get the RSA key from the private key file
# todo still having issues with this and can't move on till I fix it
key = paramiko.RSAKey.from_private_key_file(private_key_path)
client.connect(hostname="acm.missouriwestern.edu", username="jbyers", password="ilikelinux", pkey=key)

# create an arg dict with JSON formatting for easy porting to other stuff
# todo create a try catch for if the csv file values have been added to this JSON
args = { 'n_list': "[11,11,11]",
 'l_list': "[1.1, 1.1, 1.65]",
 'd_var': '3',
 'eigenvalue_method': 'False',
 'set_calculation': 'Full Matrix',
 'num_of_eigenvalues': '10'
 }

# Define the variables
file1 = "equil.csv"
file2 = "potential.csv"

# Use scp to transfer the files to the server
scp = client.open_sftp()
scp.put(file1, "equil.csv")
scp.put(file2, "potential.csv")
scp.close()

# Run the script with the variables and file paths as arguments
#command = f"python3 hello.py"
command = f"python3 pyfgh_script.py {args['n_list']} {args['l_list']} {args['d_var']} {args['eigenvalue_method']} {args['set_calculation']} {args['num_of_eigenvalues']} potential.csv equil.csv"
stdin, stdout, stderr = client.exec_command(command)

# Print the output
print(stdout.read().decode())

# Close the connection
client.close()
