import json
import random
import socket



def send(data, port):
    host = socket.gethostbyname(socket.gethostname())   
    s = socket.socket()
    s.connect((host, port))
    s.send(data.encode())
    print("Sending data")
    print('Date Sent ', repr(data.encode()))
    s.close()  

class Sensor():
	def __init__(self, header):
		self.header=header
		
class FuelSensor(Sensor):
	def ___init__(self, header):
		Sensor.__init__(self, header)
	
	def sensor_data(self):
		data = {'fuel': random.uniform(0, 100)}
		fuel= json.dumps(data)
		print("Fuel data generated :", fuel)
		return fuel
	def send_data(self):
                try:
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT1)
                except:
                        print("Server not available")
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT2)	
	
	
		

class ProximitySensor(Sensor):
	def __init__(self, header):
		Sensor.__init__(self, header)	
		
	def sensor_data(self):
		data = {'x': random.randint(-45, 45),'y':  random.randint(-45, 45)}
		distance= (data['x']**2 + data['y']**2)**0.5
		proximity = json.dumps(distance)
		print("Location data generated :",proximity)      
		return proximity
	def send_data(self):
                try:
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT1)
                except:
                        print("Server not available")
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT2)
     
		
	
	
class PowerSensor(Sensor):
	def __init__(self, header):
		Sensor.__init__(self, header)	
		
	def sensor_data(self):
		data={'power': random.uniform(0, 100)}
		power=json.dumps(data)
		print("Power data generated:" , power)
		return power
	def send_data(self):
                try:
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT1)
                except:
                        print("Server not available")
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT2)	
		
	
		
class SpeedSensor(Sensor):
	def __init__(self,header):
		Sensor.__init__(self,header)
		
	def sensor_data(self):
		data={'speed': random.randint(0,80)}
		speed=json.dumps(data)
		print("Speed data generated:",speed)
		return speed
	
	def send_data(self):
                try:
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT1)
                except:
                        print("Server not available")
                        self.data = self.sensor_data()
                        # send data
                        send(self.data, PORT2)
