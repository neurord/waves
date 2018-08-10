import ajustador as aju
import numpy as np
from A2Acre import alldata
import matplotlib.pyplot as plt

lr_explist = [];non_explist = []
#A2Acre data is identified D1R and D2R, so 2 separate lists required
#A2Acre is a file with dict. 'alldata' linking filename (key) to datafile (obj)
#A2Acre file is SEPARATE from A2Acre directory with data
#(both in waves directory)

for exp in alldata.keys():
     #change 'LR' for separating data on other characteristics
     if exp.startswith('LR'):
          lr_explist.append(exp)
     else:
          non_explist.append(exp)
        
def data_extract(explist):
     startspikes = [];trace_inj = []
     baseline = [];latency = [];response = []
     spike_height = [];spike_width =[];spike_count = []
     spike_ahp = [];falling_curve = [];rectification = []
     ahp_time = []; ahp_amp = []; mean_isi = []
     for i,exp in enumerate(explist):
          #initialize lists that accumulate one measure per trace
          baselist = [];latencylist = [];responselist = []
          spike_hlist = [];spike_wlist = [];spike_clist= []
          spike_ahplist = [];fc_list = [];rect_list = []; isi_list = []
          ahp_timelist = [];ahp_amplist = [];tracelist = []
          for j,trace in enumerate(alldata[exp].waves):
               tracelist.append(trace.injection)
               baselist.append(np.mean(\
               [aju.features.SteadyState(trace).baseline_pre.x,\
                aju.features.SteadyState(trace).baseline_post.x]))
               responselist.append(aju.features.SteadyState(trace).response.x)
               fc_list.append(aju.features.FallingCurve(trace).falling_curve_tau.x)
               #if statement for (-) current inj only for rectifcation values
               if trace.injection < 0:
                    rect_list.append(aju.features.Rectification(trace).rectification.x)
               else:
                    rect_list.append(np.nan)
               if aju.features.Spikes(trace).spike_height.size:
                    latencylist.append(aju.features.Spikes(trace).spike_latency)
                    spike_hlist.append(np.mean(aju.features.Spikes(trace).spike_height))
                    spike_wlist.append(np.mean(aju.features.Spikes(trace).spike_width))
                    spike_clist.append(aju.features.Spikes(trace).spike_count) 
                    spike_ahplist.append(np.mean(aju.features.AHP(trace).spike_ahp.x))
                    isi_list.append(aju.features.Spikes(trace).mean_isi.x)
                    #This is AHP Time
                    ahp_timelist.append(np.mean(aju.features.AHP(trace).spike_ahp_position.x \
                                        - aju.features.Spikes(trace).spikes.x))
                    #This is AHP Amplitude
                    ahp_amplist.append(np.mean(aju.features.Spikes(trace).spike_threshold \
                                        - aju.features.AHP(trace).spike_ahp.x))
                    if len(startspikes) == i:
                         startspikes.append(j)
          baseline.append(baselist)
          latency.append(latencylist)
          response.append(responselist)
          spike_height.append(spike_hlist)
          spike_width.append(spike_wlist)
          spike_count.append(spike_clist)
          spike_ahp.append(spike_ahplist)
          falling_curve.append(fc_list)
          rectification.append(rect_list)
          ahp_time.append(ahp_timelist)
          ahp_amp.append(ahp_amplist)
          #this replaces any mean.isi value with nan if spike count == 1
          for i, count in enumerate(spike_clist):
               if count == 1:
                    isi_list[i] = np.nan
          mean_isi.append(isi_list)
          trace_inj.append(tracelist)
     return baseline,latency,response,spike_height,spike_width,trace_inj,\
          startspikes, spike_count , spike_ahp, falling_curve, rectification, ahp_time, ahp_amp, mean_isi

baseline_lr,latency_lr,response_lr,spike_height_lr,spike_width_lr,trace_inj_lr,startspikes_lr,spike_count_lr,spike_ahp_lr,falling_curve_lr,rectification_lr,ahp_time_lr,ahp_amp_lr,mean_isi_lr = data_extract(lr_explist)

baseline_non,latency_non,response_non,spike_height_non,spike_width_non,trace_inj_non,startspikes_non,spike_count_non,spike_ahp_non,falling_curve_non,rectification_non,ahp_time_non,ahp_amp_non,mean_isi_non  = data_extract(non_explist)

def stat(desdata,trace_inj,startspikes,label):
#alignment is done here since alternative would have a bunch of nan appends in extract function
     if len(desdata[0]) != len(trace_inj[0]):
          newtemplist = []
          for i, exp in enumerate(desdata):
               templist =  [np.nan for x in range(startspikes[i])] + exp
               newtemplist.append(templist)
          desdata = np.array(newtemplist)
     else:
          desdata = np.array(desdata)
     if label == 'baseline':
          # axis 1 is each value PER experiment i.e. only for baseline at this point
          meanarray = np.nanmean(desdata, axis = 1)
          stdarray = np.nanstd(desdata, axis = 1)
     else:
          # axis 0 is each trace inj across ALL experiments
          meanarray = np.nanmean(desdata, axis = 0)
          stdarray = np.nanstd(desdata, axis = 0)
     cvarray = stdarray/meanarray
     return {'data':desdata, 'mean':meanarray, 'std':stdarray, 'cv':cvarray}

alllabels = ['baseline','latency','response','spike_height','spike_width','spike_count','spike_ahp','falling_curve','rectification','ahp_time','ahp_amplitude','mean_isi']
lrdict = {};nondict = {}
lrdata = [baseline_lr,latency_lr,response_lr,spike_height_lr,spike_width_lr,spike_count_lr,spike_ahp_lr,falling_curve_lr,rectification_lr,ahp_time_lr,ahp_amp_lr,mean_isi_lr]
nondata = [baseline_non,latency_non,response_non,spike_height_non,spike_width_non,spike_count_non,spike_ahp_non,falling_curve_non,rectification_non,ahp_time_non,ahp_amp_non,mean_isi_non]

#this will send warnings: ignore for now (nan-values help align data for plot, stat)
for label,data in zip(alllabels, lrdata):
     lrdict[label] = stat(data, trace_inj_lr, startspikes_lr,label)
for label,data in zip(alllabels, nondata):
     nondict[label] = stat(data, trace_inj_non, startspikes_non,label)

#lrdict.keys()
#nondict.keys()
trace_inj_lr = np.array(trace_inj_lr)
trace_inj_non = np.array(trace_inj_non)

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
     
cv_data_lr = []
cv_data_non = []
def cv_stat(feature,key,cv_data):
     templist = []
     templist.append(key)
     templist.append(np.nanmean(feature['cv']))
     cv_data.append(templist)
     return cv_data

for key in alllabels:
     plot(trace_inj_lr, lrdict[key]['data'], key, lr_explist, lrdict[key]['mean'],'lr')
     plot(trace_inj_non, nondict[key]['data'], key, non_explist, nondict[key]['mean'],'non')
     #these are the desired variances below, one for lr and non data
     cv_data_lr = cv_stat(lrdict[key], key, cv_data_lr)
     cv_data_non = cv_stat(nondict[key], key, cv_data_non)
     
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
     
plt.figure()     
for key in alllabels:
     cv_plot(key,trace_inj_lr,lrdict[key],'lr')
     
plt.figure()     
for key in alllabels:
     cv_plot(key,trace_inj_non, nondict[key],'non')
