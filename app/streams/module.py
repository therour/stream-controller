from fastapi import FastAPI

from app.streams.streaming import StreamingThread
from .routes import router
from .dependencies import add_stream, stop_all_streamings

def register_module(app: FastAPI):
    app.add_event_handler("shutdown", stop_all_streamings)

    # add_stream(source=0, name="webcam")
    # add_stream(app, StreamingThread(0), "stream1")
    # register_thread(app, StreamingThread("rtsp://admin:011118Widya!@192.168.0.10:554/cam/realmonitor?channel=4&subtype=0"), "stream4")

    app.include_router(router)
