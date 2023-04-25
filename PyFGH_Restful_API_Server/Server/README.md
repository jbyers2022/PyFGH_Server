# PyFGH RESTful API Server

This is a Python script for a RESTful API server that runs a Python script called
PyFGH using Flask and Flask-RESTful libraries. The API server is used to upload data
to PyFGH and receive the results.

## Prerequisites
- Python 3
- Flask
- Flask-RESTful
- Docker (optional)

## Installation
1. Clone the repository
2. Install dependencies using pip install -r requirements.txt

## Usage

1. Run the server by executing python __main__.py
2. Send a POST request to the server's /api endpoint with the following JSON data:
```json
{
    "session_token": "YOUR_SESSION_TOKEN",
    "n_list": "YOUR_N_LIST",
    "l_list": "YOUR_L_LIST",
    "d_var": "YOUR_D_NUMBER",
    "eigenvalue_method": "True or False",
    "set_calculation": "YOUR_CALCULATION",
    "num_of_eigenvalues": "YOUR_NUMBER_OF_EIGENVALUES",
    "equil": "YOUR_JSON_FORMATTED_CSV_OF_EQUIL",
    "potential": "YOUR_JSON_FORMATTED_CSV_OF_POTENTIAL"
} 
```
3. You can now send HTTP requests to http://localhost:5000/api to use the PyFGH RESTful API server.
The server will run the PyFGH script with the given data and return the results
in a JSON object with an ID, status, and data field.

## Docker
This project comes ready to work with Docker.

1. Build the Docker image using the following command:
```commandline
docker build -t pyfgh-api .
```
2. Run the Docker container using the following command:
```commandline
docker run -p 5000:5000 pyfgh-api
```
This will start the server and map port 5000 on your local machine to port 5000 inside the container.

3. You can now send HTTP requests to http://localhost:5000/api to use the PyFGH RESTful API server.


## Configuration
The API server can be configured using a config.json file in the root directory. 
The following options are available:

- use_openpbs: Set to true if OpenPBS is being used to run the PyFGH script.

## Contributing
If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
GPL v3.0