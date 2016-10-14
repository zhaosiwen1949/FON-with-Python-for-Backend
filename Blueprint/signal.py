from flask import Blueprint,request,jsonify
from scipy.stats import poisson,expon
from random import randint
from .Helpers.signal_topo import generate_signal_topo

signal = Blueprint('signal',__name__)

@signal.route('/get_signal',methods=['POST','GET'])
def generate_signal():
    opt = request.get_json()['signal_settings']
    lamda = opt['lamda']
    mu = opt['mu']
    compute_resource_top = opt['compute_resource_top']
    compute_resource_buttom = opt['compute_resource_buttom']
    spectrum_resource_top = opt['spectrum_resource_top']
    spectrum_resource_buttom = opt['spectrum_resource_buttom']
    sig_num_top = opt['sig_num_top']
    sig_num_buttom = opt['sig_num_buttom']

    sigs = []
    sig_number = poisson.rvs(lamda)
    for n in range(sig_number):
        duration = round(expon.rvs(0,mu))
        sig_list = []
        sig_graph = []
        sig_list_num = randint(sig_num_buttom,sig_num_top)
        for m in range(sig_list_num):
            sig_list.append(randint(compute_resource_buttom,compute_resource_top))

        #coding=utf-8
        #进行信号源拓扑类型的判断
        sig_graph = generate_signal_topo(sig_list_num,spectrum_resource_buttom,spectrum_resource_top)

        sigs.append({
            'duration':duration,
            'sig_list':sig_list,
            'sig_graph':sig_graph
            })
    return jsonify({'signals':sigs})
