import math

def Dijkstra(graph,source,target):
    
    
    unvisited_nodes=graph
    shortest_distance={}
    route=[] 
    predecessor={}
    
    for nodes in unvisited_nodes:
        
        shortest_distance[nodes]=math.inf
        
    shortest_distance[source]=0
    
    while(unvisited_nodes):
        
        min_Node=None
        
        for current_node in unvisited_nodes: 
            
            if min_Node is None:
            
                min_Node=current_node
                
                

                min_Node=current_node

        for child_node,value in unvisited_nodes[min_Node].items():

            if value > 0:

                if value + shortest_distance[min_Node] < shortest_distance[child_node]:  
                    
                    shortest_distance[child_node] = value + shortest_distance[min_Node]
                    
                    predecessor[child_node] = min_Node
        
        unvisited_nodes.pop(min_Node)
        
    node = target
    
    while node != source:
        
        try:
            route.insert(0,node)
            node = predecessor[node]
        except Exception:
            print('Path not reachable')
            break
    route.insert(0,source)
    
    if shortest_distance[target] != math.inf:
        print('Shortest distance is ' + str(shortest_distance[target]))
        print('And the path is ' + str(route))

# graph = {'base_station':{'car1':5,'car2':2},'car1':{'base_station':5,'car2':4}, 'car2':{'base_station':-1, 'car1':4}}
# # Calling the function with source as 'a' and target as 'e'.
# Dijkstra(graph,'car1','base_station')