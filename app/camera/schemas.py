from typing import Optional
from pydantic import BaseModel


class CreateCamera(BaseModel):
    name: str
    source: str

class EditCamera(BaseModel):
    name: Optional[str] = None
    source: Optional[str] = None

class CameraResponse(BaseModel):
    id: int
    name: str
    source: str
