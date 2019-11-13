import numpy as np
import ajustador as aju
from ephys_feature_extract_func import data_lists,data_extract, stat, plot, cv_plot,parse_args
import matplotlib.pyplot as plt
import importlib
import sys 

#usage: python3 ephys_feature_extrat.py -n list of neuron types -w data_repo
#example  python3 ephys_feature_extrat.py -n LR non -w A2Acre

desired_params=['baseline', 'latency', 'response', 'spike_height', 'spike_width','trace_inj','startspikes', 'spike_count', 'spike_ahp', 'falling_curve', 'rectification', 'ap_time', 'ap_amp', 'mean_isi']

##Below is the list of the parameters that you want to be considered for each neuron
commandline=sys.argv[1:]
neuron_types,data_name=parse_args(commandline)
print(neuron_types,data_name)

wavedir=importlib.import_module(data_name)

##this prodces a dictonary with the desired type of neurons
n_list=data_lists(neuron_types)

##Next, all the neuron names in desired list (for this example is the alldata in A2Acre) is sorted into the appropriate neuron types. Here, n_list should provide you with a dictionary that has all your data sorted by the type of neuron that each neuron is.

for exp in wavedir.alldata.keys():
    for nm in neuron_types:
        if exp.startswith(nm):
            n_list[nm].append(exp)

## NOTE: If you do not consistenly name your neurons in alldata, this dictionary will not contain all the necessary data. 

##This creates another dictionary that holds the information from the parameters for  each individual neuron. Dictionary style is {neuron type #1: {param1: [], param2:[]}} It then stores the data for each neuron 

info=data_lists(neuron_types)
for ntype in n_list.keys():
    print(ntype)
    info[ntype] = data_extract(n_list[ntype],wavedir.alldata,desired_params)

##nstats is another dictonary that will hold all the data with the numpy nan spacers, the standard deviation, mean, and coeffcient of variance with each neuron type.
 
nstats=data_lists(neuron_types)
for ntype in nstats:
    nstats[ntype]=data_lists(desired_params)
    for nkey in desired_params:
        ##The following for loops check to ensure that you are not changing the trace injection data or the start spikes data. Then it performs the statistical analysis and assigns it properly
          if nkey != 'trace_inj' and  nkey!= 'startspikes':
                  print('my neuron is:', ntype,'my key is:', nkey )
                  nwstat=stat(info[ntype][nkey],info[ntype]['trace_inj'], info[ntype]['startspikes'], nkey)
                  nstats[ntype][nkey]=nwstat
                  

##This uses the function plot to plot the data for parameters listed in the desired_params. Each graph will contain the parameter vs. trace injection and include each of the specific neuron type. For example, the first graph will produce a graph of baseline vs. trace_inj for all arky neurons. 
for ntype in nstats.keys():
    for nstat in nstats[ntype].keys():
        if nstat != 'trace_inj' and  nstat!= 'startspikes':
            plot(info[ntype]['trace_inj'], nstats[ntype][nstat]['adjdata'], nstat, n_list[ntype], nstats[ntype][nstat]['mean'], ntype)

##This provides 1 graph of all the cv's for all the parameters  vs. trace_inj for each neuron type. You should get the same amount of graphs as neuron types.            
for nkey in nstats.keys():
    plt.figure()
    for nstat in nstats[nkey].keys():
        if nstat != 'trace_inj' and  nstat!= 'startspikes':
            cv_plot(nstat, info[nkey]['trace_inj'],nstats[nkey][nstat],nkey)
CVs={ntype:[] for ntype in nstats.keys()}
for ntype in nstats.keys():
    for nkey in nstats[ntype].keys():
        if nkey != 'trace_inj' and  nkey != 'startspikes':
            print(ntype, nkey, nstats[ntype][nkey]['cv'], np.abs(np.nanmean(nstats[ntype][nkey]['cv'])))
            CVs[ntype].append(1/np.abs(np.nanmean(nstats[ntype][nkey]['cv'])))
    print(ntype,CVs[ntype],np.log(CVs[ntype]))
  
  

 

        
