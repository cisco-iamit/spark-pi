def proc(command, message):
    return {
        "data": {
            "status": "ok",
            "html": """
                <p>
                Hi! I can control your Raspberry Pi. Send me the commands <b>in bold</b> to make me do stuff.<br><br>
                
                &#128247; camera controls<br>
                <b>camera photo</b>: I will take a photo and send it back<br>
                
                &#9881; subscription to events<br>
                <b>event subscribe security</b>: if I detect motion, I'll send you a photo<br>
                <b>event unsubscribe security</b>: I will stop sending photos<br>
                
                </p>
                """
        },
        "response_required": True
    }
