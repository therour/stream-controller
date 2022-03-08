from app.events import AppEvent, EventsEmitter
from app.streams.dependencies import add_stream, remove_stream, reset_stream
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


def setup_event_listeners(events_emitter: EventsEmitter):
    def on_camera_created(event: CameraCreated):
        stream_name = f"camera-{event.camera.id}"
        add_stream(
            name=stream_name,
            source=event.camera.source,
        )


    def on_camera_deleted(event: CameraDeleted):
        remove_stream(name=f"camera-{event.camera.id}")


    def on_camera_updated(event: CameraUpdated):
        reset_stream(
            name=f"camera-{event.camera.id}",
            source=event.camera.source,
        )


    events_emitter.on(CameraCreated.event, on_camera_created)
    events_emitter.on(CameraDeleted.event, on_camera_deleted)
    events_emitter.on(CameraUpdated.event, on_camera_updated)
