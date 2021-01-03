import socket

HOST = '10.35.70.12' # Server IP or Hostname
PORT = 33001 # Pick an open Port (1000+ recommended), must match the client sport
PORT2 = 33002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

flag = 0
s.connect((HOST, PORT))

#managing error exception
# try:
# 	s.bind((HOST, PORT))
# except socket.error:
# 	print ('Bind failed on port 1'); flag = 1
# if flag == 1:
#     try:
#         s.bind((HOST, PORT2))
#         print('Connected on port 2')
#     except socket.error:
#         print('Bind failed on port 2 \n Exiting'); exit()


s.listen(5)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')

# awaiting for message
while True:
	data = conn.recv(1024)
	print ('I sent a message back in response to: '+ data.decode())
	data1=data.decode()
	reply = ''

	# process your message
	if data1 != ''  or data1!='{}':
		reply = 'Data recieved'
	# elif data1 == 'This is important':
	# 	reply = 'OK, I have done the important thing you have asked me!'

	# #and so on and on until...
	# elif data1 == 'quit':
	# 	conn.send('Terminating')
	# 	break
	else:
		reply = 'Sensor data not uniform'

	# Sending reply
	conn.send(reply.encode())
conn.close() # Close connections