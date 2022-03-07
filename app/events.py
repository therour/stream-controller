from functools import lru_cache

class AppEvent:
    event = ""
    def get_event_name(self) -> str:
        return self.event


class EventsEmitter:
    @staticmethod
    @lru_cache
    def instance():
        return EventsEmitter()

    handlers = {}

    def emit(self, event: AppEvent):
        if self.handlers.get(event.get_event_name()) is not None:
            for handler in self.handlers[event.get_event_name()]:
                handler(event)


    def listen(self, event_name: str, handler):
        if self.handlers.get(event_name) is None:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)


def events_on(event_name: str):
    def decorator(func):
        EventsEmitter.instance().listen(event_name, func)

    return decorator
