import logging
from typing import Dict

from app.streams.streaming import StreamingThread


log = logging.getLogger(__name__)
streamings: Dict[str, StreamingThread] = dict()

def add_stream(name: str, source: str):
    print("Adding stream:", name, source)
    thread = StreamingThread(source, name)
    streamings.update({name: thread})
    thread.start()


def reset_stream(name: str, source: str):
    print("Resetting stream:", name, source)
    thread = streamings.get(name)

    thread.source = source

    thread.reset()

    # thread = streamings.pop(name)
    # if thread.is_alive():
    #     thread.stop()
    # add_stream(name, source)


def remove_stream(name: str):
    print("Removing stream:", name)
    thread = streamings.pop(name)
    if thread.is_alive():
        thread.stop()


def stop_all_streamings():
    for stream in streamings.values():
        stream.stop()

    for stream in streamings.values():
        stream.join()
