import pymongo

client = pymongo.MongoClient()
db = client.pi

allowed_events = ["security"]


def proc(command, message):
    if len(command) == 2:
        if command[0] == "subscribe":
            return subscribe(command[1], message["roomId"])
        elif command[0] == "unsubscribe":
            return unsubscribe(command[1], message["roomId"])
        else:
            return {
                "data": {
                    "status": "error",
                    "text": "Event command was not recognised."
                },
                "response_required": True
            }
    else:
        return {
            "data": {
                "status": "error",
                "text": "Event command has invalid syntax."
            },
            "response_required": True
        }


def subscribe(event_type, room_id):
    if event_type in allowed_events:
        
        data = {"room_id": room_id}
        getattr(db.subscriptions, event_type).update_one(data, {"$set": data}, upsert=True)
        
        return {
            "data": {
                "status": "ok",
                "text": "You have been subscribed to: " + event_type + "."
            },
            "response_required": True
        }
    else:
        return {
            "data": {
                "status": "error",
                "text": "Subscription to this event is not allowed."
            },
            "response_required": True
        }
    
    
def unsubscribe(event_type, room_id):
    if event_type in allowed_events:
        
        data = {"room_id": room_id}
        getattr(db.subscriptions, event_type).remove(data)
        
        return {
            "data": {
                "status": "ok",
                "text": "You have been unsubscribed from: " + event_type + "."
            },
            "response_required": True
        }
    else:
        return {
            "data": {
                "status": "error",
                "text": "You may not unsubscribe from this event."
            },
            "response_required": True
        }


def get_subscribers(event_type):
    if event_type in allowed_events:
        
        data = []
        
        event_cursor = getattr(db.subscriptions, event_type).find({})
        for document in event_cursor:
            data.append(document)
        
        return data
    else:
        return []
