from fastapi import FastAPI

from .events import setup_event_listeners
from .routes import router


def register_module(app: FastAPI):
    app.add_event_handler("startup", setup_event_listeners)

    app.include_router(router)
