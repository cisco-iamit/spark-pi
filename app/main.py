import spark
import bot
from bot import process_command
from config import config
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

#print(bot.process_command("camera photo"))


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
    app.run(host='0.0.0.0', port=8080)
