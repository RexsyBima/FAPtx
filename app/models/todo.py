from pydantic import BaseModel
from pydantic.fields import Field
from datetime import datetime


class Todo(BaseModel):
    title: str
    done: bool = Field(default=False)
    added: datetime = Field(default_factory=datetime.now)
