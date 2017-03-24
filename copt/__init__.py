__version__ = '0.2.0'

from .gradient_descent import minimize_PGD, minimize_DavisYin, minimize_APGD
from .primal_dual import fmin_CondatVu
from .stochastic import minimize_SAGA, minimize_BCD
from .utils import LogisticLoss, SquaredLoss, L1Norm, TotalVariation2D
from . import datasets
from . import tv_prox
