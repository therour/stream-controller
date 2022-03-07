from fastapi import APIRouter, Response
from .schemas import CreateCamera, EditCamera
from .dependencies import camera_repository

router = APIRouter(prefix="/camera");

@router.get("/")
def get_all():
    cameras = camera_repository.get_all()
    return {
        "data": cameras
    }


@router.post("/")
def add(camera: CreateCamera):
    new_camera = camera_repository.add(camera)
    return Response(status_code=201, content={
        "data": new_camera,
    })


@router.get("/{id}")
def get(id: int):
    camera = camera_repository.find(id)
    return {
        "data": camera,
    }


@router.put("/{id}")
def edit(id: int, camera: EditCamera):
    camera = camera_repository.edit(id, camera)
    return {"data": camera}


@router.delete("/{id}")
def delete(id: int):
    camera_repository.delete(id)
    return Response(status_code=204)
