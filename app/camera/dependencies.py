from functools import lru_cache
from fastapi import Depends

from app.events import EventsEmitter
from .repository import CameraRepository

@lru_cache()
def get_camera_repository(events_emitter: EventsEmitter = Depends(EventsEmitter.instance)):
    return CameraRepository(events_emitter)
