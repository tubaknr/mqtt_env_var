import paho.mqtt.publish as publish

# MQTT broker information
broker_address = "0.0.0.0"
broker_port = 1883

# Topic to publish the new variable
topic = "/environment/variable"

# Get the new variable from user input
new_variable = input("Enter the new variable (e.g., KEY=VALUE): ")

# Publish the new variable to the topic
publish.single(topic, payload=new_variable, hostname=broker_address, port=broker_port)
