import cv2
import threading


class CamThread(threading.Thread):
    def __init__(self, PreviewName, CamId):
        threading.Thread.__init__(self)
        self.PreviewName = PreviewName
        self.CamId = CamId

    def run(self):
        print('Starting' + self.PreviewName)
        CamPreview(self.PreviewName, self.CamId)


def CamPreview(PreviewName, CamId):
    cv2.namedWindow(PreviewName)
    cam = cv2.VideoCapture(CamId)
    if cam.isOpened():  # capturando o primeiro frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        rval, frame = cam.read()
        cv2.imshow(PreviewName, frame)
        key = cv2.waitKey(20)
        if key == 27:  # saída com ESC
            break
    cv2.destroyWindow(PreviewName)


# Cria as threads
thread1 = CamThread("Camera 1", 1)
thread0 = CamThread("Camera 0", 0)
thread1.start()
thread0.start()
