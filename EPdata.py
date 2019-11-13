import os.path
from ajustador.loader import IVCurveSeries

class Params:
    requires = ()
    provides = ('baseline_before', 'baseline_after',
                'steady_after', 'steady_before', 'steady_cutoff',
                'falling_curve_window', 'rectification_window',
                'injection_start', 'injection_end',
                'injection_interval')

    baseline_before = 0.1
    # current injection stops at 0.4, wait a bit for it to return to steady state
    baseline_after = 0.5

    steady_after = .25
    steady_cutoff = 80

    falling_curve_window = 20
    rectification_window = 11

    injection_start = 0.1
    injection_end = 0.4

    injection_interval = injection_end - injection_start
    steady_before = injection_end

dirname = os.path.dirname(__file__) + '/EPmeasurements'
params = Params()

EPwaves120617 = IVCurveSeries(dirname + '/ep120617-11_Waves', params,
                              IV = (-200e-12, 50e-12),
                              IF = (0e-12, 50e-12),
                              time = .6)

EPwaves051517 = IVCurveSeries(dirname + '/ep051517_6_Waves', params,
                              IV = (-200e-12, 50e-12),
                              IF = (0e-12, 50e-12),
                              time = .6)

EPwaves032717 = IVCurveSeries(dirname + '/ep032717_1_Waves', params,
                              IV = (-200e-12, 50e-12),
                              IF = (0e-12, 50e-12),
                              time = .6)

EPwaves032117 = IVCurveSeries(dirname + '/ep032117_2_Waves', params,
                              IV = (-200e-12, 50e-12),
                              IF = (0e-12, 50e-12),
                              time = .6)

waves = {
    '120617':EPwaves120617,
    '051517':EPwaves051517,
    '032717':EPwaves032717,
    '032117':EPwaves032117,
}

