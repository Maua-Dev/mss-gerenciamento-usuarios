from typing import Any

from pydantic import BaseModel


class ResPadrao(BaseModel):
    msg: str


class ResRoot(BaseModel):
    deployment: dict
    controlador: dict


class ResArg(BaseModel):
    arg: Any
    msg: str
