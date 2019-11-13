##This file is contains the four functions necessary to run ephys_feature_extract
import numpy as np
import ajustador as aju
import argparse
import matplotlib.pyplot as plt
#function that creates specified amounts of lists
def data_lists(array):
    dictofneur={}
    for x in array:
        dictofneur[x]=[]
    return dictofneur

#function to read commandline arguments
def parse_args(commandline):
    parser=argparse.ArgumentParser()
    parser.add_argument("--neurontypes", "-n", nargs='+', help="enter list of neuron tyoes in your data")
    parser.add_argument("--waves","-w", type=str,help="enter name of python file describing the data")
    
    args=parser.parse_args()
    neuron_types=args.neurontypes
    wavedir=args.waves
    return neuron_types,wavedir
    
##This function takes the list of neuron names, the list of neuron information that you have saved in another file, and the list of parameters to place all the data in one dictionary

def data_extract(explist,ndata,desired_params):
    info=data_lists(desired_params)
    
    for i,dkey in enumerate(explist):
        print('in data_extract, processing', dkey)
        traces_without_spikes=[]
        for p in desired_params:
            info[p].append([])
        for j, trace in enumerate(ndata[dkey].waves):
            info['trace_inj'][-1].append(trace.injection)
            info['baseline'][-1].append(np.mean(\
               [aju.features.SteadyState(trace).baseline_pre.x,\
                aju.features.SteadyState(trace).baseline_post.x]))
            info['response'][-1].append(aju.features.SteadyState(trace).response.x)
            info['falling_curve'][-1].append(aju.features.FallingCurve(trace).falling_curve_tau.x)
            #if statement for (-) current inj only for rectifcation values
            if trace.injection < 0:
                   info['rectification'][-1].append(aju.features.Rectification(trace).rectification.x)
            else:
                   info['rectification'][-1].append(np.nan)
            if aju.features.Spikes(trace).spike_height.size:
                info['latency'][-1].append(aju.features.Spikes(trace).spike_latency)
                info['spike_height'][-1].append(np.mean(aju.features.Spikes(trace).spike_height))
                info['spike_width'][-1].append(np.mean(aju.features.Spikes(trace).spike_width))
                info['spike_count'][-1].append(aju.features.Spikes(trace).spike_count) 
                info['spike_ahp'][-1].append(np.mean(aju.features.AHP(trace).spike_ahp.x))
                info['mean_isi'][-1].append(aju.features.Spikes(trace).mean_isi.x)
                    #This is AHP Time
                info['ap_time'][-1].append(np.mean(aju.features.AHP(trace).spike_ahp_position.x \
                                        - aju.features.Spikes(trace).spikes.x))
                    #This is AHP Amplitude
                info['ap_amp'][-1].append(np.mean(aju.features.Spikes(trace).spike_threshold \
                                        - aju.features.AHP(trace).spike_ahp.x))
            else:
                traces_without_spikes.append(j)
        info['startspikes'][-1]=traces_without_spikes
        #this replaces any mean.isi value with nan if spike count == 1
        for i,count in enumerate(info['spike_count']):
            if count == 1:
                info['mean_isi'][-1]= np.nan
    return info

##This function aligns the data in case there is an uneven number of entries in each parameter. It then finds the mean, standard deviation, and the coefficient of variation for the data for every neuron. It returns it as a dictionary

def stat(desdata,trace_inj,non_spike_traces,label):
#begins by testing the length to see if the data has the same amount of entries as trace injection. Otherwise, it appends a nan so that the plotting and statistics are able to run 
    if len(desdata[0]) != len(trace_inj[0]): #need to test this for all lists in desdata
         newtemplist = []
         for i, exp in enumerate(desdata):
             templist =  [np.nan for x in non_spike_traces[i]] + exp
             newtemplist.append(templist)
         desdata = np.array(newtemplist)
         print(desdata)
    else:
          desdata = np.array(desdata)
          print(desdata)
## After all data has nan's in, mean, standard deviation, and coeffiecent of variance for each parameter is calculated. 
    if label == 'baseline':
          # axis 1 is each value PER experiment i.e. only for baseline at this point
          meanarray = np.nanmean(desdata, axis = 1)
          stdarray = np.nanstd(desdata, axis = 1)
    else:
          # axis 0 is each trace inj across ALL experiments
          meanarray = np.nanmean(desdata, axis = 0)
          stdarray = np.nanstd(desdata, axis = 0)
    cvarray = stdarray/meanarray
    return {'adjdata':desdata, 'mean':meanarray, 'stddev':stdarray, 'cv':cvarray}

 ## This function takes each parameter (outside of startspikes) and plots it against the trace_injection. It will put every neuron from one neuron type on one plot. For example, all the 'arky' neurons' baseline information will be plotted on one figure. 
def plot(trace_inj, desdata, title, expnames, stat, ext):
     plt.figure()
     plt.title(title + ' ' + ext)
     for i,exp in enumerate(trace_inj):
          plt.plot(trace_inj[i] ,desdata[i], 'o', label = expnames[i])
     plt.xlabel('inject (nA)')
     plt.ylabel('Vm (V)')
     plt.legend(fontsize = 'small', loc = 'best')
     if title == 'spike_count':
          plt.ylabel('count')
     if title == 'baseline': #plots mean data for baseline at 0 (not vdep feature)
          for i, exp in enumerate(trace_inj):
               plt.plot(0, stat[i], 'kx')
     else:  #everything else (for now) is assumed voltage dependent
          plt.plot(trace_inj[0], stat, 'k')

##This function plots the coefficent of variance for the different parameters on one graph for each type of neuron. For example, all the arky neurons' latency, mean isi, and spike width cv's will be plotted on one graph. the number of cv plots should be equal to the number of neuron types that you have. 
def cv_plot(key,trace_inj,feature,title):
     plt.title('cv-data values' + ' ' + title)
     if key == 'baseline': #for baseline only cv-values PER exp, NOT across all exp
          base_list = []
          for i in range(len(trace_inj)):
               base_list.append(0)
          plt.plot(base_list, feature['cv'], 'kx', label = key)
     else: #since rest is voltage dependent, each mean per voltage ACROSS all exp
          plt.plot(trace_inj[0], feature['cv'], 'o', label = key)
     plt.xlabel('inject (nA)')
     plt.ylabel('cv')
     plt.legend(fontsize = 'small', loc = 'best') 


        
    
            
    
    
    
    
