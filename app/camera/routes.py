from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.camera.repository import CameraRepository
from .schemas import CreateCamera, EditCamera
from .dependencies import get_camera_repository

router = APIRouter(prefix="/camera");

@router.get("/")
def get_all(camera_repository: CameraRepository = Depends(get_camera_repository)):
    cameras = camera_repository.get_all()
    return {
        "data": cameras
    }


@router.post("/")
def add(camera: CreateCamera, camera_repository: CameraRepository = Depends(get_camera_repository)):
    new_camera = camera_repository.add(camera)
    return JSONResponse(status_code=201, content={
        "data": new_camera,
    })


@router.get("/{id}")
def get(id: int, camera_repository: CameraRepository = Depends(get_camera_repository)):
    camera = camera_repository.find(id)
    return {
        "data": camera,
    }


@router.put("/{id}")
def edit(id: int, camera: EditCamera, camera_repository: CameraRepository = Depends(get_camera_repository)):
    camera = camera_repository.edit(id, camera)
    return {"data": camera}


@router.delete("/{id}")
def delete(id: int, camera_repository: CameraRepository = Depends(get_camera_repository)):
    camera_repository.delete(id)
    return JSONResponse(status_code=204)
