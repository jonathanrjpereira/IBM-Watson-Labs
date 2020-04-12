# MQTT

*All the code and other information is from the [Explore the Internet of Things Platform service](https://developer.ibm.com/tutorials/cl-mqtt-bluemix-iot-node-red-app/) Tutorial*


**Prerequisites**

Install the latest Python for IBM Watson IoT Platform library

 ```
pip install wiotp-sdk
```

## Device
Device-side programming consists of three parts:

-   Connecting to the IoT service (MQTT broker).
-   Publishing events to applications.
-   Subscribing commands from applications.

**Connect to the IoT service**  - device/connect.py
The code here shows the structure of the device-side program. It connects to one of the Watson IoT Platform devices we created in the dashboard. The connection parameters are loaded from a YAML configuration file for the specific device.

**Publish events** - device/publish.py
The main function of an IoT sensor device is to collect and send data to backend applications. The IBM IoT Platform is responsible for broadcasting the event to all applications that listens for device events.

**Subscribe commands** - device/subscribe.py
After connection to the device on IBM IoT Platform, our device is now ready to receive commands from an application registered in the same IBM IoT Platform service. The program below registers a callback function for commands. The device then waits for commands, and processes each received command in the callback function.
