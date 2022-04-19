from time import sleep
from flask import Flask, render_template, Response, request

app = Flask(__name__)


def generate_frames():
    # camera = cv2.VideoCapture(0)
    while True:
        # read the camera frame
        # success, frame = camera.read()
        # if not success:
        #     print("video, frame capturing failed")
        #     break
        # else:
        #     ret, buffer = cv2.imencode('.jpg', frame)
        #     frame = buffer.tobytes()
        with open('result.jpg', "rb") as image:
            f = image.read()
            frame = bytearray(f)
            image.close()
        sleep(2)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def liveStream():
    return render_template('index.html')


@app.route('/frame/upload', methods=['POST'])
def getLiveFrame():
    file = request.files['file']
    # filename = secure_filename(file.filename)
    file.save("result.jpg")
    return Response('data received')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(threaded=True)
