import pathlib
import glob
from ajustador.loader import CSVSeries

class Params:
    requires = ()
    provides = ('baseline_before', 'baseline_after',
                'steady_after', 'steady_before', 'steady_cutoff',
                'falling_curve_window', 'rectification_window',
                'injection_start', 'injection_end',
                'injection_interval')

    injection_start = 0.5
    injection_end = 1.0

    injection_interval = injection_end - injection_start

    baseline_before = 0.5
    baseline_after = injection_end + .15 # Going back to stability requires a bit of time
                                        # Also skip the initial spike which is different.

    #measure the steady state response to current injection after this time (relative to time 0)
    steady_after = injection_start+0.2
     #exclude values exceeding steady_cutoff percentile in the calculation of steady state response
    #this excludes the spikes and allows better estimate of response when spikes generated
    steady_cutoff = 80#units: percentile
    steady_before = injection_end

    #number of points / time samples to use to measure the shape of falling curve
    falling_curve_window = 20
    rectification_window = 11

dirname = pathlib.Path(__file__).parent / 'iSPN_IV'
csvs = sorted(glob.glob('{}/*.csv'.format(dirname)))

params = Params()
data = [CSVSeries(name, params) for name in csvs]
alldata = {series.name:series for series in data}
