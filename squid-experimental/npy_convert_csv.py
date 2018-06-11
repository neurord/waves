import numpy as np
import pandas as pd
from collections import OrderedDict

def convert_sim_data_to_csv(data_file):
    ''' Created a csv file from the simulated data file generated from adjustador.basic_simulation.py when
        --save-vm argument is set in command line mode.
    '''
    np_data_obj = np.load(data_file).item()
    time_instances = np.linspace(0,np_data_obj['simtime'],np_data_obj['data_points'])
    data = {'time(ms)': time_instances, 'i({}A)'.format(np_data_obj['injection_current']):np_data_obj['voltage_trace']}
    data = OrderedDict(data.items(), key= lambda t:t[0])
    data_frame = pd.DataFrame(data).drop('key', axis=1)
    data_frame.to_csv("squid_experimental.csv", index=False)

convert_sim_data_to_csv(data_file = "squid_vm1.npy")

