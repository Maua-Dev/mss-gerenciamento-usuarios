import uvicorn

from src.init import Init

def main():
    (_, _ctrl) = Init()()
    return _, _ctrl


if __name__ == '__main__':
    (_, ctrl) = main()
    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.porta)
