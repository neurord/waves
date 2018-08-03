import numpy as np
import pandas as pd
from pathlib import Path
from collections import OrderedDict
import argparse

def convert_sim_data_to_csv(data_file, output_file, time_units='S', current_units='A', inj_indx=0):
    ''' Created a csv file from the simulated data file generated from adjustador.basic_simulation.py when
        --save-vm argument is set in command line mode.
    '''
    np_data_obj = np.load(data_file).item()
    time_instances = np.linspace(0,np_data_obj['simtime'],np_data_obj['data_points_count'])
    data = {'Time '+time_units: time_instances,
            '{} {}'.format(np_data_obj['injection_current'][inj_indx], current_units): np_data_obj['voltage_data_points']}
    data = OrderedDict(data.items(), key= lambda t:t[0])
    data_frame = pd.DataFrame(data).drop('key', axis=1)
    data_frame.to_csv(output_file, index=False)

def check_input_existance(filename):
    assert Path(filename).is_file() is True, "NO file {}".format(filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts npy file generated by moose_nerp.squid to a csv file')
    parser.add_argument('--data-file', type=str)
    parser.add_argument('--output-file', type=str)
    parser.add_argument('--time-units', type=str, default='S')
    parser.add_argument('--current-units', type=str, default='A')
    parser.add_argument('--inj-index', type=int, default=0)
    args = parser.parse_args()
    check_input_existance(args.data_file)
    convert_sim_data_to_csv(args.data_file, args.output_file,
                            args.time_units, args.current_units,
                            args.inj_index)

#python3 npy_convert_csv.py --data-file=squid_trace_tau.npy --output-file=squid_exp_tau.csv
#python3 npy_convert_csv.py --data-file=squid_trace_tau_z.npy --output-file=squid_exp_tau_z.csv
#python3 npy_convert_csv.py --data-file=squid_trace.npy --output-file=squid_exp.csv
