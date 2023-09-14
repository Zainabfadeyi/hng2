# Person CRUD API Documentation
This document provides information about the Person CRUD API, including request/response formats, sample usage, limitations, and setup instructions.
# Endpoints
The API provides the following endpoints:

1. Create a Person
URL: /api/
Method: POST
Request Format:
    JSON Object with the following fields:
        name (string, required): The name of the person.
        age (integer): The age of the person.
        email (string): The email address of the person.
# Sample Request:

POST /api/
{
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}

# Response Format:

{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}

# Retrieve a Person
URL: /api/{person_id}
Method: GET

# Sample Request:
GET /api/1

# Response Format:

{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}

# Update a Person
URL: /api/{person_id}
Method: PUT
Request Format:
    JSON Object with the following fields (all optional):
        name (string): The updated name of the person.
        age (integer): The updated age of the person.
        email (string): The updated email address of the person.

# Sample Request:
PUT /api/1
{
  "name": "Updated Name",
  "age": 35
}

# Response Format:

{
  "message": "Person updated successfully"
}
#  Delete a Person
URL: /api/{person_id}
Method: DELETE

# Sample Request:
DELETE /api/1

# Response Format:
{
  "message": "Person deleted successfully"
}