import numpy as np
import pandas as pd

data_file = "squid_vm1.npy"
np_data_obj = np.load(data_file)
data_frame = pd.DataFrame(np_data_obj)
data_frame.to_csv("squid_experimental.csv")
