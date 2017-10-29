import requests
import json


# Return Spark API base URL
def spark_url():
    return "https://api.ciscospark.com/v1/"


# Get message by ID
def get_message(message_id, bearer):

    s = requests.Session()
    s.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + bearer
    })

    r = s.get(spark_url() + 'messages/' + message_id)

    content = json.loads(r.text)

    return content


# Send message
def send_message(room_id, message, bearer):
    pass
