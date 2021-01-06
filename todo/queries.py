from .tables import todos
from resources import database

async def resolve_todos(_, info):
    try:
        query = todos.select()
        results = await database.fetch_all(query)
        content = [
            {
                "id": result["id"],
                "title": result["title"],
                "created_on": result["created_on"],
                # "modified_on": result["modifed_on"],
                "completed": result["completed"]
            }
            for result in results
        ]
        payload = {
            "success": True,
            "records": content
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

async def resolve_todo(_, info, todoId):
    try:
        query = todos.select().where(todos.c.id == todoId)
        result = await database.fetch_one(query)
        content = {
                "id": result["id"],
                "title": result["title"],
                "created_on": result["created_on"],
                "completed": result["completed"]
            }
        payload = {
            "success": True,
            "record": content
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload