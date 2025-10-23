from fastapi import FastAPI
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(main_router)

        




    
