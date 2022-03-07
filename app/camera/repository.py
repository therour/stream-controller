from copy import copy
from typing import List, Optional
from app.camera.events import CameraCreated, CameraDeleted, CameraUpdated, EventsEmitter

from app.camera.schemas import CreateCamera, EditCamera
from .model import Camera


class CameraRepository:
    data = []
    incrementor = 0
    events: EventsEmitter

    def __init__(self, events_emitter) -> None:
        self.events = events_emitter

    def get_all(self) -> List[Camera]:
        return self.data.copy()

    def find(self, id: int) -> Optional[Camera]:
        for camera in self.data:
            if camera.id == id:
                return camera
        return None

    def add(self, data: CreateCamera) -> Camera:
        camera = Camera(self._generate_id(), data.name, data.source)
        self.data.append(camera)
        self.events.emit(CameraCreated(camera))

        return camera

    def edit(self, id: int, data: EditCamera) -> Camera:
        camera = self.find(id)
        camera.name = data.name
        camera.source = data.source
        self.events.emit(CameraUpdated(camera))

        return camera;

    def delete(self, id):
        camera = self.find(id)
        if camera:
            deleted_camera = copy(camera)
            self.data.remove(camera)
            self.events.emit(CameraDeleted(deleted_camera))



    def _generate_id(self):
        self.incrementor += 1
        return self.incrementor
    