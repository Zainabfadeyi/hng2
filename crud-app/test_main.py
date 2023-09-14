from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app instance
from fastapi import status

# Create a test client using your FastAPI app
client = TestClient(app=app)

def test_crud_api():
    # Create a new person
    create_response = client.post("/api", json={"name": "John Doe", "age": 30})
    # assert create_response.status_code == status.HTTP_200_OK
    created_person = create_response.json()
    print("Create Response:", created_person)

    # Get the details of the created person
    user_id = created_person["id"]
    read_response = client.get(f"/api/{user_id}")
    assert read_response.status_code == 200
    read_person = read_response.json()
    print("Read Response:", read_person)

    # Update the details of the person
    update_response = client.put(f"/api/{user_id}", json={"name": "Updated Name", "age": 35})
    assert update_response.status_code == status.HTTP_200_OK
    updated_person = update_response.json()
    print("Update Response:", updated_person)

    # Get the updated person details
    updated_read_response = client.get(f"/api/{user_id}")
    assert updated_read_response.status_code == status.HTTP_200_OK
    updated_read_person = updated_read_response.json()
    print("Updated Read Response:", updated_read_person)

    # Delete the person
    delete_response = client.delete(f"/api/{user_id}")
    assert delete_response.status_code == 200
    print("Delete Response:", delete_response.json())

    # Try to get the deleted person (should return 404)
    deleted_read_response = client.get(f"/api/{user_id}")
    assert deleted_read_response.status_code == 404
    print("Deleted Read Response:", deleted_read_response.text)

if __name__ == "__main__":
    test_crud_api()