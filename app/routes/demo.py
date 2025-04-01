from fastapi import APIRouter, Request
from . import templates


router = APIRouter(prefix="/demo")


@router.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
