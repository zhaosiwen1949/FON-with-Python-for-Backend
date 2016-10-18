def graph_topo_to_array(origin_array):
    try:
        length =len(origin_array)
        result_array = list()
        for n in range(0,length):
            row = [0 for m in range(0,length)]
            for k in range(0,len(origin_array[n])):
                if k != 0:
                    index = origin_array[n][k]-1
                    row[index] = 1
            result_array.append(row)
        return result_array
    except:
        if len(origin_array) == 0:
            print('origin_array is empty')
            return [1,1,1,1,1,1,1,1,1,1,1,1]
        return origin_array
