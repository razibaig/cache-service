from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Payload(Base):
    __tablename__ = "payloads"

    id = Column(Integer, primary_key=True, index=True)
    input_1 = Column(String, index=True)
    input_2 = Column(String, index=True)
    output = Column(String, index=True)
