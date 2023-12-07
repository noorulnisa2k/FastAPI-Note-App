from pydantic import BaseModel
from datetime import date

class Note(BaseModel):
    todo_title: str
    todo_checkbox: bool
    created_at: date
