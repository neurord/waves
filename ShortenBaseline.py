import numpy as np
from igor import binarywave
import glob

data_dirs=glob.glob('/home/avrama/moose/waves/A2Acredata/*')
endtime=0.8
for datadir in data_dirs:
    fnames=glob.glob(datadir+'/*')
    for f in fnames:
        print('fname',f)
        data=binarywave.load(f)['wave']['wData']
        dt=binarywave.load(f)['wave']['wave_header']['hsA']
        numpts=binarywave.load(f)['wave']['wave_header']['npnts']
        tot_time=dt*numpts
        time = np.linspace(0, tot_time, num=numpts, endpoint=False)
        
