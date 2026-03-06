from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    assigned_user_id: str