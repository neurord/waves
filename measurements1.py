import os.path
from ajustador.loader import Measurement

dirname = os.path.dirname(__file__)

waves042811 = Measurement(dirname + '/042811-6ivifcurves_Waves', bad_extra=('2',))
waves1 = waves042811
waves042911 = Measurement(dirname + '/042911-10ivifcurves_Waves', bad_extra=('2',))
waves2 = waves042911
waves050311 = Measurement(dirname + '/050311-4ivifcurves_Waves', IF=(300e-12, 20e-12))
waves3 = waves050311
waves050411 = Measurement(dirname + '/050411-7ivifcurves_Waves', IF=(300e-12, 20e-12), bad_extra=('2',))
waves4 = waves050411
waves050511 = Measurement(dirname + '/050511-3ivifcurves_Waves')
waves5 = waves050511
waves050611 = Measurement(dirname + '/050611-5ivifcurves_Waves', IF=(300e-12, 20e-12))
waves6 = waves050611
waves051311 = Measurement(dirname + '/051311-9ivifcurves_Waves', IF=(100e-12, 20e-12))
waves7 = waves051311
waves051411 = Measurement(dirname + '/051411-5ivifcurves_Waves')
waves8 = waves051411
waves051811 = Measurement(dirname + '/051811-13ivifcurves_Waves')
waves9 = waves051811
waves090612 = Measurement(dirname + '/090612-1ivcurves_Waves', IF=(-500e-12, 50e-12))
waves10 = waves090612
waves091312 = Measurement(dirname + '/091312-4ivcurves_Waves')
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
