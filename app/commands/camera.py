import picamera
import time


camera = picamera.PiCamera()


def proc(command):
    return {
        "data": {
            "text": "Work in progress."
        },
        "response_required": True
    }


def take_photo():
    session_id = ""
    camera.capture('../tmp/photo-' + session_id + '.jpg')


def shoot_video(video_length):
    camera.start_recording('video.h264')
    time.sleep(video_length)
    camera.stop_recording()
