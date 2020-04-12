import wiotp.sdk.application

# options = wiotp.sdk.application.parseConfigFile("app_test2.yaml")
options = wiotp.sdk.application.parseConfigFile("app_test1.yaml")
client = wiotp.sdk.application.ApplicationClient(options)


client.connect()
myData={'rebootDelay' : 50}
client.publishCommand("test", "4321", "reboot", "json", myData)
client.disconnect()
