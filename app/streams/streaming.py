from threading import Thread
import numpy as np
import time
import cv2


class StreamingThread(Thread):
    def __init__(self, source, name):
        Thread.__init__(self)
        self.name = name
        self.source = source

        self.capture = None  # type: cv2.VideoCapture
        self.current_frame = None
        self.status = "ready"

        self.should_stop = False
        self.should_flip = str(self.source).isnumeric()

    def reset(self):
        self.status = "need_restart"

    def run(self):
        try:
            self.status = "starting"
            self.capture = cv2.VideoCapture(self.source)
            while True:
                time.sleep(0.02)

                if self.status == "need_restart":
                    self.status = "starting"
                    self.capture = cv2.VideoCapture(self.source)
                    time.sleep(3)


                if self.should_stop:
                    self.should_stop = False
                    break

                success, frame = self.capture.read()
                if not success:
                    self.current_frame = np.zeros((240, 320, 3), np.uint8)
                    time.sleep(1)
                    self.current_frame = cv2.imencode('.png', frame)[1].tobytes()
                    self.status = "failing"

                else:
                    self.status = "running"
                    frame = image_resize(frame, width=320)

                    if self.should_flip:
                        frame = cv2.flip(frame, 1)

                    ## Assume here for Hard Processing
                    
                    self.current_frame = cv2.imencode('.png', frame)[1].tobytes()
        finally:
            self.current_frame = None
            self.capture.release()


    def stream_frame(self):
        while self.current_frame:
            if self.status == "failing":
                time.sleep(1)
            else:
                time.sleep(0.02)

            yield self.current_frame


    def stop_frame(self):
        pass


    def stop(self):
        self.should_stop = True
        return True


# class VideoWriterThread(Thread):
#     def __init__(self, frame_generator, filename):
#         Thread.__init__(self)
#         self.frame_generator = frame_generator
#         self.should_stop = False

#         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#         self.video_writer = cv2.VideoWriter(filename, fourcc, 30, (640, 480))

#     def run(self) -> None:
#         try:
#             for frame in self.frame_generator():
#                 if self.should_stop: break

#                 self.video_writer.write(frame)
#         finally:
#             self.video_writer.release()
    
#     def end(self):
#         self.should_stop = True



def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
        pass

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized
