from .tables import todos
from resources import database
from starlette.responses import JSONResponse


async def list_todo(request):
    query = todos.select()
    results = await database.fetch_all(query)
    # needs debuging
    # import pdb; pdb.set_trace()
    content = [
        {
            "title": result["title"],
            "created_on": result["created_on"],
            # "modified_on": result["modifed_on"],
            "completed": result["completed"]
        }
        for result in results
    ]
    return JSONResponse(content)

async def add_todo(request):
    data = await request.json()
    query = todos.insert().values(
       title=data["title"],
       completed=data["completed"]
    )
    await database.execute(query)
    return JSONResponse({
        "title": data["title"],
        "completed": data["completed"]
    })