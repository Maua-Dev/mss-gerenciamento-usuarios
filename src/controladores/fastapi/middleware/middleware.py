from fastapi import Request, Response
import httpx
import asyncio

from starlette.responses import JSONResponse


async def add_redirect_auth(request: Request, call_next):
    bearer = request.headers['Authorization']  # Pegamoso header
    token = bearer.split()[1]  # separamos o token

    res = await _enviaParaValidar(token)  # Enviamos para GetAuthw -> Ele joga erro se falhar

    if res.status_code == 200:
        response = await call_next(request)
    else:
        response = Response(content=res.content, status_code=res.status_code)

    return response



async def _enviaParaValidar(token: str):
    async with httpx.AsyncClient() as client:
        task = await client.get("http://localhost:8000/validar", headers={"Authorization": "Bearer " + token})
        return task


