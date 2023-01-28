"""
pyFlySkyIbus.

FlySky Ibus python library for the raspberry pi.
"""

__version__ = "1.0.0"
__author__ = 'GamerHegi64'

import sys
from pathlib import Path
path_file = Path(sys.path[0])
print(path_file)

from .IBus import *