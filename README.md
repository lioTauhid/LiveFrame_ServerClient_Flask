# Remote Server-Client Live Frame/Stream with Flask


## Description

This is an implementation of low level, low quality live stream example that happens from client to server send live frame then to user. Server side flask app uses Flask web to receive and save frame to image, Client side app uses OpenCV to get camera feed and requests is to send frame to server continuously.

The streaming process can be summed into the following steps:
1. Capturing image frame from camera
2. For each frame bytes, upload it by server api
3. Server receive frame and save into image file
4. Server encode image to bytes then transmit to web form
5. Serve the result in the web page


## Install
This project runs with Python. Also install all dependencies listed to requirements.py by following command :
* pip install -

## Usage
1. Start the server.py and go to "http://&lt;address&gt;:&lt;port&gt;/"
2. Start the client.py
3. See the result in the browser

