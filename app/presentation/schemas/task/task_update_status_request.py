import pydantic from BaseModel

class TaskUpdateStatusRequest(BaseModel):
    status: str