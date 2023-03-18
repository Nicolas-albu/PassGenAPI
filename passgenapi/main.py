from fastapi import FastAPI

from passgenapi.routes.main_routes import main_routes
from passgenapi.routes.password_generation_routes import password_routes
from passgenapi.routes.hash_generation_routes import hash_routes

app = FastAPI()

app.include_router(main_routes)
app.include_router(password_routes)
app.include_router(hash_routes)