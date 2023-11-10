from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String, Text, Date
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(100))
    complete = Column(Boolean, default=False)

    # comment le backend et le frontenjd interagissent ensemble, exemple de fastapi et de jinja