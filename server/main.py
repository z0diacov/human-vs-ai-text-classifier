from fastapi.templating import Jinja2Templates

from fastapi import (
    FastAPI,
    Request
)

from server.routers import api_router

app = FastAPI()

app.include_router(api_router)

jinja_templates = Jinja2Templates(directory="server/templates")

@app.get("/")
async def root(request: Request):
    return jinja_templates.TemplateResponse("index.html", {"request": request})