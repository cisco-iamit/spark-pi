import picamera
import time


camera = picamera.PiCamera()


def proc(command):
    if command[0] == "photo":
        return take_photo()
    elif command[0] == "video":
        return shoot_video()
    else:
        return {
            "data": {
                "status": "error",
                "text": "Camera command was not recognised."
            },
            "response_required": True
        }


def take_photo():
    session_id = str(time.time())
    file_name = 'app/tmp/' + session_id + '.jpg'
    camera.capture(file_name)
    return {
        "data": {
            "status": "ok",
            "text": "Photo has been successfully taken",
            "files": [file_name]
        },
        "response_required": True
    }


def shoot_video(video_length):
    session_id = str(time.time())
    file_name_h264 = 'app/tmp/' + session_id + '.h264'
    file_name_mp4 = 'app/tmp/' + session_id + '.mp4'
    camera.start_recording(file_name_h264)
    camera.wait_recording(video_length)
    camera.stop_recording()
    # sudo apt-get install gpac
    # MP4Box -add filename.h264 filename.mp4
