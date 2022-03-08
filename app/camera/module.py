from fastapi import FastAPI

from app.events import EventsEmitter
from .events import setup_event_listeners
from .routes import router


def register_module(app: FastAPI):
    app.add_event_handler("startup", lambda: setup_event_listeners(EventsEmitter.instance()))

    app.include_router(router)
