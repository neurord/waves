import os.path
from ajustador.optimize import SimulationResult
import measurements1 as ms1

dirname = os.path.dirname(__file__) + '/strange1'

high_baseline_post = SimulationResult(dirname + '/high_baseline_post', ms1.Params())

waves = {
    'high_baseline_post':high_baseline_post,
    }
