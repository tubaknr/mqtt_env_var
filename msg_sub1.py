#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import quotes

# MQTT broker information
broker_address = "0.0.0.0" #get_broker_add.py ile öğrenildi. String.
broker_port = 1883

# Topic to subscribe for new variables
topic = "/environment/variable"

# Path to the /etc/environment file
environment_file_path = "/etc/environment"

def get_until_equalls(var_whole_name):
    splitter="=" #eşitirin önünde arkasında boşluksuz girildiyse
    var_name = var_whole_name.partition(splitter)[0]
    var_value = (var_whole_name.partition(splitter)[2])
    return [var_name, var_value]


# Callback function to handle received messages
def on_message(client, userdata, msg):
    new_variable = msg.payload.decode("utf-8")

    var_name = get_until_equalls(new_variable)[0]
    var_value = quotes.add_quotes(get_until_equalls(new_variable)[1])

    print("var name:",var_name)
    print("var value1:",var_value)

    old_var = False

    with open(environment_file_path, "r") as f:   
        lines = f.readlines()
        line_num = None 

        print("var value2:",var_value)


        for line in lines:
            if var_name in line: #eski değişkense
                old_var = True
                print("eski değişken")
                print("var value3:",var_value)


        if old_var:
            for index, line in enumerate(lines, start=1):
                if var_name in line:
                    line_num = index
                    print(index)
            
            print("var value4:",var_value)                       
            lines[line_num-1] = "export " + var_name + "=" + (var_value) + "\n"
            print(lines)

            with open(environment_file_path, "w") as f:
                f.writelines(lines)

                print("The value of the variable has changed.")


         #if this is completely a new variable, add it to the end of file:
         
        else:
            print("var value5:",var_value) 
            print("THİS is a new variable")
            with open(environment_file_path, "a") as f: #append
                f.write("export " + var_name + "=" + (var_value) + "\n")
                print("New variable added to /etc/environment.")


# Connect to the MQTT broker
client = mqtt.Client()
client.on_message = on_message
client.connect(broker_address, broker_port)

# Subscribe to the topic for new variables
client.subscribe(topic)

# Start the MQTT client loop to listen for incoming messages
client.loop_forever()
