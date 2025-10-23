import time
from fastapi import Request
from typing import Callable


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

