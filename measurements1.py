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
    baseline_after = 0.75

    steady_after = .25
    steady_cutoff = 80

    falling_curve_window = 20
    rectification_window = 11

    injection_start = 0.2
    injection_end = 0.6

    injection_interval = injection_end - injection_start
    steady_before = injection_end

dirname = os.path.dirname(__file__) + '/measurements1'
params = Params()

waves042811 = IVCurveSeries(dirname + '/042811-6ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (200e-12, 20e-12),
                            time = .9,
                            bad_extra = ('2',))
waves1 = waves042811

waves042911 = IVCurveSeries(dirname + '/042911-10ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (200e-12, 20e-12),
                            time = .9,
                            bad_extra = ('2',))
waves2 = waves042911

waves050311 = IVCurveSeries(dirname + '/050311-4ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (300e-12, 20e-12),
                            time = .9)
waves3 = waves050311
waves050411 = IVCurveSeries(dirname + '/050411-7ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (300e-12, 20e-12),
                            time = .9,
                            bad_extra = ('2',))
waves4 = waves050411

waves050511 = IVCurveSeries(dirname + '/050511-3ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (200e-12, 20e-12),
                            time = .9)
waves5 = waves050511

waves050611 = IVCurveSeries(dirname + '/050611-5ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (300e-12, 20e-12),
                            time = .9)
waves6 = waves050611

waves051311 = IVCurveSeries(dirname + '/051311-9ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (100e-12, 20e-12),
                            time = .9)
waves7 = waves051311

waves051411 = IVCurveSeries(dirname + '/051411-5ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (200e-12, 20e-12),
                            time = .9)
waves8 = waves051411

waves051811 = IVCurveSeries(dirname + '/051811-13ivifcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (200e-12, 20e-12),
                            time = .9)
waves9 = waves051811

waves090612 = IVCurveSeries(dirname + '/090612-1ivcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (500e-12, 50e-12),
                            time = .9)
waves10 = waves090612

waves091312 = IVCurveSeries(dirname + '/091312-4ivcurves_Waves', params,
                            IV = (-500e-12, 50e-12),
                            IF = (200e-12, 20e-12),
                            time = .9)
waves11 = waves091312

waves = {
    'waves042811':waves042811,
    'waves042911':waves042911,
    'waves050311':waves050311,
    'waves050411':waves050411,
    'waves050511':waves050511,
    'waves050611':waves050611,
    'waves051311':waves051311,
    'waves051411':waves051411,
    'waves051811':waves051811,
    'waves090612':waves090612,
    'waves091312':waves091312,
}
