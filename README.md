# Cisco Spark + Raspberry Pi

Cisco Spark bot to interact with components of Raspberry Pi.

## How It Works

Check out our video on YouTube.

## Prerequisite

### Python

* Install Python 3.6+
* Install Python dependencies: ```pip3 install -r requirements.txt```

### Other Software

* [ngrok](https://ngrok.com/download) to create tunnels to localhost visible on the public internet

### Hardware

We use:

* Raspberry Pi 2b or 3b
* Official Raspberry Pi camera
* Motion sensor ([we use this](https://www.amazon.co.uk/gp/product/B00NFXBPU8/))
* LED Matrix ([we use this](https://www.amazon.co.uk/gp/product/B0714FVF3R/))
* Keypad ([we use this](https://www.amazon.co.uk/gp/product/B00UB32C7U/))

## Run Bot

1. Sign up on [developer.ciscospark.com](https://developer.ciscospark.com) and [create a bot](https://developer.ciscospark.com/add-bot.html).
2. Sign up on [ngrok.com](https://ngrok.com) and follow guidelines to run the tunnel to port 8080.
3. [Create a webhook](https://developer.ciscospark.com/endpoint-webhooks-post.html) for your Spark bot. This will ensure that messages sent to your bot will be forwarded via ngrok to your localhost script. Make sure to enable test mode on and enter your bot information on the webpage.
4. Run ```python3 app/main.py```.
5. You can now use your bot.

## Bot API

Bot responds to the commands stated below. Commands are case insensitive, which means that ```COMMAND```, ```command``` and ```CoManD``` are all the same thing. 

You can add a bot to a Spark space, or start an 1:1 chat - all cases are covered.

### Command Help

* ```help``` - Get help on commands 

### Lights

* ```lights on [color]``` - Turn the LED matrix on with the specific color flashing. Red by default. 

* ```lights off``` - Turn the LED matrix off.

Both commands respond with a confirmation of the operation.

### Camera

* ```camera photo``` - Take a photo with a Raspberry Pi  camera and send it back as an attached image.

* ```camera video [sec]``` - Shoot a video for *sec* seconds and send it back as an attached file.

### Subsription

* ```subscribe security``` - Add your current Spark account to a database to receive security updates. It includes sending you photos taken by camera, when the motion sensor fires up.

* ```unsubscribe security``` - Opt out from the subscription.

## Links

* [Spark for developers](https://developer.ciscospark.com)