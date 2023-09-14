# API Documentation

This document provides detailed information about the API endpoints, including the standard request and response formats, as well as sample usage scenarios.

## Endpoints

The API offers the following endpoints:

1. **Create a Person**
   - **Endpoint:** `/api/`
   - **Method:** POST
   - **Request Format:**
     ```json
     {
       "name": "string (required)",
       "age": "integer",
       "email": "string"
     }
     ```
   - **Response Format:**
     ```json
     {
       "id": "integer (auto-generated)",
       "name": "string",
       "age": "integer",
       "email": "string"
     }
     ```

2. **Read a Person**
   - **Endpoint:** `/api/{person_id}`
   - **Method:** GET
   - **Response Format:**
     ```json
     {
       "id": "integer",
       "name": "string",
       "age": "integer",
       "email": "string"
     }
     ```

3. **Update a Person**
   - **Endpoint:** `/api/{person_id}`
   - **Method:** PUT
   - **Request Format:**
     ```json
     {
       "name": "string",
       "age": "integer",
       "email": "string"
     }
     ```
   - **Response Format:**
     ```json
     {
       "message": "successful"
     }
     ```

4. **Delete a Person**
   - **Endpoint:** `/api/{person_id}`
   - **Method:** DELETE
   - **Response Format:**
     ```json
     {
       "message": "successful"
     }
     ```

## Sample Usage

### Creating a New Person

**Request:**

```http
POST /api/
Content-Type: application/json

{
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}

**Expected Response**

{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com"
}


