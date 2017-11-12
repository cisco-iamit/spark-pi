import spark
import motion
from bot import process_command
from config import config
from flask import Flask
from flask import request
from flask import jsonify
from threading import Thread
import time
import sys
app = Flask(__name__)


def on_motion_detected():
    print("motion detected!")


def run_motion_detection():
    print("hello")
    motion.detector_on(on_motion_detected)
   
    
def run_flask_server():
    app.run(host='0.0.0.0', port=8181)


@app.route("/", methods=["post"])
def index():
    # Parse request
    webhook_req = request.get_json()
    message = spark.get_message(message_id=webhook_req['data']['id'], bearer=config["bearer"])

    if message["personEmail"] != config["bot_email"]:
        res = process_command(message["command"])
        if res["response_required"]:
            spark.send_message(message["roomId"], res["data"], config["bearer"])

    return jsonify({})


if __name__ == "__main__":
    motion_thread = Thread(target = run_motion_detection)
    motion_thread.daemon = True
    motion_thread.start()
    app.run(host='0.0.0.0', port=8080)
