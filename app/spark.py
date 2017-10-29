import requests


# Return Spark API base URL
def spark_url():
    return "https://api.ciscospark.com/v1/"


# Get message by ID
def get_message(message_id, config):

    s = requests.Session()
    s.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.bearer
    })

    r = s.get(spark_url() + 'messages/' + message_id)

    return r.text
