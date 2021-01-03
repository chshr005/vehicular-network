import socket
import json
import math
from Dijkstra import Dijkstra
import time

HOST = '10.35.70.12' # Server IP or Hostname
PORT = 33001 # Pick an open Port (1000+ recommended), must match the client sport
PORT2 = 33002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

flag = 0
s.bind((HOST, PORT))
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
    # data = b'{"id": "Sensor_data", "fuel": 7.153023857845497, "x": -24, "y": 0, "speed": 97}'
    print ('Data recieved: '+ data.decode())
    data1=data.decode()
    reply = ''

    # process your message
    if data1 != ''  or data1!='{}':
    	reply = 'Data recieve acknowledged'
    else:
    	reply = 'Sensor data not uniform'

    json_dict = json.loads(data1)
    name = json_dict['id']
    x = json_dict['x']
    y = json_dict['y']
    dist = math.sqrt((x*x)+(y*y))
    if dist>50:
        dist = -1
    x2 = 20
    y2 = 10
    dist2 = math.sqrt((x2*x2)+(y2*y2))
    dist3 = math.sqrt((x2 - x)*(x2 - x) + (y2 - y)*(y2 - y))
    name2 = 'car2'
    graph = {'base':{name:dist, name2:dist2}, name:{'base':dist, name2: dist3}, name2:{'base':dist2, name:dist3}}
    Dijkstra(graph, name,'base')
	# Sending reply
	# conn.send(reply.encode())
conn.close() # Close connections