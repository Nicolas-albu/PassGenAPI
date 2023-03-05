from fastapi import FastAPI

from app.routes.password_generation_routes import password_routes

app = FastAPI()

app.include_router(password_routes)