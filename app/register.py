import requests
import json
import config

target_url = ""

post_data = {
    "name": "Spark Pi Bot",
    "targetUrl": target_url,
    "resource": "messages",
    "event": "created"
}

# Create a session
s = requests.Session()

s.headers.update({
    "Content-type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + config["bearer"]
})

r = s.post("https://api.ciscospark.com/v1/webhooks", json.dumps(post_data))

if r.status_code == 200:
    print("OK")
else:
    print(r.text)
