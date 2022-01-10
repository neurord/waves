#create_waves.py
#read in csv file with time, Vm, current columns, and rehape to 1 column per current injection
'''From Eric Prager
"voltage is scaled at 10x and current at 200x.
For the injection protocol, starting at 500 ms, we had 25pA current steps for  500 ms, starting at -200pA. If i remember correctly, we had 18 steps total. "
'''
#Usage
#ARGS='/home/avrama/moose/waves/iSPN_IV/iSPN_Matrix/VR-06072018-0723-007  -plot True
#exec(open('create_waves.py').read())
#or
# python3 -i ../create_waves.py iSPN_Matrix/VR-06072018-0723-007/ -plot True

import numpy as np
import sys
from matplotlib import pyplot as plt
import glob
import os
import scipy.signal

def plot_vm_array(vm_array,time,labels):
    from matplotlib import pyplot as plt
    plt.figure()
    if np.shape(vm_array)==2:
        for col in range(np.shape(vm_array)[1]):
            plt.plot(time,vm_array[:,col],label=labels[col])
    else:
        plt.plot(time,vm_array)
    plt.legend()
    plt.xlabel('Time (msec)')
    plt.ylabel('Vm (mV)')
    plt.show()

def parse_args(commandline):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filedir', type=str, help = 'path/to/dir/with/data')
    parser.add_argument('-Vm_scale',type=float,help='scale factor for Vm data',default=0.1)
    parser.add_argument('-I_scale',type=float,help='scale factor for Vm data',default=0.005)
    parser.add_argument('-Istart',type=float,help='starting current injection',default=-200)
    parser.add_argument('-Iinc',type=float,help='current injection increment',default=25)
    parser.add_argument('-plot',type=bool,help='plot data or not',default=False)
    parser.add_argument('-output_dt',type=bool,help='dt for output file',default=0.1)
    args=parser.parse_args(commandline)
    return args

def reshape_data(filename,args):
    data=np.loadtxt(filename,skiprows=1,delimiter=',',usecols = (0,1,2))
    dt=data[1,0]-data[0,0]
    downsamp=int(args.output_dt/dt)
    downsamp_data=data[::downsamp]
    vm= downsamp_data[:,1]/args.Vm_scale
    t= downsamp_data[:,0]
        
    ######## find duration of single current injection
    curr=downsamp_data[:,2]
    change_inject=scipy.signal.find_peaks(np.abs(np.diff(curr)),threshold=0.01,distance=10)[0]
    #0.01 is larger than minor fluctations in inject
    delay=change_inject[0]
    width=change_inject[1]-delay
    interval=change_inject[2]-change_inject[1]
    epoch=delay+width+(interval-delay)
    #reshape vm into one column per current injection
    num_curr=int(len(vm)/epoch)
    vm_array=np.reshape(vm[0:num_curr*epoch],(epoch,-1),order='F')
    newt=t[0:len(vm_array)]
    #determine value of current injection from recording
    inject_start=[1+delay+(width+interval)*i for i in range(num_curr)]
    curr_vals=curr[inject_start]/args.I_scale
    offset=curr_vals[np.argmin(np.abs(curr_vals))]
    output_curr_vals=curr_vals-offset
    #determine number of inject epochs, then calculate current injection from formula
    num_curr=np.argmax(output_curr_vals)+1
    print('from trace',[round(cv) for cv in output_curr_vals])
    curr_vals=[args.Istart+args.Iinc*x for x in range(num_curr)]
    print('from Istart,Iinc',[round(cv) for cv in curr_vals])
    ### optionally plot data
    if args.plot:
        plot_vm_array(vm,t,['all'])
        plot_vm_array(vm_array[:,0:num_curr],newt,curr_vals)
    #write csv file
    path_parts=os.path.dirname(filename).split('/')
    fname=path_parts[-2]+'_'+path_parts[-1]+'.csv'
    output=np.column_stack((newt,vm_array[:,0:num_curr]))
    header='Time (ms),'+' pA,'.join([str(round(cv)) for cv in curr_vals])+' pA'
    np.savetxt(fname,output,delimiter=',',header=header,comments='',fmt='%.3f')
    
if __name__ == '__main__':
    try:
        raw_args = ARGS.split(" ")
        do_exit = False
    except NameError: #NameError refers to an undefined variable (in this case ARGS)
        raw_args = sys.argv[1:]
        do_exit = True
    args=parse_args(raw_args)
    print ("args =", raw_args,args)
    
    #
    filename=glob.glob(args.filedir+'/*.csv')
    if len(filename)==1:
        reshape_data(filename[0],args)
    elif len(filename)==0:
        root,dirs,files=list(os.walk(args.filedir))[0]
        for d in dirs:
            filename=glob.glob(root+d+'/*.csv')
            reshape_data(filename[0],args)
    else:
        print('wrong number of files found',filename)
