from resources import database
from .tables import todos


async def resolve_create_todo(_, info, **kwargs):
    try:
        title = kwargs.get('title')
        completed = kwargs.get('completed', False)
        query = todos.insert().values(
            title=title,
            completed=completed
            )
        result = await database.execute(query)
        
        payload = {
            "success": True,
            "record": {
                "id": result,
                "title": title,
                "completed": completed
            }
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


async def resolve_complete_todo(_, info, todoId):
    try:
        query = todos.update().where(todos.c.id == todoId).values(
            completed=True
            )
        await database.execute(query)

        query_record = todos.select().where(todos.c.id == todoId)
        record = await database.fetch_one(query_record)
        content = {
            "id": record["id"],
            "title": record["title"],
            "created_on": record["created_on"],
            "completed": record["completed"]
        }
        payload = {
            "success": True,
            "record": content
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors":  [f"Todo matching id {todo_id} was not found"]
        }

    return payload


async def resolve_delete_todo(_, info, todoId):
    try:
        query = todos.delete().where(todos.c.id == todoId)
        await database.execute(query)

        payload = {
            "success": True,
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors":  [f"Todo matching id {todo_id} was not found"]
        }

    return payload