class Task:
    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        status: str,
        priority: str,
        assigned_user_id: int
    ):
        self.id = id,
        self.title = title,
        self.description = description,
        self.status = status,
        self.priority = priority,
        self.assigned_user_id = assigned_user_id