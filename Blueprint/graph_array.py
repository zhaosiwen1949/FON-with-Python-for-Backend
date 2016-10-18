from flask import Blueprint,request,jsonify
from .Helpers.graph_topo_to_array import graph_topo_to_array

graph_array = Blueprint('graph_array',__name__)

@graph_array.route('/graph_array',methods=['POST','GET'])
def generate_graph_array():
    if request.method == 'GET':
        return "该API需要使用POST方法访问"
    if request.method == 'POST':
        obj = request.get_json()
        origin_graph = obj['graph']
        result_graph = graph_topo_to_array(origin_graph)
        return jsonify({'graph':result_graph})
