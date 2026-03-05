from sqlalchemy import Session
from typing import Optional, List

from app.domain.interfaces.itask_repository import ITaskRepository
from app.domain.entities.task import Task
from app.infrastructure.database.models import TaskModel

class TaskRepository(ITaskRepository):

    def __init__(self, db: Session):
        self.db = db

    # method to get a task by id
    def get_by_id(task_id: int) -> Optional[Task]:
        model = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        
        if not model:
            return None

        return Task(
            id=model.id,
            title=model.title,
            description=model.description,
            status=model.status,
            priority=model.priority,
            assigned_user_id=model.assigned_user_id,
        )

    
    # method to get all tasks
    def get_all() -> List[Task]: