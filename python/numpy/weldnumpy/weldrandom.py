import numpy as np
from numpy.random import *
from weldnumpy.weldarray import weldarray

def rand(*args):
    return weldarray(np.random.rand(*args))

# TODO: Define other similar array creation functions from numpy.random



