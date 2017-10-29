import requests


def spark_url():
    return "https://api.ciscospark.com/v1/"


def get_message(message_id, config):
    """
    This method is used for:
        -retrieving message text, when the webhook is triggered with a message
        -Getting the username of the person who posted the message if a command is recognized
    """
    url = f"https://api.ciscospark.com/v1/messages/"

    s = requests.Session()
    s.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.bearer
    })

    r = s.get(spark_url() + 'messages/' + message_id)

    return r.text