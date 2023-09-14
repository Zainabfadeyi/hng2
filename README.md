# FastAPI CRUD API - Person Resource

This is a simple REST API built with FastAPI that allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource. You can use this API to manage information about individuals, such as their name, age, and email address.

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## Table of Contents

- [Features](#features)
- [Endpoints](#endpoints)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the API](#running-the-api)
- [Usage](#usage)
- [Sample Requests and Responses](#sample-requests-and-responses)
- [Limitations and Assumptions](#limitations-and-assumptions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create a new person record.
- Retrieve details of a person by ID.
- Update the details of an existing person.
- Delete a person.
- Dynamic parameter handling for searching and performing operations based on name.
- Data validation to ensure that fields are of the correct data type (e.g., strings only for name and email).
- Robust error handling and responses.

## Endpoints

The API provides the following endpoints:

- **Create a Person**: `POST /api/`
- **Retrieve a Person**: `GET /api/{person_id}`
- **Update a Person**: `PUT /api/{person_id}`
- **Delete a Person**: `DELETE /api/{person_id}`

For detailed information on each endpoint, request/response formats, and sample usage, please refer to the [Endpoints](#endpoints) section.

## Getting Started

### Prerequisites

Before you can run this API, ensure you have the following installed:

- Python (3.11.5 recommended)
- FastAPI
- A database (e.g., SQLite for simplicity)
- SQLAlchemy (if using a relational database)
- Pydantic (for data validation)
- Uvicorn (for ASGI server)

You can install these dependencies using `pip`. See the [Installation](#installation) section for details.

### Create a virtual environment (optional but recommended):

python -m venv vir
source vir/bin/activate  

#### Install the required dependencies:

pip install -r requirements.txt

#### Running the API
Configure the database URL in the main.py file.

#### Run the API locally using Uvicorn:

uvicorn app:app --reload

Access the API at http://localhost:8000