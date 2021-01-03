import socket
import time
from sensor import SensorData

HOST = '10.35.70.12'      #'10.35.70.29' # Enter IP or Hostname of your server
PORT = 33001 # Pick an open Port (1000+ recommended), must match the server port
PORT2 = 33002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
flag = 0
try:
	s.connect((HOST,PORT))
	print('Connected on port 1')
except:
	print('Connection failed on port 1'); flag = 1

if flag == 1:
	try:
		s.connect(HOST, PORT2)
		print('Connected on port 2')
	except:
		print('Connection failed on port 2 \n Exiting'); exit()

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