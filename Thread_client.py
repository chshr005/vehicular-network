import Sensors
import socket
import json
import time

fuel=Sensors.FuelSensor('Fuel')
power=Sensors.PowerSensor('Power')
speed=Sensors.SpeedSensor('Speed')
proximity=Sensors.ProximitySensor('Proximity')


def sensors():
        data ={'Fuel_data':fuel.sensor_data(),'Power_data':power.sensor_data(),'Speed_data':speed.sensor_data() , 'Proximity':proximity.sensor_data()}
        data=json.dumps(data)
        return data
        


ClientSocket = socket.socket()
host = '10.35.70.12'
port = 33004

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input =sensors()
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    time.sleep(5)

ClientSocket.close()
