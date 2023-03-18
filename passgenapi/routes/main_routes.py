from fastapi import APIRouter, status

main_routes = APIRouter()

@main_routes.get("/")
async def root():
    return {
        "PassGenAPI": {
            "status": status.HTTP_200_OK
            }
        }