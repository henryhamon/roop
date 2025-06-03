#!/usr/bin/env python3
import numpy as _np
if not hasattr(_np, 'dtypes'):
    _np.dtypes = _np

import os
import sys
from roop import core

if __name__ == '__main__':
    core.run()
