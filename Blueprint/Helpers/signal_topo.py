from random import randint
from .graph_topo_to_array import graph_topo_to_array as gtta
from .connected_graph import connected_graph as c_graph

def spectrum_resource_on_demand (func):
    def signal_topo_with_spectrum (node_num,spectrum_resource_buttom,spectrum_resource_top):
        origin_graph = func(node_num)
        length = len(origin_graph)
        print(origin_graph)
        for i in range(0,length):
            for j in range(0,length):
                if origin_graph[i][j] == 1:
                    origin_graph[i][j] = randint(spectrum_resource_buttom,spectrum_resource_top)
        return origin_graph
    return signal_topo_with_spectrum

@spectrum_resource_on_demand
def generate_signal_topo (node_num):
    result_array = []
    if node_num == 3:
        seed = randint(1,2)
        if seed == 1:
            gtta(c_graph['1_of_3_nodes'],result_array)
        elif seed == 2:
            gtta(c_graph['2_of_3_nodes'],result_array)
    elif node_num == 4:
        seed = randint(1,5)
        if seed == 1:
            gtta(c_graph['1_of_4_nodes'],result_array)
        elif seed == 2:
            gtta(c_graph['2_of_4_nodes'],result_array)
        elif seed == 3:
            gtta(c_graph['3_of_4_nodes'],result_array)
        elif seed == 4:
            gtta(c_graph['4_of_4_nodes'],result_array)
        elif seed == 5:
            gtta(c_graph['5_of_4_nodes'],result_array)
    return result_array
