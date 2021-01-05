from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint

class Homepage(HTTPEndpoint):
    async def get(self, request):
        if request.user.is_authenticated:
            return PlainTextResponse('Todo! ' + request.user.display_name)
        return PlainTextResponse('Todo!')
