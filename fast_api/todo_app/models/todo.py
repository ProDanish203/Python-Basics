from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
