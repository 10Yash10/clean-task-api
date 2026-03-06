from fastapi import APIRouter, Depends

from app.deps import get_task_service
from app.application.services.task_service import TaskService
from app.presentation.schemas.task.task_create_request import TaskCreateRequest
from app.presentation.schemas.task.task_update_status_request import TaskStatusUpdateRequest
from app.presentation.schemas.task.task_response import TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(
    request: TaskRequest,
    service: TaskService = Depends(get_task_service)
):
    task = service.create_task(
        title=request.title,
        description=request.description,
        priority=request.priority,
        assigned_user_id=request.assigned_user_id
    )

    return TaskResponse(**task.__dict__)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)    
):
    task = service.get_task(task_id)

    return TaskResponse(**task.__dict__)


@router.get("/", response_model=list[TaskResponse])
def list_task(
    service: TaskService = Depends(get_task_service)
):
    tasks = service.list_task()

    return [TaskResponse(**task.__dict__) for task in tasks]

@router.put("/{task_id}/status", response_model=TaskUpdateStatusRequest)
def update_status(
    task_id: int,
    request: TaskRequest,
    service: TaskService = Depends(get_task_service)
):
    task = service.update_task_status(task_id, request.status)

    return TaskResponse(**task.__dict__)

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    service.delete_task(task_id)

    return {"message": "Task Deleted"}
