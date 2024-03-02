from fastapi import APIRouter, Request, Response, status
from .serializer import Form

router = APIRouter()


@router.get("/headers")
async def headers(request: Request) -> Response:
    json = {
        "host": request.headers["host"],
        "user_agent": request.headers["user-agent"],
        "content_type": request.headers["content-type"],
        "content_length": request.headers["content-length"],
        "status": request.headers["connection"],
    }
    return Response(content=str(json), status_code=status.HTTP_200_OK)


@router.post("/form")
async def form(f: Form) -> Response:
    return Response(content=str(f), status_code=status.HTTP_202_ACCEPTED)