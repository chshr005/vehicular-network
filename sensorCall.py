import time
from sensor import SensorData

while(True):
    try:
        data = SensorData.gen_sensor_data()
        print(data)
        time.sleep(5)
    except:
        print("Intrupted")
        exit()
        
    