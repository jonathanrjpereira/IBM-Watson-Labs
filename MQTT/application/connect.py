import wiotp.sdk.application

options = wiotp.sdk.application.parseConfigFile("app_test1.yaml")
client = wiotp.sdk.application.ApplicationClient(options)
client.connect()
# do things
client.disconnect()
