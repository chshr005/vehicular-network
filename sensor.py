import json

import random

class SensorData:
    def gen_sensor_data():
        fuel_data = {'id': 'Sensor_data', 'fuel': random.uniform(0, 100), 
        'x': random.randint(-45, 45),'y':  random.randint(-45, 45), 
        'speed': random.randint(50, 150)}

        data = json.dumps(fuel_data)
        return data
    # print(data)

    data1 = gen_sensor_data()
    # print(data1)