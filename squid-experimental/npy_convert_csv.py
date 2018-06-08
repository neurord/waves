import numpy as np
import pandas as pd
from collections import OrderedDict

data_file = "squid_vm1.npy"
np_data_obj = np.load(data_file)
time_instances = np.linspace(0,0.9,4501) # fetch from file.
data = {'time(ms)': time_instances, 'i(1nA)':np_data_obj}
data = OrderedDict(data.items(), key= lambda t:t[0])
data_frame = pd.DataFrame(data).drop('key', axis=1)
data_frame.to_csv("squid_experimental.csv", index=False)
