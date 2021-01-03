import socket
import time
from sensor import SensorData

HOST = '10.35.70.12'      #'10.35.70.29' # Enter IP or Hostname of your server
PORT = 33001 # Pick an open Port (1000+ recommended), must match the server port
PORT2 = 33002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((HOST,PORT))
except socket.error:
	print('Connection refused on port 1')
	try:
		s.connect(HOST, PORT2)
	except socket.error:
		print('Connection refused on port 2')
		print('Exiting...')

#Lets loop awaiting for your input
while True:
	data = SensorData.gen_sensor_data()
	print(data)
	# command = input('Enter your command: ')
	s.send(data.encode())
	reply = s.recv(1024)
	# print(reply)
	reply1 = reply.decode()
	if reply1 == 'Sensor data not uniform':
		break
	print(reply1)
	time.sleep(5)