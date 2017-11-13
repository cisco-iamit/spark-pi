import picamera
import time

camera = picamera.PiCamera()


def proc(command, message):
    if command[0] == "photo":
        return take_photo()
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
    file_name = session_id + '.jpg'
    file_path = 'app/tmp/'
    full_path = file_path + file_name
    camera.capture(full_path)
    
    return {
        "data": {
            "status": "ok",
            "text": "Photo has been successfully taken",
            "files": (file_name, open(full_path, 'rb'), 'image/jpeg')
        },
        "response_required": True
    }
