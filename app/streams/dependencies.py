from typing import Dict

from app.streams.streaming import StreamingThread


streamings: Dict[str, StreamingThread] = dict()

def add_stream(name: str, source: str):
    thread = StreamingThread(source, name)
    streamings.update({name: thread})
    thread.start()


def reset_stream(name: str, source: str):
    thread = streamings.pop(name)
    if thread.is_alive():
        thread.stop()

    add_stream(name, source)


def remove_stream(name: str):
    thread = streamings.pop(name)
    if thread.is_alive():
        thread.stop()


def stop_all_streamings():
    for stream in streamings.values():
        stream.stop()

    for stream in streamings.values():
        stream.join()
