"""This module includes initialization and main configuration of PassaGenAPI."""

from fastapi import FastAPI

from .routes import hash_routes, main_routes, password_routes

app = FastAPI()

app.include_router(main_routes)
app.include_router(password_routes)
app.include_router(hash_routes)
