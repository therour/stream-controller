class Camera(object):
    id: int
    name: str
    source: str

    def __init__(self, id, name, source) -> None:
        self.id = id
        self.name = name
        self.source = source

    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'source': self.source
        }

    def __copy__(self):
        return type(self)(self.id, self.name, self.source)
        
