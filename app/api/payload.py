from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.core.transformer import generate_payload
from app.core.database import SessionLocal
from app.models.payload_model import Payload
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

class PayloadRequest(BaseModel):
    list_1: List[str]
    list_2: List[str]

class PayloadResponse(BaseModel):
    output: str

# Utility function to get DB session
def get_db():
    """
    Provides a database session for dependency injection.

    Yields:
        Session: A SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/payload", response_model=dict)
def create_payload(payload: PayloadRequest, db: Session = Depends(get_db)):
    """
    Creates a new payload by transforming and interleaving two lists of strings.

    Args:
        payload (PayloadRequest): The request body containing two lists of strings.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the payload ID and the transformed output.
    """
    # Check if the input already exists in the database
    db_payload = db.query(Payload).filter(
        Payload.input_1 == ','.join(payload.list_1),
        Payload.input_2 == ','.join(payload.list_2)
    ).first()
    
    if db_payload:
        # return cached flag as True since the output is coming from cache
        return {"id": db_payload.id, "cached": True, "output": db_payload.output}

    # Use the transformer to generate the payload
    transformed_output = generate_payload(payload.list_1, payload.list_2)

    # Store the new payload in the database
    new_payload = Payload(
        input_1=','.join(payload.list_1),
        input_2=','.join(payload.list_2),
        output=transformed_output
    )
    db.add(new_payload)
    db.commit()
    db.refresh(new_payload)
    # return cached flag as False since the output is not from cache
    return {"id": new_payload.id, "cached": False, "output": transformed_output}

@router.get("/payload/{id}", response_model=PayloadResponse)
def read_payload(id: int, db: Session = Depends(get_db)):
    """
    Retrieves a payload by its ID.

    Args:
        id (int): The ID of the payload to retrieve.
        db (Session): The database session.

    Returns:
        PayloadResponse: The response containing the output of the payload.

    Raises:
        HTTPException: If the payload is not found.
    """
    db_payload = db.query(Payload).filter(Payload.id == id).first()
    if db_payload is None:
        raise HTTPException(status_code=404, detail="Payload not found")
    return {"output": db_payload.output}
