from functools import cache

class AppEvent:
    event = ""
    def get_event_name(self) -> str:
        return self.event


class EventsEmitter:
    @cache
    @staticmethod
    def instance():
        return EventsEmitter()

    handlers = {}

    def emit(self, event: AppEvent):
        if self.handlers.get(event.get_event_name()) is not None:
            for handler in self.handlers[event.get_event_name()]:
                handler(event)


    def listen(self, event: AppEvent, handler):
        if self.handlers.get(event.get_event_name()) is None:
            self.handlers[event] = []
        self.handlers[event.name].append(handler)


def events_on(event: AppEvent):
    def decorator(func):
        EventsEmitter.instance().listen(event, func)

    return decorator
