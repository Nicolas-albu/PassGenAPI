"""This module contains the main route of PassGenAPI."""

from fastapi import APIRouter, status

main_routes = APIRouter()


@main_routes.get("/")
async def root():
    """Return the status of the request from the main route.

    Returns:
        _type_: returns the state
    """
    return {"PassGenAPI": {"status": status.HTTP_200_OK}}
