import socket

HOST = '10.35.70.12'      #'10.35.70.29' # Enter IP or Hostname of your server
PORT = 33001 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	command = input('Enter your command: ')
	s.send(command.encode())
	reply = s.recv(1024)
	print(reply)
	reply1 = reply.decode()
	if reply1 == 'Terminate':
		break
	print(reply1)