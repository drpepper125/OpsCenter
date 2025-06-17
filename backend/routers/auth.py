from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
# Use BASE_DIR resolution in main.py for templates directory
# Jinja2Templates will be configured in main.py

@router.get("/login")
async def login_form(request: Request):
    return request.app.state.templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Dummy auth logic: only 'admin'/'password' succeeds
    if username == "admin" and password == "password":
        return RedirectResponse(url="/welcome", status_code=302)
    return RedirectResponse(url="/failed", status_code=302)

@router.get("/welcome")
async def welcome(request: Request):
    return request.app.state.templates.TemplateResponse("welcome.html", {"request": request})

@router.get("/failed")
async def failed(request: Request):
    return request.app.state.templates.TemplateResponse("failed.html", {"request": request})