from typing import Callable
from fastapi import FastAPI, Request, Response
from src.middlewares.global_middleware import global_middleware
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(main_router)

        
app.middleware("http")(global_middleware)