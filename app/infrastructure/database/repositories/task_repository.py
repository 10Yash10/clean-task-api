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
        models = self.db.query(TaskModel).all()

        tasks = []

        for model in models:
            tasks.append(
                Task(
                    id=model.id,
                    title=model.title,
                    description=model.description,
                    status=model.status,
                    priority=model.priority,
                    assigned_user_id=model.assigned_user_id
                )
            )

        return tasks

    
    # method to create a task
    def create(self, task: Task) -> Task:
        model = Task(
            title=task.title,
            description=task.description,
            status=task.status,
            priority=task.priority,
            assigned_user_id=task.assinged_user_id,
        )

        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)

        return Task(
            id = model.id,
            title=model.title
            description=model.description,
            status=model.status,
            priority=model.priority,
            assigned_user_id=model.assigned_user_id
        )


    # method to update the exisiting task
    def update(self, task:Task) -> Task:

        # fetch the model from database
        model = self.db.query(TaskModel).filter(TaskModel.id == task.id).first()

        if not model:
            return Null

        # update the model with new task values
        model.title=task.title
        model.description=task.description
        model.status=task.status
        model.priority=task.priority
        model.assigned_user_id=task.assigned_user_id

        # update the database with updated model
        self.db.commit()
        self.db.refresh(model)

        return Task(
            id=model.id,
            title=model.title,
            description=model.description,
            status=model.status,
            priority=model.priority,
            assigned_user_id=model.assigned_user_id
        )