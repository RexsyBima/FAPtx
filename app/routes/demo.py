from fastapi import APIRouter, Request
from . import templates
from app.models.todo import Todo


router = APIRouter(prefix="/demo")


@router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@router.get("/todos")
async def view_todos(request: Request):
    todos = [
        Todo(title="Buy milk"),
        Todo(title="Buy eggs"),
        Todo(title="Buy bread"),
    ]
    return templates.TemplateResponse(
        request=request, name="view_todos.html", context={"todos": todos}
    )
