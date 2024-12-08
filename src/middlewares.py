
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from collections import defaultdict
from time import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int, time_window: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        route = request.scope["path"]
        key = f"{client_ip}:{route}"

        current_time = time()
        self.requests[key] = [
            timestamp for timestamp in self.requests[key] if current_time - timestamp < self.time_window
        ]

        if len(self.requests[key]) >= self.max_requests:
            raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")

        self.requests[key].append(current_time)
        return await call_next(request)
