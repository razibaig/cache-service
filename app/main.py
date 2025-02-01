from fastapi import FastAPI
from app.api import payload
from app.core.database import engine, Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the routes
app.include_router(payload.router)
