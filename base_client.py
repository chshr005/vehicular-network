import socket
import time
from sensor import SensorData

HOST = '10.35.70.12'      #'10.35.70.29' # Enter IP or Hostname of your server
PORT = 33001 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	data = SensorData.gen_sensor_data()
	print(data)
	time.sleep(5)
	# command = input('Enter your command: ')
	s.send(data.encode())
	reply = s.recv(1024)
	print(reply)
	reply1 = reply.decode()
	if reply1 == 'Sensor data not uniform':
		break
	print(reply1)