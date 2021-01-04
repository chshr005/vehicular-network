import socket
import os
from _thread import *
import json

ServerSocket = socket.socket()
host = '10.35.70.12'
port = 33004
CarNumber = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def multi_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        data1 = data.decode('utf-8')
        jsonData = json.loads(data1)
        with open('data.txt', 'w') as outfile:
            json.dump(jsonData, outfile)
        print(reply)
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_client, (Client, ))
    CarNumber += 1
    print(' Data Collected from CarNumber: ' + str(CarNumber))
ServerSocket.close()
