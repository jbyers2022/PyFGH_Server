# PyFGH: Quantum Calculation API and SSH Client

This project consists of three main components: a server-side script, a client-side GUI, and an SSH client script. The server-side script uses the Flask framework to create an API that processes quantum calculation requests. The client-side GUI allows users to input parameters and upload CSV files containing the necessary data. The SSH client script connects to a remote server, transfers the required CSV files, and executes a Python script on the remote server.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Server](#server)
   - [Client](#client)
   - [SSH Client](#ssh-client)
3. [Dependencies](#dependencies)
4. [Support](#support)
5. [Contributing](#contributing)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/jwoodford/whateveryounameit.git
```

Navigate to the project directory:

```bash
cd PyFGH-Final
```

## Usage

### Server

To start the server, run the following command:

```bash
python server.py
```

The server will be accessible at http://localhost:5000.

### Client

To launch the client-side GUI, run the following command:

```bash
python client.py
```

The client-side GUI allows you to input various parameters, select CSV files for the Equil and Potential data, and send the request to the server. Once the server processes the request, the results will be displayed in a pop-up window.

### SSH Client

Before running the SSH client script, ensure that you have the correct private key file and remote server credentials. Update the `private_key_path`, `hostname`, `username`, and `password` variables in the `ssh_client.py` script as needed.

To run the SSH client script, execute the following command:

```bash
python ssh_client.py
```

The SSH client script will connect to the remote server, transfer the required CSV files, and execute the specified Python script on the remote server. The output will be displayed in the console.

## Dependencies

- Python 3.x
- Flask
- Paramiko
- Tkinter

Install the required Python packages using the following command:

```bash
pip install Flask Paramiko
```

For Tkinter, use the package manager for your system to install the required packages. For example, on Ubuntu:

```bash
sudo apt-get install python3-tk
```

## Support

For support or questions, please contact the author at [jwoodford@missouriwestern.edu](mailto:jwoodford@missouriwestern.edu).

## Contributing

This project is not currently accepting contributions. However, if you have suggestions for improvements or bug fixes, feel free to open an issue or submit a pull request.

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.