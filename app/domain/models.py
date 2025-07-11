from pydantic import BaseModel
from typing import Literal

Role = Literal["admin", "supervisor", "usuario"]

class User(BaseModel):
    username: str
    password: str
    role: Role