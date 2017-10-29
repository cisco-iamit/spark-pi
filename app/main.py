import spark
from config import config
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


@app.route("/", methods=["post"])
def index():
    # Parse request
    webhook_req = request.get_json()
    spark.get_message(message_id=webhook_req['data']['id'], bearer=config["bearer"])
    return jsonify({})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
