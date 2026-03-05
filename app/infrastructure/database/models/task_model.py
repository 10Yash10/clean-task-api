from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# We are defining database tables using Python classes.
Base = declarative_base();

class TaskModel(Base):
    # This maps the class to a database table.
    __tablename__ = "Task"

    # This tells about the columns in tha database table.
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    priority = Column(String)
    assigned_user_id = Column(String)