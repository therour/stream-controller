from functools import cache
from fastapi import Depends

from app.events import EventsEmitter
from .repository import CameraRepository

@cache
def get_camera_repository(events_emitter: EventsEmitter = Depends(EventsEmitter.instance)):
    return CameraRepository(events_emitter)
