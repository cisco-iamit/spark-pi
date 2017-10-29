# Cisco Spark + Raspberry Pi

Cisco Spark bot to interact with elements of Raspberry Pi

## API

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