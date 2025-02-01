from fastapi.testclient import TestClient
from app.main import app
from app.core.database import SessionLocal
from app.models.payload_model import Payload

client = TestClient(app)

def test_create_payload():
    # Clear the database before the test
    db = SessionLocal()
    db.query(Payload).delete()
    db.commit()

    response = client.post("/payload", json={
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    })
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response
    assert "output" in json_response

    # Verify that the payload is stored in the database
    db_payload = db.query(Payload).filter(Payload.id == json_response["id"]).first()
    assert db_payload is not None
    assert db_payload.input_1 == "first string,second string,third string"
    assert db_payload.input_2 == "other string,another string,last string"
    assert db_payload.output == "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"

    db.close()

def test_read_payload():
    # Create a payload to ensure it exists
    response = client.post("/payload", json={
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    })
    payload_id = response.json()["id"]

    # Test reading the payload
    response = client.get(f"/payload/{payload_id}")
    assert response.status_code == 200
    json_response = response.json()
    assert "output" in json_response
    assert json_response["output"] == "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"