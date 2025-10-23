from typing import Callable
from fastapi import FastAPI, Request, Response
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(main_router)

        
@app.middleware("http")
async def global_middleware(request: Request, call_next: Callable):
    ip_address = request.client.host
    # if ip_address in ['127.0.0.1']:
    #     return Response(status_code=429, content="Вы превысли кол-во запросов")
    
    print(f"{ip_address}")
    
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print(f"Время обработки запрос: {end}")
    response.headers['X-Special'] = "I am speacial"
    return response


