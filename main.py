import threading
import time
import motion_detector
import gpio_connector
import camera_provider
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse


lock = threading.Lock()
video_capture = camera_provider.get_camera()
gpio = gpio_connector.GpioConnector()
detector = motion_detector.MotionDetector(gpio, video_capture, lock)


def launch_detector():
    detector.start_monitoring()


def rotate_and_freeze_detector(rotate_action):
    detector.continue_monitoring = False
    rotate_action()
    time.sleep(0.5)
    detector.continue_monitoring = True


print('detector initialization')
motion_detector_thread = threading.Thread(target=launch_detector)
motion_detector_thread.start()

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/get-photo")
def get_photo():
    detector.pause_monitoring()
    lock.acquire()
    path_photo = camera_provider.get_capture_file(video_capture)
    lock.release()
    detector.resume_monitoring()

    return FileResponse(path_photo, filename=path_photo)


@app.get("/rotate-right")
def rotate_camera_right():
    rotate_and_freeze_detector(gpio.rotate_right)


@app.get("/rotate-left")
def rotate_camera_left():
    rotate_and_freeze_detector(gpio.rotate_left)

@app.get("/get-video")
def get_video():
    directory = "captures"
    files = os.listdir(directory)
    files.sort()
    video_name = files[-1]
    return FileResponse(directory + '/' + video_name, filename=video_name)
