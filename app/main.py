from fastapi import FastAPI

import app.streams.module as streams
import app.camera.module as camera


app = FastAPI()

streams.register_module(app)
camera.register_module(app)
