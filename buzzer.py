import threading
from datetime import datetime as dt
import paho.mqtt.subscribe as subscribe
import time
from time import sleep 
import serial 
from console_logging.console import Console
console = Console()
try: 
  arduino = serial.Serial("/dev/ttyUSB0",9600)
except:
  console.error("FALHA AO CONECTAR PORT /dev/ttyUSB0")

global counter
counter = 0    
 
HOST = '192.168.101.1'
PORT = 1883
KEEPALIVE = 60  # in seconds

topic = "/sensor/fadiga/0001/buzzer"
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
     console.log(msg.topic)
     console.log(msg.payload)
    
     dict_str = msg.payload.decode("UTF-8")
    
     data = int(dict_str)
     if data == 1:
         console.info("BUZZER ON")
         arduino.write(b'l')
    
def main(): 
  [console.log("FADIGA - BUZZER [ ONLINE ] ") for p in range(10)]
  
  subscribe.callback(on_message, topic, hostname=HOST, port=PORT, keepalive=KEEPALIVE)

if __name__ == "__main__":
    
    main()    
