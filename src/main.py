import uvicorn

from src.init import Init


def main():
    (_, _, _, _ctrl) = Init()()
    return _, _, _, _ctrl


if __name__ == '__main__':
    (_, _, _, ctrl) = main()
    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.porta)
