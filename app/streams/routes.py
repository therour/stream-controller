import time
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from starlette.background import BackgroundTask


from .streaming import StreamingThread
from .dependencies import streamings


router = APIRouter()

@router.get('/')
def show(fps: int = 15):
    return ", ".join(list(streamings.keys()))


@router.get('/streams/{name}/stream')
def get_stream(name: str, fps: int = 15):
    stream: StreamingThread = streamings.get(name)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")

    return StreamingResponse(
        content=stream_generator(stream, fps),
        media_type='multipart/x-mixed-replace; boundary=frame',
        background=BackgroundTask(stream.stop_frame)
    )

@router.get('/streams/{name}')
def show(name: str, fps: int = 15):
    html = f"""
    <!DOCTYPE html>
    <html>
        <head><title>Streaming</title></head>
        <body>
            <img width="1024" src="/streams/{name}/stream?fps={fps}" />
        </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)


def stream_generator(stream: StreamingThread, fps: int):
    fps_sleep = 1/fps
    for frame in stream.stream_frame():
            time.sleep(fps_sleep)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
