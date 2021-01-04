import json
from Dijkstra import Dijkstra

def call_dijkstra():
    with open('data.txt', 'r') as reader:
        lines = reader.readlines()

    print(lines[len(lines)-1])
    data = lines[len(lines)-1]
    data2 = lines[len(lines)-2]
    data = data.replace('\\','')
    data2 = data2.replace('\\', '')
    json_dict = json.loads(data)
    print(json_dict['Fuel_data'])

    json_dict2 = json.loads(data2)

    flag =0
    name = 'CAR1'#json_dict['id']
    name2 =  'CAR2'#json_dict2['id']
    dist = json_dict['Proximity']
    dist2 = json_dict2['Proximity']
    dist3 = dist2-dist

    if dist > 50:
        dist = -1
        flag =1
    if dist2 > 50:
        dist2 = -1
        if flag == 1:
            flag =12
        else:
            flag = 2
    if dist3 < 0:
        dist3 = dist3*-1




    graph = {'base':{name:dist, name2:dist2}, name:{'base':dist, name2: dist3}, name2:{'base':dist2, name:dist3}}

    if flag ==1:
        car= name
    elif flag ==2:
        car = name2
    elif flag == 12:
        print("All cars out of range")
    else:
        print('All cars in range')

    if flag != 0:
        Dijkstra(graph, car, 'base')
    

call_dijkstra()