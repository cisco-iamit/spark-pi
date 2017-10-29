# Cisco Spark + Raspberry Pi

Cisco Spark bot to interact with elements of Raspberry Pi



## API

* ```help``` - Get help on commands 

### Lights

* ```lights on [color]``` - Turn the LED matrix on with the specific color flashing. Red by default

* ```lights off``` - Turn the LED matrix off

Both commands respond with a confirmation of the operation.

### Camera

* ```camera photo``` - Take a photo from the camera and send it to the Spark room as an attached image.

* ```camera video [sec]``` - Shoot a video for *sec* seconds.

### Subsription

* ```subscribe security``` - Add your current Spark account to a database to receive security updates. It includes sending you photos taken by camera.

* ```unsubscribe security``` - Opt out from the subscription.

## Links

* [Spark for developers](https://developer.ciscospark.com)