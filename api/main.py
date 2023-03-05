from fastapi import FastAPI

from api.routes.main_routes import main_routes
from api.routes.password_generation_routes import password_routes

app = FastAPI()

app.include_router(main_routes)
app.include_router(password_routes)