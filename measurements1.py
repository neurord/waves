import os.path
from ajustador.loader import Measurement

class Params(object):
    requires = ()
    provides = ('baseline_before', 'baseline_after',
                'steady_after', 'steady_before', 'steady_cutoff',
                'falling_curve_window', 'rectification_window',
                'injection_start', 'injection_end',
                'injection_interval')

    baseline_before = .2
    baseline_after = 0.75

    steady_after = .25
    steady_cutoff = 80

    falling_curve_window = 20
    rectification_window = 11

    injection_start = 0.2
    injection_end = 0.6

    @property
    def injection_interval(self):
        return self.injection_end - self.injection_start

    @property
    def steady_before(self):
        return self.injection_end

dirname = os.path.dirname(__file__)

waves042811 = Measurement(dirname + '/042811-6ivifcurves_Waves', bad_extra=('2',),
                          params=Params())
waves1 = waves042811
waves042911 = Measurement(dirname + '/042911-10ivifcurves_Waves', bad_extra=('2',),
                          params=Params())
waves2 = waves042911
waves050311 = Measurement(dirname + '/050311-4ivifcurves_Waves', IF=(300e-12, 20e-12),
                          params=Params())
waves3 = waves050311
waves050411 = Measurement(dirname + '/050411-7ivifcurves_Waves', IF=(300e-12, 20e-12), bad_extra=('2',),
                          params=Params())
waves4 = waves050411
waves050511 = Measurement(dirname + '/050511-3ivifcurves_Waves',
                          params=Params())
waves5 = waves050511
waves050611 = Measurement(dirname + '/050611-5ivifcurves_Waves', IF=(300e-12, 20e-12),
                          params=Params())
waves6 = waves050611
waves051311 = Measurement(dirname + '/051311-9ivifcurves_Waves', IF=(100e-12, 20e-12),
                          params=Params())
waves7 = waves051311
waves051411 = Measurement(dirname + '/051411-5ivifcurves_Waves',
                          params=Params())
waves8 = waves051411
waves051811 = Measurement(dirname + '/051811-13ivifcurves_Waves',
                          params=Params())
waves9 = waves051811
waves090612 = Measurement(dirname + '/090612-1ivcurves_Waves', IF=(-500e-12, 50e-12),
                          params=Params())
waves10 = waves090612
waves091312 = Measurement(dirname + '/091312-4ivcurves_Waves',
                          params=Params())
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
