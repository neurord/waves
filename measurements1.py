import os.path
from ajustador.loader import Measurement

dirname = os.path.dirname(__file__)

waves1 = Measurement(dirname + '/042811-6ivifcurves_Waves', bad_extra=('2',))
waves2 = Measurement(dirname + '/042911-10ivifcurves_Waves', bad_extra=('2',))
waves3 = Measurement(dirname + '/050311-4ivifcurves_Waves', IF=(300e-12, 20e-12))
waves4 = Measurement(dirname + '/050411-7ivifcurves_Waves', IF=(300e-12, 20e-12), bad_extra=('2',))
waves5 = Measurement(dirname + '/050511-3ivifcurves_Waves')
waves6 = Measurement(dirname + '/050611-5ivifcurves_Waves', IF=(300e-12, 20e-12))
waves7 = Measurement(dirname + '/051311-9ivifcurves_Waves', IF=(100e-12, 20e-12))
waves8 = Measurement(dirname + '/051411-5ivifcurves_Waves')
waves9 = Measurement(dirname + '/051811-13ivifcurves_Waves')
waves10 = Measurement(dirname + '/090612-1ivcurves_Waves', IF=(-500e-12, 50e-12))
waves11 = Measurement(dirname + '/091312-4ivcurves_Waves')

waves = (waves1, waves2, waves3, waves4, waves5, waves6, waves7,
         waves8, waves9, waves10, waves11)
