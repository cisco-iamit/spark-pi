import spark
from config import config
import json
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

print(config["bearer"])


@app.route("/", methods=["post"])
def index():
    # Parse request
    print(request.get_json(force=True))



    return jsonify({})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
