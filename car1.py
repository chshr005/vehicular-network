import socket
import time
from sensor import SensorData
import json

HOST = '10.35.70.12'      #'10.35.70.29' 
PORT = 33001 
PORT2 = 33002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# flag = 0
s.connect((HOST, PORT))



print('Car 1')
while True:
    data = SensorData.gen_sensor_data()
    # print(data)
    json_dict = json.loads(data)
    json_dict['id'] = 'CAR1'
    data = json.dumps(json_dict)
    print(data)
    s.send(data.encode())
    reply = s.recv(1024)
	# print(reply)
    # reply = b'sadas'
    reply1 = reply.decode()
    if reply1 == 'Sensor data not uniform':
        break
    # print(reply1)
    time.sleep(2)