import cv2
from datetime import datetime

def get_camera():
    video = cv2.VideoCapture(0)
    if (not video.isOpened()):
        video = cv2.VideoCapture(1)

    return video

def get_capture_file(video_capture):
    ret, frame = video_capture.read()

    filename = "captures/capture_" + datetime.now().strftime("%d.%m.%Y__%H.%M.%S") + ".png"
    if not ret:
        print("Error reading camera photo")
        return ""

    if not cv2.imwrite(filename, frame):
        print("Error writing photo into file")
        return ""
    
    return filename