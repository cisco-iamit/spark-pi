import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


# Return Spark API base URL
def spark_url():
    return "https://api.ciscospark.com/v1/"


def clean_message(message):
    
    message = message.lower()
    
    no_mention_msg = ""
    
    mention_start_arr = message.split('<spark-mention ')
    
    for s in mention_start_arr:
        if '</spark-mention>' in s:
            s = s.split('</spark-mention>', maxsplit=1)[1]
        no_mention_msg += s

    no_mention_msg = no_mention_msg.split('<p>', maxsplit=1)[1].split('</p>', maxsplit=1)[0]

    no_mention_msg = no_mention_msg.strip()
    
    return no_mention_msg



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

    if "html" in content:
        content["command"] = clean_message(content["html"])
    else:
        content["command"] = content["text"]
        
    return content


# Send message
def send_message(room_id, payload, bearer):

    s = requests.Session()
    data = {"roomId": room_id}
            
    data.update(payload)

    s.headers.update({
        "Accept": "application/json",
        "Authorization": "Bearer " + bearer
    })

    if "files" in payload:
        
        m = MultipartEncoder(data)
        
        s.headers.update({
            "Content-Type": m.content_type,
        })
        
        r = s.post(spark_url() + "messages", data=m)

    else:
        
        s.headers.update({
            "Content-Type": "application/json"
        })
        
        r = s.post(spark_url() + "messages", json.dumps(data))

    content = json.loads(r.text)

    return content
