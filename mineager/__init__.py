# SPDX-License-Identifier: MIT

import logging as __logging

__version__ = "0.3.0"
__author__ = "ooliver1"
__license__ = "MIT"
__title__ = "mineager"

from .run import *
from .websocket import *

__logging.getLogger(__name__).addHandler(__logging.NullHandler())
