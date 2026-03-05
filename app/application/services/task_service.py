from typing import Optional, List

from app.domain.interfaces.itask_repository import ITaskRepository
from app.domain.entities.task import Task

class TaskService:

    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository



def create_task(self, title: str, description: str, priority: str, assigned_user_id: int) -> Task:
    if priority not in ['low', 'medium', 'high']:
        raise ValueError('Invalid priority')

    task = Task(
        id=None,
        title=title,
        description=description,
        status="todo",   # By default the status will be todo
        priority=priority,
        assigned_user_id=assigned_user_id
    )

    return self.task_repository.create(task)


def get_task(self, task_id: int) -> Optional[Task]:
    task = self.task_repository.get_by_id(task_id)

    return task


def list_task(self) -> List[Task]:
    return self.task_repository.get_all()


def update_task_status(self, task_id: int, new_status: str) -> Task:
    task = self.task_repository.get_by_id(task_id)

    if not task:
        raise ValueError("Task not Found")

    if task.status == "done" and new_status == "todo":
        raise ValueError("Task cannot move from DONE to TODO")

    task.status = new_status

    return self.task_repository.update(task)


def delete_task(self, task_id: int) -> None:
    task = self.task_repository.get_by_id(task_id)

    if not task:
        raise ValueError("Task not Found")

    return self.task_repository.delete(task_id)