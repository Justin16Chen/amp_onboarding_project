import cv2

class Image_Publisher():
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def run(self):
        success, frame = self.cam.read()
        return frame if success else None