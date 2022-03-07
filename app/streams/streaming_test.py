from .streaming import image_resize
import numpy as np

def test_should_resize_width():
    image = np.zeros((720, 1280, 3), dtype=np.uint8)
    resized = image_resize(image, width=300)
    assert resized.shape[1] == 300
    assert resized.shape[0] == int(720/1280*300)

def test_should_resize_height():
    image = np.zeros((720, 1280, 3), dtype=np.uint8)
    resized = image_resize(image, height=300)
    assert resized.shape[0] == 300
    assert resized.shape[1] == int(1280/720*300)
