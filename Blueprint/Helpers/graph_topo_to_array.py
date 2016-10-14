def graph_topo_to_array(origin_array,result_array):
    for list in origin_array:
        list.pop(0)
        row = [0 for n in range(0,len(origin_array))]
        for index in list:
            row[index-1] = 1
        result_array.append(row)
