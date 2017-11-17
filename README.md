# Cisco Spark + Raspberry Pi

[Cisco Spark](https://www.ciscospark.com) bot to interact with components of [Raspberry Pi](https://www.raspberrypi.org).

Currently, the bot accepts commands to take a photo with a Raspberry Pi camera on a user's demand, as well as subscribe to automatic photo shooting on detected motion.

## Why

This is a simple educational project aimed to provide a clue about architecture of applications based on popular Cisco solution, Spark, and a world favourite mini-computer Raspberry Pi.

It was initially used at Cisco infrastructure team to inspire young students to information technologies. You are welcome to update the code, fork it and submit your ideas, as we're doing a lot of charity and educational projects and would be glad to reuse existing resources.

## Prerequisite

### Hardware

We use:

* Raspberry Pi 2b or 3b
* Official Raspberry Pi camera
* Motion sensor

The motion sensor is connected to the [GPIO port 23](https://pinout.xyz/pinout/pin16_gpio23) in our example, however you are free to choose any other port. Make sure to change ```app/config``` file accordingly.

#### Precautions

Make sure to remove static electricity, when playing with the Pi Camera and motion sensors, as they might be damaged.

Plug the camera in and out when the Pi board is not powered only, as doing otherwise could damage it.

### Software

* Python 3.6+
* Python dependencies
* [ngrok](https://ngrok.com/download) to create tunnels to localhost visible on the public internet.

You can install the dependencies manually or run an automated script to get this job done:

```shell
./setup.sh
```

### External Services

1. Sign up on [developer.ciscospark.com](https://developer.ciscospark.com) and [create a bot](https://developer.ciscospark.com/add-bot.html).
2. Sign up on [ngrok.com](https://ngrok.com) and follow guidelines to run the tunnel to port 8080.
3. [Create a webhook](https://developer.ciscospark.com/endpoint-webhooks-post.html) for your Spark bot. This will ensure that messages sent to your bot will be forwarded via ngrok to your localhost script. Make sure to enable test mode on and enter your bot information on the webpage.

## Run Bot

1. Run ```./ngrok http 8080```
2. Run ```python.63 app/main.py```
3. You can now use your bot.

## Bot API

Bot responds to the commands stated below. Commands are case insensitive, which means that ```COMMAND```, ```command``` and ```CoMmanD``` are all the same thing. 

You can add a bot to a Spark space, or start an 1:1 chat - all cases are covered.

### Command Help

* ```help``` - Get the list of available commands and their description 

### Camera

* ```camera photo``` - Take a photo with a Raspberry Pi  camera and send it back as an attached image.

### Subsription

* ```subscribe security``` - Add your current Spark account to a database to receive security updates. It includes sending you photos taken by camera, when the motion sensor fires up.

* ```unsubscribe security``` - Opt out from the subscription.

## References

* [Spark for developers](https://developer.ciscospark.com)
* [Raspberry Pi Pinout](https://pinout.xyz)

## License

This code and documentation are available under MIT license. See [license](LICENSE) for more details.

