
# to convert mongodb object into pythonic dictionary
def noteEntity(item) -> dict:
    return {
        "_id": str(item["id"]),
        "todo_title": item["todo_title"],
        "todo_checkbox": item["todo_checkbox"],
        "created_at": item["created_at"]
    }

def notesEntity(items) -> list:
    return [ noteEntity(item) for item in items]