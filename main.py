from fastapi import FastAPI
import uvicorn as server
from api.controllers import router



app = FastAPI(
    title="Nginx",
    description="Example of FastAPI framework",
    version="1.0",
)

app.include_router(router, tags=["api.v1"])

if __name__ == "__main__":
    server.run("main:app", host="0.0.0.0", port=8000, reload=True)