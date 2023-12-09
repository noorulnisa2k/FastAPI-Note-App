from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from datetime import datetime
from fastapi.responses import RedirectResponse

from models.note import Note
from config.db import conn
from schemas.note import *

note = APIRouter()

# Static files
note.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_note(request: Request):
    docs = conn.testdb.note_app.find({})
    data = []
    for doc in docs:
        data.append({
            "id":doc['_id'],
            "note":doc['todo_title'],
            "date":doc['created_at']
        })
    return templates.TemplateResponse("index.html",{"request": request, "data":data})

@note.post("/")
# Note is module
async def add_note(request: Request):
    form = await request.form()
    form_data = dict(form)
    form_data['created_at'] = datetime.now()
    form_data['todo-checkbox'] = 'off'
    data = conn.testdb.note_app.insert_one(form_data)
    # return noteEntity(data)
    return {'Success':True}
