![Banner](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/img/Banner.svg)


*All the code and other information is from the [Explore the Internet of Things Platform service](https://developer.ibm.com/tutorials/cl-mqtt-bluemix-iot-node-red-app/) Tutorial*


**Prerequisites**

Install the latest Python for IBM Watson IoT Platform library

 ```
pip install wiotp-sdk
```

![Fig1](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/img/Fig1.PNG)

## Device
Device-side programming consists of three parts:

-   Connecting to the IoT service (MQTT broker).
-   Publishing events to applications.
-   Subscribing commands from applications.

**Connect to the IoT service**  - [device/connect.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/device/connect.py)

The code here shows the structure of the device-side program. It connects to one of the Watson IoT Platform devices we created in the dashboard. The connection parameters are loaded from a YAML configuration file for the specific device.

**Publish events** - [device/publish.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/device/publish.py)

The main function of an IoT sensor device is to collect and send data to backend applications. The IBM IoT Platform is responsible for broadcasting the event to all applications that listens for device events.

**Subscribe commands** - [device/subscribe.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/device/subscribe.py)

After connection to the device on IBM IoT Platform, our device is now ready to receive commands from an application registered in the same IBM IoT Platform service. The program below registers a callback function for commands. The device then waits for commands, and processes each received command in the callback function.

## Application
As with device-side programming, application-side programming consists of three parts:

-   Connecting to the IoT service (MQTT broker).
-   Subscribing to events from devices or from applications.
-   Publishing commands to devices

**Connect to the IoT service** - [application/connect.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/application/connect.py)

The code here shows the structure of the application-side program. It connects to one of the Watson IoT Platform applications we created in the dashboard. The connection parameters are loaded from a YAML configuration file for the specific application.

 **Subscribe to events** - [application/subscribe.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/application/subscribe.py)

After connection to the application on IBM IoT Platform, our application is now ready to receive events from devices and applications registered in the same IBM IoT Platform service. The program below registers a callback function for events. The application then waits for events in the specified queue, and processes each received event in the callback function.

**Send commands** - [application/command.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/application/commands.py)

To send a reboot command to the device, we use the IBM IoT Platform service to relay the command.

## Combined Programs
In this section, we demonstrate how to run the Python programs to send an event from a device to an application, and to send a command from an application to a device.

**Events**

First, start the application to listen for events for a device queue.
[application/app_event_recd.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/application/app_event_recd.py)

![Fig2](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/img/Fig2.PNG)

The application waits. Next, run the device program to send an event from the device.
[device/dev_event_send.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/device/dev_event_send.py)

![Fig3](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/img/Fig3.PNG)

The application should receive the event and print it in the console

**Commands**

First, start the device program to listen for commands for this device.
[device/dev_cmd_recd.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/device/dev_cmd_recd.py)

![Fig4](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/img/Fig4.PNG)

The device waits. Next, run the application to send a command for the device.
[application/app_cmd_send.py](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/application/app_cmd_send.py)

![Fig5](https://github.com/jonathanrjpereira/IBM-Watson-Labs/blob/master/MQTT/img/Fig5.PNG)

The device should receive the command and print it in the console.

## References
1. [Explore the Internet of Things Platform Service](https://developer.ibm.com/tutorials/cl-mqtt-bluemix-iot-node-red-app/)
2. [MQTT IoT Watson Platform - Michael Yuan](https://github.com/juntao/mqtt-watson-iot-platform-sample/tree/master/python/device)
3. [Banner Logo References](https://www.ibm.com/design/language/iconography/pictograms/library)


## Contributing
Are you a programmer, engineer or hobbyist who has a great idea for a new feature in this project? Maybe you have a good idea for a bug fix? Feel free to grab our code & schematics from Github and tinker with it. Don't forget to smash those ⭐️ & Pull Request buttons. [Contributor List](https://github.com/jonathanrjpereira/IBM-Watson-Labs/graphs/contributors)

Made with ❤️ by [Jonathan Pereira](https://github.com/jonathanrjpereira)
