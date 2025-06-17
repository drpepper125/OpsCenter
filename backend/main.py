import pathlib
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import test, auth

# Initialize FastAPI app
app = FastAPI(title="OpsCenter")

# Resolve base directory for consistent paths
BASE_DIR = pathlib.Path(__file__).resolve().parent

# Mount static files directory
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# Configure Jinja2 templates and store in app state
templates = Jinja2Templates(directory=BASE_DIR / "templates")
app.state.templates = templates

# Include routers
app.include_router(test.router, prefix="/api")
app.include_router(auth.router)

# Landing page -> login screen
@app.get("/", include_in_schema=False)
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})