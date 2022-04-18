from time import sleep

import cv2
import requests


def sendLiveFrame():
    camera = cv2.VideoCapture(0)
    url = "http://127.0.0.1:5000/frame/upload"
    while True:
        # read the camera frame
        success, frame = camera.read()
        if not success:
            print("video, frame capturing failed")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        print(requests.post(url, files={"file": frame}).text)
        sleep(1)


if __name__ == "__main__":
    sendLiveFrame()
