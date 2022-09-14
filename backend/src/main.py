"""lhb-backend.src.main."""
from fastapi import FastAPI

from .api import router
from . import config


def init_app() -> FastAPI:
    """Init application"""
    application = FastAPI()
    application.include_router(router, prefix=config.API_PREFIX)
    return application


app = init_app()
