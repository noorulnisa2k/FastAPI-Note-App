from pydantic import BaseModel
from datetime import date

class Note(BaseModel):
    todo_title: str
    todo_checkbox: bool | None = None
    created_at: date = date.today()
