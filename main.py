from fastapi import FastAPI, HTTPException, Request
from settings import settings
from core.container import container_routes
import asyncio
import time
from async_timeout import timeout
import logging
_log = logging.getLogger(__file__)
from starlette.middleware.cors import CORSMiddleware
from core.instances import init_db


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    
    ##SOLO EN PRODUCCION
    # docs_url=None,
    # redoc_url=None,
    # openapi_url=None,
)


class TimeoutMiddleware:
    def __init__(self, app: FastAPI, timeout_seconds: int = 12):
        self.app = app
        self.timeout_seconds = timeout_seconds

    async def __call__(self, request: Request, call_next):
        start_time = time.time()
        try:
            async with timeout(self.timeout_seconds):
                response = await call_next(request)
            return response
        except asyncio.TimeoutError:
            _log.warning(
                f"TimeoutMiddleware: Request timed out after {time.time() - start_time} seconds.",
                extra={"path": request.url.path},
            )
            raise HTTPException(status_code=408, detail="Por favor intenta de nuevo.")


app.middleware("http")(TimeoutMiddleware(app, 12))

init_db()
##Inicializar las rutas de los controladores
container_routes(app)



def init_middlewares(app: FastAPI):
    # Configuration of CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )


init_middlewares(app)


