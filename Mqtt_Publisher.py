from time import sleep
import paho.mqtt.client as paho
import random


count=0
client=paho.Client()
# client.on_connect=on_connect
var=client.connect("broker.hivemq.com",1883)
client.loop_start()


if(var==0):
     print("connected")
     while True:
        Data1 ="Data1"+"."+str(random.randint(2,100))+"."+str(random.randint(10,50))+"."+str(random.randint(10,80))
        Data2 = "Data2"+"."+str(random.randint(0,1))+"."+str(random.randint(0,440))+"."+str(random.randint(0,50))+"."+str(random.randint(0,20))
        Data3 ="Data3"+"."+ str(random.randint(0,1))+"."+str(random.randint(0,1))+"."+str(random.randint(0,1))
        (rc, mid) = client.publish("E-well",str( "/"+Data1+"/"+Data2+"/"+Data3), qos=1)
        sleep(1)

        
       
        
if(var>0):
    print("not connected")

   

   

    


    
