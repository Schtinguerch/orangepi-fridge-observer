import cv2
import numpy as np

from threading import Timer
from datetime import datetime


class MotionDetector:
    def __init__(self, gpio_connector, video, lock):
        self.continue_monitoring = True
        self.continue_recording = False
        self.timer_started = False
        self.gpio_connector = gpio_connector
        self.camera_index = 0
        self.video = video
        self.lock = lock


    def start_monitoring(self):
        previous_frame = None
        print("OpenCV motion detector started")

        while True:
            if (not self.timer_started) and (not self.continue_monitoring):
                continue

            self.lock.acquire()
            _, cur_frame = self.video.read()
            self.lock.release()

            #if cur_frame is None:
            #    self.video = cv2.VideoCapture(self.camera_index)
            #    continue

            prepared_frame = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
            prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(15, 15), sigmaX=0)

            if previous_frame is None:
                previous_frame = prepared_frame
                continue

            diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
            previous_frame = prepared_frame

            kernel = np.ones((5, 5))
            diff_frame = cv2.dilate(diff_frame, kernel, 1)

            thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]
            contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                self.lock.acquire()
                ret, frame = self.video.read()
                self.lock.release()

                if not self.continue_recording:
                    self.start_recording()

                if self.timer_started:
                    self.timer.cancel()

                self.start_timer()

            if self.continue_recording:
                now_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
                cv2.putText(frame, now_time, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
                self.result.write(frame)


    def pause_monitoring(self):
        self.continue_monitoring = False


    def resume_monitoring(self):
        self.continue_monitoring = True
    

    def start_recording(self):
        start_time = datetime.now().strftime("%d.%m.%Y__%H.%M.%S")

        self.filename = "captures/record_" + start_time + ".mp4"
        self.continue_recording = True

        self.lock.acquire()
        size = (int(self.video.get(3)), int(self.video.get(4)))
        self.lock.release()

        self.result = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*"MP4V"), 8, size)

        self.gpio_connector.make_noise()
        print(f"{start_time}: motion detected")


    def stop_recording(self):
        self.continue_recording = False
        self.timer_started = False

        self.result.release()
        self.gpio_connector.stop_noise()

        end_time = datetime.now().strftime("%d.%m.%Y__%H.%M.%S")
        print(f"{end_time}: motion recorded")


    def start_timer(self):
        self.timer = Timer(3, self.stop_recording)
        self.timer_started = True
        self.timer.start()
