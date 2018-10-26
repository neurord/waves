import os.path
from ajustador.loader import IVCurveSeries

class Params:
    requires = ()
    provides = ('baseline_before', 'baseline_after',
                'steady_after', 'steady_before', 'steady_cutoff',
                'falling_curve_window', 'rectification_window',
                'injection_start', 'injection_end',
                'injection_interval')

    baseline_before = 0.2
    # current injection stops at 0.6, wait a bit for it to return to steady state
    #i.e., begin measurement of baseline response after current injection at this time
    baseline_after = 0.75

    #measure the steady state response to current injection after this time (relative to time 0)
    steady_after = .4
    #exclude values exceeding steady_cutoff percentile in the calculation of steady state response
    #this excludes the spikes and allows better estimate of response when spikes generated
    steady_cutoff = 80 #units: percentile

    #number of points / time samples to use to measure the shape of falling curve
    falling_curve_window = 20
    rectification_window = 11

    injection_start = 0.2
    injection_end = 0.6
    
    #injection_interval is synonomous with injection_width.  This is duration of current injection
    injection_interval = injection_end - injection_start
    steady_before = injection_end

dirname = os.path.dirname(__file__) + '/A2Acredata'

params = Params()

#data collected from striatal spiny projection neurons of mouse from D2-Cre crossed with Ai32.  
#A2A2-Cre expressing mice have ChR2 expressed in the D2 (indirect pathway) SPNs
#Thus, light responseive (LR) neurons are D2, and non-light responsive neurons (non) are D1 containing

non05Jan2015_SLH004 = IVCurveSeries(dirname + '/05Jan2015_SLH004_non_Waves', params,
                            IV = (-450e-12, 50e-12, 3),
                            IF = (40e-12, 20e-12, 4),
                            time = .9)
# p26 Male

non05Jan2015_SLH005 = IVCurveSeries(dirname + '/05Jan2015_SLH005_non_Waves', params,
                            IV = (-450e-12, 50e-12,4),
                            IF = (40e-12, 20e-12,5),
                            time = .9)
# p26 Male

LR06Jan2015_SLH004 = IVCurveSeries(dirname + '/06Jan2015_SLH004_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p27 Male

non08Jan2015_SLH001 = IVCurveSeries(dirname + '/08Jan2015_SLH001_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p29 Female

non08Jan2015_SLH003 = IVCurveSeries(dirname + '/08Jan2015_SLH003_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p29 Female

LR08Mar2015_SLH003 = IVCurveSeries(dirname + '/08Mar2015_SLH003_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p30 Male

LR08Mar2015_SLH004 = IVCurveSeries(dirname + '/08Mar2015_SLH004_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p30 Male

non08Mar2015_SLH005 = IVCurveSeries(dirname + '/08Mar2015_SLH005_non_Waves', params,
                            IV = (-450e-12, 50e-12, 5),
                            IF = (40e-12, 20e-12, 6),
                            time = .9)

# p30 Male

non09Jan2015_SLH004 = IVCurveSeries(dirname + '/09Jan2015_SLH004_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p29 Male

non09Jan2015_SLH006 = IVCurveSeries(dirname + '/09Jan2015_SLH006_non_Waves', params,
                            IV = (-450e-12, 50e-12, 5),
                            IF = (40e-12, 20e-12, 6),
                            time = .9)

# p29 Male

non09Mar2015_SLH001 = IVCurveSeries(dirname + '/09Mar2015_SLH001_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

LR09Mar2015_SLH003 = IVCurveSeries(dirname + '/09Mar2015_SLH003_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

non09Mar2015_SLH005 = IVCurveSeries(dirname + '/09Mar2015_SLH005_non_Waves', params,
                            IV = (-450e-12, 50e-12, 5),
                            IF = (40e-12, 20e-12, 6),
                            time = .9)

# p31 Male

LR09Mar2015_SLH006 = IVCurveSeries(dirname + '/09Mar2015_SLH006_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

non11Jan2015_SLH003 = IVCurveSeries(dirname + '/11Jan2015_SLH003_non_Waves', params,
                            IV = (-450e-12, 50e-12, 5),
                            IF = (40e-12, 20e-12, 6),
                            time = .9)

# p31 Male

non11Jan2015_SLH004 = IVCurveSeries(dirname + '/11Jan2015_SLH004_non_Waves', params,
                            IV = (-450e-12, 50e-12, 6),
                            IF = (40e-12, 20e-12, 7),
                            time = .9)

# p31 Male

LR12Jan2015_SLH001 = IVCurveSeries(dirname + '/12Jan2015_SLH001_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

non12Jan2015_SLH002 = IVCurveSeries(dirname + '/12Jan2015_SLH002_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

LR13Mar2015_SLH001 = IVCurveSeries(dirname + '/13Mar2015_SLH001_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Female

non13Mar2015_SLH003 = IVCurveSeries(dirname + '/13Mar2015_SLH003_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Female

non13Mar2015_SLH005 = IVCurveSeries(dirname + '/13Mar2015_SLH005_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Female

LR14Jan2015_SLH001 = IVCurveSeries(dirname + '/14Jan2015_SLH001_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

LR14Jan2015_SLH002 = IVCurveSeries(dirname + '/14Jan2015_SLH002_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

non14Jan2015_SLH005 = IVCurveSeries(dirname + '/14Jan2015_SLH005_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p31 Male

non14Mar2015_SLH002 = IVCurveSeries(dirname + '/14Mar2015_SLH002_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p32 Male

non14Mar2015_SLH003 = IVCurveSeries(dirname + '/14Mar2015_SLH003_non_Waves', params,
                            IV = (-450e-12, 50e-12, 5),
                            IF = (40e-12, 20e-12, 6),
                            time = .9)

# p32 Male

non18Jan2015_SLH001 = IVCurveSeries(dirname + '/18Jan2015_SLH001_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p26 Female

non18Jan2015_SLH005 = IVCurveSeries(dirname + '/18Jan2015_SLH005_non_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p26 Female

LR19Jan2015_SLH004 = IVCurveSeries(dirname + '/19Jan2015_SLH004_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p27 Female

LR19Jan2015_SLH005 = IVCurveSeries(dirname + '/19Jan2015_SLH005_LR_Waves', params,
                            IV = (-450e-12, 50e-12, 4),
                            IF = (40e-12, 20e-12, 5),
                            time = .9)

# p27 Female

alldata = {'non05Jan2015_SLH004':non05Jan2015_SLH004,
           'non05Jan2015_SLH005':non05Jan2015_SLH005,
           'LR06Jan2015_SLH004':LR06Jan2015_SLH004,
           'non08Jan2015_SLH001':non08Jan2015_SLH001,
           'non08Jan2015_SLH003':non08Jan2015_SLH003,
           'LR08Mar2015_SLH003':LR08Mar2015_SLH003,
           'LR08Mar2015_SLH004':LR08Mar2015_SLH004,
           'non08Mar2015_SLH005':non08Mar2015_SLH005,
           'non09Jan2015_SLH004':non09Jan2015_SLH004,
           'non09Jan2015_SLH006':non09Jan2015_SLH006,
           'non09Mar2015_SLH001':non09Mar2015_SLH001,
           'LR09Mar2015_SLH003':LR09Mar2015_SLH003,
           'non09Mar2015_SLH005':non09Mar2015_SLH005,
           'LR09Mar2015_SLH006':LR09Mar2015_SLH006,
           'non11Jan2015_SLH003':non11Jan2015_SLH003,
           'non11Jan2015_SLH004':non11Jan2015_SLH004,
           'LR12Jan2015_SLH001':LR12Jan2015_SLH001,
           'non12Jan2015_SLH002':non12Jan2015_SLH002,
           'LR13Mar2015_SLH001':LR13Mar2015_SLH001,
           'non13Mar2015_SLH003':non13Mar2015_SLH003,
           'non13Mar2015_SLH005':non13Mar2015_SLH005,
           'LR14Jan2015_SLH001':LR14Jan2015_SLH001,
           'LR14Jan2015_SLH002':LR14Jan2015_SLH002,
           'non14Jan2015_SLH005':non14Jan2015_SLH005,
           'non14Mar2015_SLH002':non14Mar2015_SLH002,
           'non14Mar2015_SLH003':non14Mar2015_SLH003,
           'non18Jan2015_SLH001':non18Jan2015_SLH001,
           'non18Jan2015_SLH005':non18Jan2015_SLH005,
           'LR19Jan2015_SLH004':LR19Jan2015_SLH004,
           'LR19Jan2015_SLH005':LR19Jan2015_SLH005
}
