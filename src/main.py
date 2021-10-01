import uvicorn

from src.init import Init

from src.controladores.fastapi.roteadores.roteadores import roteador

def main():
    (_, _ctrl) = Init()()

    _ctrl.app.include_router(roteador)

    return _, _ctrl


if __name__ == '__main__':
    (_, ctrl) = main()
    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.porta)
