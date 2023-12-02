# from fastapi import FastAPI
from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# connection with mongodb instance
conn = MongoClient('mongodb+srv://NoorulNisa:Tgfe5JmMr5qUAJkI@cluster0.y7gmhsr.mongodb.net')

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

@app.get("/items/{item_id}/{q}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id, "q":q}

@app.get("/profile/{first_name}/{last_name}")
def read_profile(first_name: str, last_name: str):
    return {"name":first_name ,"lastname":last_name}

@app.get("/", response_class=HTMLResponse)
async def read_temp(request: Request):
    docs = conn.testdb.note_app.find({})
    for doc in docs:
        print(doc)
    return templates.TemplateResponse("index.html",{"request": request})


