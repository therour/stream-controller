from app.events import AppEvent, events_on
from app.streams.dependencies import add_stream, remove_stream, reset_stream
from app.streams.streaming import StreamingThread
from .model import Camera


class CameraEventPayload(AppEvent):
    def __init__(self, camera: Camera) -> None:
        self.camera = camera

class CameraCreated(CameraEventPayload):
    event = "camera:created"

class CameraUpdated(CameraEventPayload):
    event = "camera:updated"

class CameraDeleted(CameraEventPayload):
    event = "camera:deleted"


def setup_event_listeners():
    @events_on(CameraCreated.event)
    def on_camera_created(event: CameraCreated):
        stream_name = f"camera-${event.camera.id}"
        add_stream(
            name=stream_name,
            source=event.camera.source,
        )


    @events_on(CameraDeleted.event)
    def on_camera_deleted(event: CameraDeleted):
        remove_stream(name=f"camera-${event.camera.id}")


    @events_on(CameraUpdated.event)
    def on_camera_updated(event: CameraUpdated):
        reset_stream(
            name=f"camera-${event.camera.id}",
            source=event.camera.source,
        )
