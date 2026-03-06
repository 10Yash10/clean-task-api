from pydantic import BaseModel

class TaskRequest(BaseModel):
    title: str
    description: str
    priority: str
    assigned_user_id: int
