#Table of Contents
Introduction
Features
Installation
Usage
API Endpoints
Testing
Dynamic Parameter Handling
Deployment
umldiagram
Documentation

#Introduction
This is a simple REST API built using FastAPI that allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource. The API is designed to dynamically handle parameters and can perform operations like adding or retrieving a person by name

#Features
Create: Add a new person to the database.
Read: Retrieve person details by their unique user_id.
Update: Modify the details of an existing person using their user_id.
Delete: Remove a person from the database based on their user_id.
Dynamic Parameter Handling: The API can perform operations based on a person's name, in addition to user_id.
Validation: Fields are validated to ensure they contain only strings; integers or other data types are not allowed.

#Installation
fastapi
unvicorn
requirement.txt
virtual environment

#testing
pytest

#Dynamic Parameter Handling
The API allows for dynamic parameter handling. You can use the GET /api/person?name={name} endpoint to fetch person details based on their name.