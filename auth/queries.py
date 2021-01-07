from .tables import users
from resources import database

async def resolve_users(_, info):
    try:
        query = users.select()
        results = await database.fetch_all(query)
        content = [
            {"id": result["id"], "username": result["username"]}
            for result in results]
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